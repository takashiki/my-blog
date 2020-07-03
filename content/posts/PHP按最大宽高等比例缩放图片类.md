+++
title= "PHP按最大宽高等比例缩放图片类"
draft = false
date= "2013-05-07 16:54:49"
+++

   本来用phpthumb来缩略图片是十分方便的，但是最近在sae上写项目发现phpthumb在sae上保存文件时会出问题，想来实现一个简单的按最大宽高等比例缩放图片类也并不困难，于是便自己写了一个方便修改。
   需GD库支持，可支持jpg、jpeg、png、gif格式的图片，代码短小适合新手学习用。
 
[php]<?php
class slpic {
	//原图片文件，包含路径和文件名
	var $orpic;	
	//原图的临时图像
	var $tempic;
	//缩略图
	var $thpic;
	//原宽度
	var $width;	
	//原高度
	var $height;
	//图片类型
	var $type;
	//缩略后的宽度
	var $thwidth;
	//缩略后的高度
	var $thheight;
	
	function __construct($file){
		$this->orpic = $file;
		$infos = getimagesize($file);
		$this->width = $infos[0];
		$this->height = $infos[1];
		$this->type = $infos[2];
	}
	
	//根据用户所指定最大宽高来计算缩略图尺寸
	function cal_size($maxwidth, $maxheight){
		//缩略图最大宽度与最大高度比
		$thcrown = $maxwidth/$maxheight;    
		//原图宽高比
		$crown = $this->width/$this->height;    
		if($crown/$thcrown >= 1){
			$this->thwidth = $maxwidth;
			$this->thheight = $maxwidth/$crown;
		} else {
			$this->thheight = $maxheight;
			$this->thwidth = $maxheight*$crown;
		}
	}
	
	function init(){
		switch($this->type){
			case 1:		//GIF
				$this->tempic = imagecreatefromgif($this->orpic);
				break;
			case 2:		//JPG
				$this->tempic = imagecreatefromjpeg($this->orpic);
				break;
			case 3:		//PNG
				$this->tempic = imagecreatefrompng($this->orpic);
				break;
			default:
				echo '暂不支持该图片格式';
		}
	}

	function resize($maxwidth, $maxheight){
		//初始化图像
		$this->init();
		//计算出缩略图尺寸
		$this->cal_size($maxwidth, $maxheight);
		
		$this->thpic = imagecreatetruecolor($this->thwidth, $this->thheight);
		imagecopyresampled($this->thpic, $this->tempic, 0, 0, 0 ,0, $this->thwidth, $this->thheight, $this->width, $this->height);
	}
	
	function save($filename, $type){
		switch($type){
			case 'jpg':
			case 'jpeg':
				imagejpeg($this->thpic, $filename);
				break;
			case 'png':
				imagepng($$this->thpic, $filename);
				break;
			case 'gif':
				imagegif($$this->thpic, $filename);
				break;
			default:
				echo '暂不支持您所选择的格式';
		}
	}
}
?>[/php]
