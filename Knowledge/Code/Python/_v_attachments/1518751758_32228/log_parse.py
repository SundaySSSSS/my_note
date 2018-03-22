# -*- coding: gb2312 -*-

import re, sys

#使用方法:
#本类可以用于在大量文本中筛选想要的文本, 并输出到流中
#本类支持两种模式,
#   1, 逐行寻找目标行, 并处理
#   2, 在某个范围内寻找目标行, 并处理
#   使用步骤:
#       1): 生成对象
#       2): 调用setOutput设置输出流
#       3): 调用setStartStamp和setEndStamp设置开始结束标记(如果两个都调用了则对应模式2, 否则对应模式1)
#       4): 调用setTargetStamp方法设置目标行的判定方法(filterFunc)和找到目标行后的处理方案, 可以设置多个
#       5): 调用startParse进行解析
class LogParser:
    __startStamp = ""
    __endStamp = ""
    fp_out = None
    targetList = []
    isFindInScale = 0   #是否在某个范围内进行查找
    isStarted = 0       #是否已经开始进行解析, 开始解析后不再允许进行配置
    #设置要处理块的起始标记
    def setStartStamp(self, stamp):
        __startStamp = stamp
    #设置要处理块的结束标记
    def setEndStamp(self, stamp):
        __endStamp = stamp
    #设置要处理行的标记和处理方法
    #filterFunc要求有一个参数, 为待检测文本中的一行, 有一个返回值, 如果为目标行, 返回True, 否则返回False
    #processFunc要求有一个参数, 为通过filterFunc判定为目标的一行字符串, 有一个返回值, 为经过处理后的一行内容
    def setTargetStamp(self, fliterFunc, processFunc):
        tempList = [fliterFunc, processFunc]
        self.targetList.append(tempList)
    def setOutput(self, file):
        self.fp_out = file
    def startParse(self, inLine):
        outLine = ""
        
        if self.isStarted == 0:
            self.isStarted = 1
        #逐条检测目标
        for item in self.targetList:
            fliter = item[0]
            process = item[1]
            if fliter(inLine) == True:
                outLine = process(inLine)
                self.fp_out.write(outLine);
                break   #只要有一个匹配就跳出
        
    def help(self):
        pass
    
    
    
    
