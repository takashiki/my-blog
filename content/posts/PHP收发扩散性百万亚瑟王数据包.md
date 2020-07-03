+++
title= "PHP收发扩散性百万亚瑟王数据包"
draft = false
date= "2013-12-04 10:25:00"
+++

   扩散性百万亚瑟王是去年在日本很火的一款卡牌类手游，今年盛大代理后国内玩家增长了很多，挂机科技也逐渐多了起来。大多数科技的源头应该都是Mawalker，非常感谢原作者的无私开源，才能促成现在科技百花齐放的情况，造福广大玩家。 
   我想将mawalker用php来改写出来，无奈在收发数据包方面就卡住了。后来在群友的帮助以及网上查找到的资料的帮助下终于完成了，于是便将最基本的登录代码公布出来以供大家参考。

```php
require("snoopy.php");
$key = "uH9JF2cHf6OppaC10000000000000000";
$url = "http://web.million-arthurs.com/connect/app/login?cyt=1";
$vars['login_id'] = Security::encrypt('yourid' , $key );
$vars['password'] = Security::encrypt('password' , $key );
$snoopy = new Snoopy();
$snoopy->agent = "Million/250 (t03gchn; t03gzc; 4.1.2) samsung/t03gzc/t03gchn:4.1.2/JZO54K/N7100ZCDMD3:user/release-keys GooglePlay";
$snoopy->rawheaders["DontTrackMeHere"] = "gzip, deflate";
$snoopy->submit($url, $vars);
$ret = $snoopy->results;

echo Security::decrypt(base64_encode($ret), $key );

class Security {
	public static function encrypt($input, $key) {
	$size = mcrypt_get_block_size(MCRYPT_RIJNDAEL_128, MCRYPT_MODE_ECB);
	$input = Security::pkcs5_pad($input, $size);
	$td = mcrypt_module_open(MCRYPT_RIJNDAEL_128, '', MCRYPT_MODE_ECB, '');
	$iv = mcrypt_create_iv (mcrypt_enc_get_iv_size($td), MCRYPT_RAND);
	mcrypt_generic_init($td, $key, $iv);
	$data = mcrypt_generic($td, $input);
	mcrypt_generic_deinit($td);
	mcrypt_module_close($td);
	$data = base64_encode($data);
	return $data;
	}
 
	private static function pkcs5_pad ($text, $blocksize) {
		$pad = $blocksize - (strlen($text) % $blocksize);
		return $text . str_repeat(chr($pad), $pad);
	}
 
	public static function decrypt($sStr, $sKey) {
		$decrypted= mcrypt_decrypt(
		MCRYPT_RIJNDAEL_128,
		$sKey,
		base64_decode($sStr),
		MCRYPT_MODE_ECB
	        );
 
		$dec_s = strlen($decrypted);
		$padding = ord($decrypted[$dec_s-1]);
		$decrypted = substr($decrypted, 0, -$padding);
		return $decrypted;
	}	
}
```
   代码中使用了snoopy类，这个类可以很容易找到，而aes编解码所使用的类也是网上找到的，可以兼容java的aes编解码。snoopy类也可以换成curl，有能力的可以自己改。另外login的登录加密key是不带login_id的，另一种加密的key需要带login_id，具体可以看mawalker。