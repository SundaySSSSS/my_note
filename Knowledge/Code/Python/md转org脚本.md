# md转org脚本
```python
# -*- coding: utf-8 -*-
import os
import re

def checkTitle(md_line):
    """
    判定为标题的依据为以若干#开始，并在#之后有一个空格
    并认为标题中只是纯文本, 不存在其他字体等变化
    返回值: 0-不是标题, 1-6: 标题级数
    """
    line = md_line.strip()
    find_str = "# "
    for i in range(6):
        if line.startswith(find_str):
            return i + 1
        find_str = "#" + find_str
    return 0


def titleMd2Org(md_line):
    """
    把md格式的标题转化为org格式
    返回值: 空-转换失败, 非空-转换后的标题
    """
    line = md_line.strip()
    title_level = checkTitle(line)
    if title_level == 0:
        print("title md 2 org failed, can not recog title level")
        org_line = ""
    else:
        org_line = "*" * title_level + " " + line[title_level + 1:]
    return org_line


def checkCode(md_line):
    """
    检查是否为代码开始或结束标记
    返回值: 0-不是代码开始结束标记 1-代码开始或结束标记
    """
    line = md_line.strip()
    if line.startswith("```"):
        return 1
    else:
        return 0


def codeMd2Org(md_line, flag):
    """
    将代码开始标记或结束标记转换为org格式
    参数: 
    md_line: 待处理行
    flag: 0-此行为代码片开始标记 1-此行是代码片结束标记
    返回值: 转换后的行
    """
    if flag == 0:
        org_line = "#+BEGIN_SRC"
    elif flag == 1:
        org_line = "#+END_SRC"
    else:
        print("flag is error %d" % flag)
        org_line = ""
    return org_line


def checkImage(md_line):
    """
    检查此行是否为图片引用
    返回值: 0-不是图片引用 1-是图片引用
    """
    line = md_line.strip()
    if line.startswith("!["):
        return 1
    else:
        return 0


def imageMd2Org(md_line):
    line = md_line.strip()
    # vnote的图片引用格式为:![dlam](_v_images/_dlam_1511075666_29358.jpg)
    m = re.findall("!\[(.*)\]\((.*)\)", line)
    if (len(m) != 0):
        image_title = m[0][0]
        image_path = m[0][1]
        # print m
        org_line = "[[file:" + image_path + "]]"
    else:
        print("this line is not image")
        org_line = ""
    return org_line


isInCode = False


def line_md2org(md_line):
    """
    将本行从md格式转化为org格式
    """
    global isInCode
    line = md_line.strip()
    
    if checkTitle(line) > 0:
        return titleMd2Org(line)
    elif checkCode(line) > 0:
        if isInCode:
            flag = 1
        else:
            flag = 0
        line = codeMd2Org(line, flag)
        isInCode = not isInCode;
        return line
    elif checkImage(line):
        return imageMd2Org(line)
    else:
        return md_line


def replaceWindowsM2N(line):
    """
    把windows下行尾的^M替换为\n
    """
    if line.endswith("\r\n"):
        unix_line = line[:-2] + "\n"
    else:
        unix_line = line + "\n"
    return unix_line


def fileMd2Org(md_file, org_file):
    f_md = open("md_file", 'r')
    f_org = open("org_file", 'w')

    isInCode = False
    md_lines = f_md.readlines()
    for md_line in md_lines:
        org_line = line_md2org(md_line)
        # print org_line
        f_org.write(replaceWindowsM2N(org_line))
    f_md.close()
    f_org.close()


def main():
    path = r"F:\Code\SVN\nvc200EH_SVN_Ver87"
    for rt, dirs, files in os.walk(path):
        for f in files:
            file_path = os.path.join(rt, f)
            print(file_path)


if __name__ == "__main__":
    main()

```