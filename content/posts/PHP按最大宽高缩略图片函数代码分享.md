+++
title= "PHP按最大宽高缩略图片函数代码分享"
draft = false
date= "2013-05-03 21:51:02"
+++

 很简单的按照最大宽高来缩略图片的代码，方便新手和懒得自己写的人。
[php]function thumb($imagefile, $maxwidth, $maxheight) {
	$dim = getimagesize($imagefile);
	$width = $dim[0];	//原图宽度
	$height = $dim[1];	//原图高度
	$original = imagecreatefromjpeg($imagefile);
	
	$thcrown = $maxwidth/$maxheight;	//缩略图最大宽度与最大高度比
	$crown = $width/$height;	//原图宽高比
	if($crown/$thcrown >= 1){
		$thumbWidth = $maxwidth;
		$thumbHeight = $maxwidth/$crown;
	} else {
		$thumbHeight = $maxheight;
		$thumbWidth = $maxheight*$crown;
	}
	
	$thumb = imagecreatetruecolor($thumbWidth, $thumbHeight);
	imagecopyresampled($thumb, $original, 0, 0, 0, 0, $thumbWidth, $thumbHeight, $width, $height);
	return $thumb;
}[/php]
