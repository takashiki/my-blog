+++
title= "PHP分页函数代码分享"
draft = false
date= "2013-05-05 15:50:01"
+++

   分页是经常会用到的一个模块，网上的分页函数和分页类的代码都相当多。为了能让分页函数的代码通用性更强，我自改了一个分页函数分享给大家。
   本代码中不包含样式，如果需要对应的CSS样式的话，可以参考 http://www.oschina.net/code/snippet_4873_3810
 
[php]<br />
//$count为总条目数，$page为当前页码，$page_size为每页显示条目数<br />
function show_page($count,$page,$page_size)
{
	$page_count  = ceil($count/$page_size);  //计算得出总页数

	$init=1;
	$page_len=7;
	$max_p=$page_count;
	$pages=$page_count;

	//判断当前页码
	$page=(empty($page)||$page<0)?1:$page;
	//获取当前页url
	$url = $_SERVER['REQUEST_URI'];
	//去掉url中原先的page参数以便加入新的page参数
	$parsedurl=parse_url($url);
	$url_query = isset($parsedurl['query']) ? $parsedurl['query']:'';
	if($url_query != ''){
		$url_query = preg_replace("/(^|&)page=$page/",'',$url_query);
		$url = str_replace($parsedurl['query'],$url_query,$url);
		if($url_query != ''){
			$url .= '&';
		}
	} else {
		$url .= '?';
	}
	
	//分页功能代码
	$page_len = ($page_len%2)?$page_len:$page_len+1;  //页码个数
	$pageoffset = ($page_len-1)/2;  //页码个数左右偏移量

	$navs='';
	if($pages != 0){
		if($page!=1){
			$navs.="<a href=\"".$url."page=1\">首页</a> ";		//第一页
			$navs.="<a href=\"".$url."page=".($page-1)."\">上页</a>";	//上一页
		} else {
			$navs .= "<span class='disabled'>首页</span>";
			$navs .= "<span class='disabled'>上页</span>";
		}
		if($pages>$page_len)
		{
			//如果当前页小于等于左偏移
			if($page<=$pageoffset){
				$init=1;
				$max_p = $page_len;
		    }
		    else  //如果当前页大于左偏移
		    {    
			    //如果当前页码右偏移超出最大分页数
				if($page+$pageoffset>=$pages+1){
					$init = $pages-$page_len+1;
				}
				else
				{
					//左右偏移都存在时的计算
					$init = $page-$pageoffset;
					$max_p = $page+$pageoffset;
				}
			}
	    }
	    for($i=$init;$i<=$max_p;$i++)
	    {
		    if($i==$page){$navs.="<span class='current'>".$i.'</span>';} 
		    else {$navs.=" <a href=\"".$url."page=".$i."\">".$i."</a>";}
	    }
	    if($page!=$pages)
	    {
		    $navs.=" <a href=\"".$url."page=".($page+1)."\">下页</a> ";//下一页
		    $navs.="<a href=\"".$url."page=".$pages."\">末页</a>";	//最后一页
	    } else {
			$navs .= "<span class='disabled'>下页</span>";
			$navs .= "<span class='disabled'>末页</span>";
		}
	    echo "$navs";
   }
}   [/php]
