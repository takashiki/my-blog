+++
title= "PHP解析雅虎天气API代码分享"
draft = false
date= "2013-04-19 21:06:44"
+++

    雅虎天气API地址： http://weather.yahooapis.com/forecastrss
    有两个可选参数w和u，其中w参数是基于WOEID的城市代码，可以在网上根据城市英文名查到，u参数是设置返回数据中的摄氏和华氏（c为摄氏，f为华氏）。
    实际请求地址如：http://weather.yahooapis.com/forecastrss?w=15015432&u=c 
    返回数据为xml格式，含有命名空间，无法使用simpleXML处理，这次分享的代码就是使用XMLReader和DOMDocument来处理该数据（获取返回数据中的天气状况代码、温度及湿度值）。
    首先是使用XMLReader时的代码：
[php]$url = 'http://weather.yahooapis.com/forecastrss?w=15015432&u=c';
$reader = new XMLReader();
$reader->open($url,'utf-8');
while($reader->read()){
	if($reader->name == 'yweather:condition'){
		$code = $reader->getAttribute('code');	//获取天气代码
		$temp = $reader->getAttribute('temp');	//获取温度
	}
	if($reader->name == 'yweather:atmosphere'){
		$humi = $reader->getAttribute('humidity');	//获取湿度
	}
}[/php]

 然后是使用DOMDocument处理的代码：
[php]$url = 'http://weather.yahooapis.com/forecastrss?w=15015432&u=c';
$yweather = "http://xml.weather.yahoo.com/ns/rss/1.0";	//命名空间
$res = new DOMDocument();
$res->load($url);

$node = $res->getElementsByTagNameNS($yweather, 'atmosphere');
$humi = $node->item(0)->attributes->item(0)->nodeValue;		//获取湿度
$node = $res->getElementsByTagNameNS($yweather, 'condition');
$code = $node->item(0)->attributes->item(1)->nodeValue;		//获取天气代码
$temp = $node->item(0)->attributes->item(2)->nodeValue;		//获取温度[/php]
 最后我们要将数字格式的天气代码转换成相应的中文：
[php]function code2char($code){
	switch($code){
		case 0:
			return '龙卷风';
		case 1:
			return '热带风暴';
		case 2:
			return '暴风';
		case 3:
			return '大雷雨';
		case 4:
			return '雷阵雨';
		case 5:
			return '雨夹雪';
		case 6:
			return '雨夹雹';
		case 7:
			return '雪夹雹';
		case 8:
			return '冻雾雨';
		case 9:
			return '细雨';
		case 10:
			return '冻雨';
		case 11:
			return '阵雨';
		case 12:
			return '阵雨';
		case 13:
			return '阵雪';
		case 14:
			return '小阵雪';
		case 15:
			return '高吹雪';
		case 16:
			return '雪';
		case 17:
			return '冰雹';
		case 18:
			return '雨淞';
		case 19:
			return '粉尘';
		case 20:
			return '雾';
		case 21:
			return '薄雾';
		case 22:
			return '烟雾';
		case 23:
			return '大风';
		case 24:
			return '风';
		case 25:
			return '冷';
		case 26:
			return '阴';
		case 27:
			return '多云';
		case 28:
			return '多云';
		case 29:
			return '局部多云';
		case 30:
			return '局部多云';
		case 31:
			return '晴';
		case 32:
			return '晴';
		case 33:
			return '转晴';
		case 34:
			return '转晴';
		case 35:
			return '雨夹冰雹';
		case 36:
			return '热';
		case 37:
			return '局部雷雨';
		case 38:
			return '偶有雷雨';
		case 39:
			return '偶有雷雨';
		case 40:
			return '偶有阵雨';
		case 41:
			return '大雪';
		case 42:
			return '零星阵雪';
		case 43:
			return '大雪';
		case 44:
			return '局部多云';
		case 45:
			return '雷阵雨';
		case 46:
			return '阵雪';
		case 47:
			return '局部雷阵雨';
		default:
			return '水深火热';
	}[/php]