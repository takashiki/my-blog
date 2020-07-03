+++
title= " 删除指定的html标签"
draft = false
date= "2013-11-22 19:02:00"
+++

    php函数strip_tags可设置保留的标签，但不能去除指定的标签，所以仿strip_tags的调用方式写了这个简单的函数。 前两个参数的使用方法与strip_tags相同，$clear参数可指定是否去除标签内的内容。

```php
function _strip_tags($str, $tags, $clear = false) 
{//去除指定html标签，$clear设为true时同时清除标签内容   
  $tagsArr = explode('<', $tags);
  unset($tagsArr[0]);
  foreach ($tagsArr as $tag) {  
    $tag = trim($tag, '>');
    if($clear) {
      $p[] = "/<".$tag.".*<\/".$tag.">/i";
    } else {
      $p[] = "/(<(?:\/".$tag."|".$tag.")[^>]*>)/i";  
    }
  }  
  $return_str = preg_replace($p,"",$str);  
  return $return_str;  
}
```