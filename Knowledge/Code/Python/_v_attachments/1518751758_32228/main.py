# -*- coding: gb2312 -*-
from excel_tools import list2Excel
from log_parse import LogParser
import re

sim_list = []

def fliterFuncFront(line):
    if (line.strip().find(r"ProcessButtonThread : Similarity Test algId = 1, buf") >= 0):
        return True
    else:
        return False

def processFuncFront(line):
    outLine = ""
    m = re.findall(r"(.*) --- ProcessButtonThread : Similarity Test algId = 1, buf = (.*)", line)
    if (len(m) != 0):
        outLine = "%s --- front sim = %s\n" % m[0]
        sim_list.append(m[0])
    else:
        outLine = "something error in %s\n" % line
    return outLine

def fliterFuncBehindUp(line):
    if (line.strip().find(r"ProcessColiLoop : Coli loop up, ignore. Similarity =") >= 0):
        return True
    else:
        return False

def processFuncBehindUp(line):
    outLine = ""
    m = re.findall(r"(.*) --- ProcessColiLoop : Coli loop up, ignore. Similarity = (.*)", line)
    if (len(m) != 0):
        outLine = "%s --- behind up sim = %s\n" % m[0]
        sim_list.append(m[0])
    else:
        outLine = "something error in %s\n" % line
    return outLine 

def fliterFuncBehindDown(line):
    if (line.strip().find(r"ProcessColiLoop : Similarity Test Result =") >= 0):
        return True
    else:
        return False

def processFuncBehindDown(line):
    outLine = ""
    m = re.findall(r"(.*) --- ProcessColiLoop : Similarity Test Result = (.*)", line)
    #print m
    if (len(m) != 0):
        outLine = "%s --- behind down sim = %s\n" % m[0]
        sim_list.append(m[0])
    else:
        outLine = "something error in %s\n" % line
    return outLine


#开始进行应用
in_file = "2017_07_07_imgCtrl_new.log"
f_read = open(in_file, 'r')
f_write = open("temp.log", 'w')

simParser = LogParser()
simParser.setOutput(f_write)

#用于生成excel的列表
sim_list = []
#title = ("时间", "后线圈上升沿抓拍和上一辆车上升沿抓拍相似度")
#title = ("时间", "后线圈下降沿抓拍和上升沿抓拍相似度")
title = ("时间", "车头相似度")
sim_list.append(title);

#simParser.setTargetStamp(fliterFuncBehindUp, processFuncBehindUp)
#simParser.setTargetStamp(fliterFuncBehindDown, processFuncBehindDown)
simParser.setTargetStamp(fliterFuncFront, processFuncFront)

#开始逐行输入文本

lines = f_read.readlines()
for line in lines:
    simParser.startParse(line)

f_result = open("log_parse.txt", "w");
for item in sim_list:
	f_result.write("%s\t%s\n" % item);
	
f_read.close()
f_write.close()
f_result.close()

#list2Excel(sim_list)


