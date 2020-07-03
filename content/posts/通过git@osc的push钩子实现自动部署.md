+++
title= "通过git@osc的push钩子实现自动部署"
draft = false
date= "2016-04-01 19:59:00"
+++

[Git@OSC](http://git.oschina.net/)可以称得上是国内的github了，在国内网络情势严峻的情况下，使用Git@OSC也是一个不错的选择。

最近想要把博客和自己的一个小站[Mugen千寻平台](http://takashiki.sinaapp.com)从sae迁移到vps上，总的来说就是两个字——折腾。为了解决自动部署问题，查询了一些解决方案后，为了稳定最终决定使用Git@OSC来实现该需求。

Git@OSC的push钩子的详细说明参见[HOOK钩子](http://git.oschina.net/oschina/git-osc/wikis/HOOK%E9%92%A9%E5%AD%90)，钩子会post过去的数据格式如下

```
{
    password: "password",
    push_data: {
        before: "fc85635faaf34c6f5104874bce9856c03be9b311",
        after: "40dea1b0efb0a3d3f71e8c302d642fe3588c254c",
        ref: "refs/heads/master",
        user_id: 用户id,
        user_name: "用户名",
        repository: {
            name: "Test",
            url: "git@git.oschina.net:takashiki/Test.git",
            description: "描述",
            homepage: "http://git.oschina.net/takashiki/Test"
        },
        commits: [
            {
                id: "40dea1b0efb0a3d3f71e8c302d642fe3588c254c",
                message: "test",
                timestamp: "2015-07-21T16:38:58+08:00",
                url: "http://git.oschina.net/takashiki/Test/commit/40dea1b0efb0a3d3f71e8c302d642fe3588c254c",
                author: {
                    name: "username",
                    email: "username@xxx.com"
                }
            }
        ],
        total_commits_count: 1
    }
}
```

每次push时，钩子都会访问我们设定的地址，这样只要我们写一个自动pull代码的脚本就可以实现自动发布了。

```php
<?php
header("Content-type: text/html; charset=utf-8");

if (! isset($_REQUEST['hook'])) die ('非法请求');

$config = require('config.php');
//hook内容详见http://git.oschina.net/oschina/git-osc/wikis/HOOK%E9%92%A9%E5%AD%90
$hook = json_decode($_REQUEST["hook"], true);
//$hook = json_decode(file_get_contents('request.json'), true);
$project = $hook['push_data']['repository']['name'];

//判断密码
if ($hook['password'] != $config['projects'][$project]['password']) die ("密码错误");
//判断branch
if (trim(strrchr($hook['push_data']['ref'], '/'), '/') != $config['projects'][$project]['branch']) die ("非自动部署分支");

$shell = <<<EOF
WEB_PATH='{$config['projects'][$hook['push_data']['repository']['name']]['web_path']}'
WEB_USER='{$config['web_user']}'
WEB_GROUP='{$config['web_group']}'

echo "Start deployment"
cd \$WEB_PATH
echo "pulling source code..."
git reset --hard origin/master
git clean -f
git pull
git checkout master
echo "changing permissions..."
chown -R \$WEB_USER:\$WEB_GROUP \$WEB_PATH
echo "Finished."
EOF;

file_put_contents('deploy.sh', $shell);
$res = shell_exec("bash deploy.sh");

$log_file = "{$project}.log";
foreach ($hook['push_data']['commits'] as $commit) {
    file_put_contents($log_file, 
        "※" . date('Y-m-d H:i:s') . "\t" . 
        $hook['push_data']['repository']['name'] . "\t" . 
        $commit['message'] . "\t" . 
        $commit['author']['name'] . PHP_EOL, 
        FILE_APPEND
    );
}
file_put_contents($log_file, $res . PHP_EOL, FILE_APPEND);

```

```php
<?php
return [
    'web_user' => 'www',
    'web_group' => 'www',
    'projects' => [
        'project' => [
            'password' => 'password',
            'web_path' => '/home/wwwroot/default/project',
        ],
    ]
];

```

将这两个文件放在可以被访问的地方，需要注意的是，web用户需要有该文件夹的读写权限，而且web用户需要有自己的home目录，且home目录内有.ssh文件夹，文件夹内的公钥已添加到Git@OSC上，这样脚本的git pull才能正常使用。

最近写了另一个版本的部署代码，这个版本不需要web用户使用ssh方式访问git，而是直接在url中加上了用户名和密码，我自己是建了一个小号专门用于部署的，这样更方便但不够安全，仅供参考，详见 [https://github.com/takashiki/tool-scripts/blob/master/deploy.php](https://github.com/takashiki/tool-scripts/blob/master/deploy.php)。
