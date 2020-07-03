+++
title= "新手学web开发杂记（十二）——bmp转GD函数"
draft = false
date= "2013-09-27 13:46:00"
+++

   最近在工作中需要把bmp图片转成jpg图片，但无奈的是网上能找到的bmp转gd的类或函数或多或少都有些问题。其中绝大多数在处理16位bmp图片时要么全黑全粉，要么干脆转换不出，其余有些根本不支持32位的bmp图片。
   最后我终于在php的官网上找到了解决方法。原来网上流传最广的一个仿GD的imagecreatefrombmp函数是一个有问题的版本，无法正确处理16位bmp图片，但好在官网上有人给出了修正方法，修正好的代码如下：

```php
/**
 * BMP 创建函数
 * @author simon
 * @modified by 天心流水
 * @param string $filename path of bmp file
 * @example who use,who knows
 * @return resource of GD
 */ 
function imagecreatefrombmp( $filename ) {
	if ( !$f1 = fopen( $filename, "rb" ) )
		return FALSE;
	
	$FILE = unpack( "vfile_type/Vfile_size/Vreserved/Vbitmap_offset", fread( $f1, 14 ) );
	if ( $FILE['file_type'] != 19778 )
		return FALSE;
	
	$BMP = unpack( 'Vheader_size/Vwidth/Vheight/vplanes/vbits_per_pixel' . '/Vcompression/Vsize_bitmap/Vhoriz_resolution' . '/Vvert_resolution/Vcolors_used/Vcolors_important', fread( $f1, 40 ) );
	$BMP['colors'] = pow( 2, $BMP['bits_per_pixel'] );
	if ( $BMP['size_bitmap'] == 0 )
		$BMP['size_bitmap'] = $FILE['file_size'] - $FILE['bitmap_offset'];
	$BMP['bytes_per_pixel'] = $BMP['bits_per_pixel'] / 8;
	$BMP['bytes_per_pixel2'] = ceil( $BMP['bytes_per_pixel'] );
	$BMP['decal'] = ($BMP['width'] * $BMP['bytes_per_pixel'] / 4);
	$BMP['decal'] -= floor( $BMP['width'] * $BMP['bytes_per_pixel'] / 4 );
	$BMP['decal'] = 4 - (4 * $BMP['decal']);
	if ( $BMP['decal'] == 4 )
		$BMP['decal'] = 0;
	
	$PALETTE = array();
  if ($BMP['colors'] < 16777216 && $BMP['colors'] != 65536)
  {
    $PALETTE = unpack('V'.$BMP['colors'], fread($f1,$BMP['colors']*4));
  }
	
	$IMG = fread( $f1, $BMP['size_bitmap'] );
	$VIDE = chr( 0 );
	
	$res = imagecreatetruecolor( $BMP['width'], $BMP['height'] );
	$P = 0;
	$Y = $BMP['height'] - 1;
	while( $Y >= 0 ){
		$X = 0;
		while( $X < $BMP['width'] ){
			if ( $BMP['bits_per_pixel'] == 32 ){
				$COLOR = unpack( "V", substr( $IMG, $P, 3 ) );
				$B = ord(substr($IMG, $P,1));
				$G = ord(substr($IMG, $P+1,1));
				$R = ord(substr($IMG, $P+2,1));
				$color = imagecolorexact( $res, $R, $G, $B );
				if ( $color == -1 )
					$color = imagecolorallocate( $res, $R, $G, $B );
				$COLOR[0] = $R*256*256+$G*256+$B;
				$COLOR[1] = $color;
			} elseif ( $BMP['bits_per_pixel'] == 24 ) {
				$COLOR = unpack( "V", substr( $IMG, $P, 3 ) . $VIDE );
      } elseif ( $BMP['bits_per_pixel'] == 16 ){
        $COLOR = unpack("v",substr($IMG,$P,2));
        $blue  = (($COLOR[1] & 0x001f) << 3) + 7;
        $green = (($COLOR[1] & 0x03e0) >> 2) + 7;
        $red   = (($COLOR[1] & 0xfc00) >> 7) + 7;
        $COLOR[1] = $red * 65536 + $green * 256 + $blue;
			} elseif ( $BMP['bits_per_pixel'] == 8 ){
				$COLOR = unpack( "n", $VIDE . substr( $IMG, $P, 1 ) );
				$COLOR[1] = $PALETTE[$COLOR[1] + 1];
			} elseif ( $BMP['bits_per_pixel'] == 4 ){
				$COLOR = unpack( "n", $VIDE . substr( $IMG, floor( $P ), 1 ) );
				if ( ($P * 2) % 2 == 0 )
					$COLOR[1] = ($COLOR[1] >> 4);
				else
					$COLOR[1] = ($COLOR[1] & 0x0F);
				$COLOR[1] = $PALETTE[$COLOR[1] + 1];
			} elseif ( $BMP['bits_per_pixel'] == 1 ){
				$COLOR = unpack( "n", $VIDE . substr( $IMG, floor( $P ), 1 ) );
				if ( ($P * 8) % 8 == 0 )
					$COLOR[1] = $COLOR[1] >> 7;
				elseif ( ($P * 8) % 8 == 1 )
					$COLOR[1] = ($COLOR[1] & 0x40) >> 6;
				elseif ( ($P * 8) % 8 == 2 )
					$COLOR[1] = ($COLOR[1] & 0x20) >> 5;
				elseif ( ($P * 8) % 8 == 3 )
					$COLOR[1] = ($COLOR[1] & 0x10) >> 4;
				elseif ( ($P * 8) % 8 == 4 )
					$COLOR[1] = ($COLOR[1] & 0x8) >> 3;
				elseif ( ($P * 8) % 8 == 5 )
					$COLOR[1] = ($COLOR[1] & 0x4) >> 2;
				elseif ( ($P * 8) % 8 == 6 )
					$COLOR[1] = ($COLOR[1] & 0x2) >> 1;
				elseif ( ($P * 8) % 8 == 7 )
					$COLOR[1] = ($COLOR[1] & 0x1);
				$COLOR[1] = $PALETTE[$COLOR[1] + 1];
			}else
				return FALSE;
			imagesetpixel( $res, $X, $Y, $COLOR[1] );
			$X++;
			$P += $BMP['bytes_per_pixel'];
		}
		$Y--;
		$P += $BMP['decal'];
	}
	fclose( $f1 );
	
	return $res;
}
```