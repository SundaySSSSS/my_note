# -*- coding: gb2312 -*-

import re, sys

#ʹ�÷���:
#������������ڴ����ı���ɸѡ��Ҫ���ı�, �����������
#����֧������ģʽ,
#   1, ����Ѱ��Ŀ����, ������
#   2, ��ĳ����Χ��Ѱ��Ŀ����, ������
#   ʹ�ò���:
#       1): ���ɶ���
#       2): ����setOutput���������
#       3): ����setStartStamp��setEndStamp���ÿ�ʼ�������(������������������Ӧģʽ2, �����Ӧģʽ1)
#       4): ����setTargetStamp��������Ŀ���е��ж�����(filterFunc)���ҵ�Ŀ���к�Ĵ�����, �������ö��
#       5): ����startParse���н���
class LogParser:
    __startStamp = ""
    __endStamp = ""
    fp_out = None
    targetList = []
    isFindInScale = 0   #�Ƿ���ĳ����Χ�ڽ��в���
    isStarted = 0       #�Ƿ��Ѿ���ʼ���н���, ��ʼ�������������������
    #����Ҫ��������ʼ���
    def setStartStamp(self, stamp):
        __startStamp = stamp
    #����Ҫ�����Ľ������
    def setEndStamp(self, stamp):
        __endStamp = stamp
    #����Ҫ�����еı�Ǻʹ�����
    #filterFuncҪ����һ������, Ϊ������ı��е�һ��, ��һ������ֵ, ���ΪĿ����, ����True, ���򷵻�False
    #processFuncҪ����һ������, Ϊͨ��filterFunc�ж�ΪĿ���һ���ַ���, ��һ������ֵ, Ϊ����������һ������
    def setTargetStamp(self, fliterFunc, processFunc):
        tempList = [fliterFunc, processFunc]
        self.targetList.append(tempList)
    def setOutput(self, file):
        self.fp_out = file
    def startParse(self, inLine):
        outLine = ""
        
        if self.isStarted == 0:
            self.isStarted = 1
        #�������Ŀ��
        for item in self.targetList:
            fliter = item[0]
            process = item[1]
            if fliter(inLine) == True:
                outLine = process(inLine)
                self.fp_out.write(outLine);
                break   #ֻҪ��һ��ƥ�������
        
    def help(self):
        pass
    
    
    
    
