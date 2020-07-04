# 传入 Obsidian 博文目录作为参数
# 
# 先获取所有文件名
#
# 循环处理文件：
#    1. 将文件名和修改时间提取成 Hugo 的 Meta 信息
#    2. 对文件内 Tag 进行匹配，如有的话调整为 Hugo 的 Meta 中 tags 部分
#    3. 对文件内 backlink 部分进行匹配，如果 link 文件存在，改为 markdown 格式，否则改为纯文本
# 
# 所有文件处理成功后调用系统命令：
#    1. 调用 Hugo 进行页面生成：hugo 
#    2. 调用 Git 上传变更

import os, sys, getopt, time, re

def main(argv):
    opts, args = getopt.getopt(argv, "d:")
    opts = dict(opts)
    srcDir = opts['-d']
    procPosts(srcDir)

def procPosts(dir):
    if not os.path.isdir(dir):
        print('dir not exits')
        sys.exit(2)

    files = os.listdir(dir)
    for file in files:
        procPost(os.path.join(dir, file), files)

def procPost(path, files):
    filename = os.path.basename(path)
    title = os.path.splitext(filename)[0]
    timestamp = os.path.getmtime(path)
    date = time.strftime('%Y-%m-%dT%H:%M:%S+08:00', time.localtime(timestamp))
    text = '''+++
title = "%s"
draft = false
date = "%s"
''' % (title, date)
    
    f = open(path)
    content = f.read()
    f.close()

    ms = re.match('(\+\+\+|---|\*\*\*|===)?\s*((tags|series|categories):\s*((#\S+)\s+)+\s*)+(\+\+\+|---|\*\*\*|===)?', content, re.DOTALL | re.IGNORECASE)
    if (ms is not None):
        meta = ms.group()
        ts = getMetas('tags', meta)
        text += 'tags = [' + ','.join(map(lambda x: '"' + x + '"', ts)) + ']\n'
        ss = getMetas('series', meta)
        text += 'series = [' + ','.join(map(lambda x: '"' + x + '"', ss)) + ']\n'
        cs = getMetas('categories', meta)
        text += 'categories = [' + ','.join(map(lambda x: '"' + x + '"', cs)) + ']\n'
        content = content.replace(ms.group(), '')

    text += '+++\n\n' + content

    f = open('content/posts/' + filename, 'w')
    f.write(text)
    f.close

def getMetas(type, meta):
    p = '.*(^' + type + ':[^\n]*)'
    ms = re.match(p, meta, re.DOTALL | re.MULTILINE)
    if (ms is not None):
        return re.findall('#(\S+)', ms.group(1))

    return []

if __name__ == "__main__":
    main(sys.argv[1:])