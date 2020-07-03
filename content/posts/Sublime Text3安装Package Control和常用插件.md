+++
title= "Sublime Text3安装Package Control和常用插件"
draft = false
date= "2016-03-04 20:32:58"
+++

Sublime Text3 是文本编辑器中比较优秀的一款，安装第三方插件比较推荐使用包管理器 Package Control，使用快捷键`Ctrl + ``或点击`View > Show Console`可以打开命令行，然后在命令行输入如下命令即可安装：

```python
import urllib.request,os,hashlib; h = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```

安装完成后重启Sublime，使用快捷键`Ctrl + Shift + P`呼出快捷面板，然后输入`install package`后回车，此时搜索你需要的插件后回车即可安装。

