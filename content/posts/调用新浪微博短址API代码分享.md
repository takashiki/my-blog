+++
title= "调用新浪微博短址API代码分享"
draft = false
date= "2013-04-15 21:10:47"
+++

  之前的一篇博客里有提到调用新浪微博API转短址，而我发现现在不少人都有使用新浪微博短链接口的需求。这对于老手来说自然是小菜一碟，但是初学者很可能在写该代码时花不少时间，所以我就把自己 写的代码分享出来供大家参考一下。
  使用前请先在新浪微博开放平台上创建应用获取APPID（但根据我的经验，未通过审核的应用的APPID调用时会发生错误，原因是权限不够，不过别担心，去百度上搜一个能用的就行了）。
  PS:本代码参考自Jucelin(http://jucelin.com/)共享的旧版API调用代码，由于新版API改了不少地方，旧代码不能使用，所以本人修改后分享出来
[php]<?php
$backurl="";
if (isset($_GET['type'])){
	$type=$_GET['type'];
	switch (trim($type))
	{
	case 1:
		if (isset($_GET['url'])){
			$backurl=shorturl(urlencode($_GET['url']));  //注意必须经过urlencode
		}
		else{
			$backurl="error0";
		}
		break;
	case 2:
		if (isset($_GET['url'])){
			$backurl=expandurl($_GET['url']);
		}
		else{
			$backurl="error1";
		}
		break;
	default:
		$backurl="error2";
	}
}
echo $backurl;

function shortenSinaUrl($long_url){
	$apiKey='xxxxxxxxx';    //请替换成你的APPID
	$apiUrl='https://api.weibo.com/2/short_url/shorten.json?source='.$apiKey.'&url_long='.$long_url;
	$curlObj = curl_init();
	curl_setopt($curlObj, CURLOPT_URL, $apiUrl);
	curl_setopt($curlObj, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($curlObj, CURLOPT_SSL_VERIFYPEER, 0);
	curl_setopt($curlObj, CURLOPT_HEADER, 0);
	curl_setopt($curlObj, CURLOPT_HTTPHEADER, array('Content-type:application/json'));
	$response = curl_exec($curlObj);
	curl_close($curlObj);
	$json = json_decode($response);
	return $json->urls[0]->url_short;
}

function expandSinaUrl($short_url){
	$apiKey='xxxxxxxxx';    //请替换成你的APPID
	$apiUrl='https://api.weibo.com/2/short_url/expand.json?source='.$apiKey.'&url_short='.$short_url;
	$curlObj = curl_init();
	curl_setopt($curlObj, CURLOPT_URL, $apiUrl);
	curl_setopt($curlObj, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($curlObj, CURLOPT_SSL_VERIFYPEER, 0);
	curl_setopt($curlObj, CURLOPT_HEADER, 0);
	curl_setopt($curlObj, CURLOPT_HTTPHEADER, array('Content-type:application/json'));
	$response = curl_exec($curlObj);
	curl_close($curlObj);
	$json = json_decode($response);
	return $json->urls[0]->url_long;
}


function shorturl($long_url){
	$apiKey='xxxxxxxxx';    //请替换成你的APPID
	$apiUrl='https://api.weibo.com/2/short_url/shorten.json?source='.$apiKey.'&url_long='.$long_url;
	$response = file_get_contents($apiUrl);
	$json = json_decode($response);
	return $json->urls[0]->url_short;
}

function expandurl($short_url){
	$apiKey='xxxxxxxxx';    //请替换成你的APPID
	$apiUrl='https://api.weibo.com/2/short_url/expand.json?source='.$apiKey.'&url_short='.$short_url;
	$response = file_get_contents($apiUrl);
	$json = json_decode($response);
	return $json->urls[0]->url_long;
}
?>[/php]