# -*- coding: gb2312 -*-

import win32com.client as win32
from time import sleep
#����ĸ�ʽҪ��:
#data_list��ÿһ����Ա����Ԫ��, ����[("����", "100"), ("����", "90")]
def list2Excel(data_list):
    #create excel
    app = 'Excel'
    xl = win32.gencache.EnsureDispatch('%s.Application' % app)
    ss = xl.Workbooks.Add()
    sh = ss.ActiveSheet
    xl.Visible = True

    sleep(1)

    #��ȡ����
    col_num = len(data_list[0])
    for i in range(col_num):
        sh.Cells(1,i + 1).Interior.ColorIndex = 4   #����ɫ����Ϊ��ɫ
    #put data_list to excel
    raw_num = 1
    for item in data_list:
        for i in range(len(item)):
            sh.Cells(raw_num,i + 1).Value = item[i]
        raw_num = raw_num + 1


#test_list = [("����", "100"), ("����", "90")]
