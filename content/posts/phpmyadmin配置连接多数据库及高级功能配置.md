+++
title= "phpmyadmin配置连接多数据库及高级功能配置"
draft = false
date= "2015-07-03 15:32:00"
+++

配置多数据库连接很简单，将phpmyadmin的config.inc.php中原本的服务器连接部分的内容修改为：

```php
$cfg['AllowArbitraryServer'] = true; 

$db_servers = array(
	1 => array(
		'host' => 'localhost',
		'user' => 'root',
		'password' => '123456',
		'port' => '3306',
	),
	2 => array(
	    'host'   => '192.168.65.168',
	    'user'   => 'root',
	    'password' => '123456',
	    'port' => '3306',
	),
);

for ($i = 1; $i <= count($db_servers); $i++) {
	$cfg['Servers'][$i]['auth_type'] = 'cookie';
	$cfg['Servers'][$i]['user'] = $db_servers[$i]['user'];
	$cfg['Servers'][$i]['password'] = $db_servers[$i]['password'];
	$cfg['Servers'][$i]['host'] = $db_servers[$i]['host'];
	$cfg['Servers'][$i]['port'] = $db_servers[$i]['port'];
	$cfg['Servers'][$i]['connect_type'] = 'tcp';
	$cfg['Servers'][$i]['compress'] = false;
	$cfg['Servers'][$i]['AllowNoPassword'] = false;
}
```

这样就可以在登录时选择服务器了。

登录验证方式改为cookie后，phpmyadmin会提示“phpMyAdmin 高级功能未全部设置，部分功能不可用”。高级功能虽然不是必要的，但要开启的话其实也很方便，步骤如下：

1. 在数据库中导入phpmyadmin/sql目录下的create_tables.sql文件。
2. 执行以下的语句创建pma用户并赋权：

```sql
GRANT USAGE ON mysql.* TO 'pma'@'localhost' IDENTIFIED BY 'pmapass';
GRANT SELECT (
  Host, User, Select_priv, Insert_priv, Update_priv, Delete_priv,
  Create_priv, Drop_priv, Reload_priv, Shutdown_priv, Process_priv,
  File_priv, Grant_priv, References_priv, Index_priv, Alter_priv,
  Show_db_priv, Super_priv, Create_tmp_table_priv, Lock_tables_priv,
  Execute_priv, Repl_slave_priv, Repl_client_priv
  ) ON mysql.user TO 'pma'@'localhost';
GRANT SELECT (Host, Db, User, Table_name, Table_priv, Column_priv)
  ON mysql.tables_priv TO 'pma'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON phpmyadmin.* TO 'pma'@'localhost';
GRANT SELECT ON mysql.db TO 'pma'@'localhost';
```

并用`FLUSH PRIVILEGES;`来使权限生效。

3. 在config.inc.php中增加以下内容：

```php
$cfg['Servers'][$i]['controluser'] = 'pma';
		$cfg['Servers'][$i]['controlpass'] = 'pmapass';
		$cfg['Servers'][$i]['pmadb'] = 'phpmyadmin';
		$cfg['Servers'][$i]['bookmarktable'] = 'pma__bookmark';
		$cfg['Servers'][$i]['relation'] = 'pma__relation';
		$cfg['Servers'][$i]['table_info'] = 'pma__table_info';
		$cfg['Servers'][$i]['pdf_pages'] = 'pma__pdf_pages';
		$cfg['Servers'][$i]['table_coords'] = 'pma__table_coords';
		$cfg['Servers'][$i]['column_info'] = 'pma__column_info';
		$cfg['Servers'][$i]['history'] = 'pma__history';
		$cfg['Servers'][$i]['recent'] = 'pma__recent';
		$cfg['Servers'][$i]['table_uiprefs'] = 'pma__table_uiprefs';
		$cfg['Servers'][$i]['users'] = 'pma__users';
		$cfg['Servers'][$i]['usergroups'] = 'pma__usergroups';
		$cfg['Servers'][$i]['navigationhiding'] = 'pma__navigationhiding';
		$cfg['Servers'][$i]['tracking'] = 'pma__tracking';
		$cfg['Servers'][$i]['userconfig'] = 'pma__userconfig';
		$cfg['Servers'][$i]['designer_coords'] = 'pma__designer_coords';
		$cfg['Servers'][$i]['favorite'] = 'pma__favorite';
		$cfg['Servers'][$i]['savedsearches'] = 'pma__savedsearches';
```

OK,大功搞成了。
