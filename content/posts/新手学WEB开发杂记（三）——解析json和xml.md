+++
title= "新手学WEB开发杂记（三）——解析json和xml"
draft = false
date= "2013-04-10 19:19:33"
+++

JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。XML (Extensible Markup Language, XML) 是用于标记电子文件使其具有结构性的标记语言，可以用来标记数据、定义数据类型，是一种允许用户对自己的标记语言进行定义的源语言。
目前JSON和XML被广泛地用在各种API的返回数据的格式化上。现在是一个API爆发的时代，各种网站都开始提供自己的API给开发者使用，所以对json和xml格式的数据解析有一定的了解是相当必要的。
PHP解析json格式数据的函数是json_decode()。
它的第一个参数为待处理的json格式字符串，第二个参数assoc默认为false即返回值为object型，若设为true则返回数组类型数据。
JSON建构有数组和对象两种结构，若为纯数组结构的json数据，则经过json_decode后返回的数据可按照数组的访问方式，即形如$arr[0]的方式访问数据。若为纯对象结构，则可通过形如$obj->attr的方式进行访问。对于比较复杂的数组和对象混合的json格式数据在访问时，需按照其结构选择访问方式，如$json->arr[0]->attr。
PHP对XML格式的支持也相当不错，常见的几种处理XML格式的技术有:XML Expat Parser、SimpleXML、XMLReader、DOMDocument等。
其中SimpleXML是PHP5后提供的一套简单易用的xml工具集，可以把xml转换成方便处理的对象，也可以组织生成xml数据。不过它不适用于包含namespace的xml，而且要保证xml格式完整(well-formed)。
DOMDocument是PHP5后推出的DOM扩展的一部分，可用来建立或解析html/xml，目前只支持utf-8编码。它与javascript十分地相像。
XMLReader也是PHP5之后的扩展（5.1后默认安装）。它就像游标一样在文档流中移动，并在每个节点处停下来。它与simpleXML及DOMDocument的很大的不同在于，它更注重于获取XML元素的属性而非元素的值。即解析形如<tagname text="text"/>的XML数据选用XMLReader更方便。