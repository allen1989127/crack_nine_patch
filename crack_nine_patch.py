#!/usr/bin/env python2
# -*-coding: utf-8 -*-

import itertools
import hashlib
import time
import os

f = open('gesture.key', 'r')        #将/data/system/gestrue.key文件pull出来，并拷贝到脚本目录下
pswd = f.readline()                 #读取加密文件内容
pswd_hex = pswd.encode('hex')       #转换为十六进制数据
print '加密密码为: %s' % pswd_hex

matrix = []
for i in range(0, 9):               #将00,01,02,03,04,05,06,07,08对应的点放置到列表中
    str_temp = '0' + str(i)
    matrix.append(str_temp)

min_num = 4
max_num = len(matrix)

for num in range(min_num, max_num + 1):           #最小连接点数为4, 最大为9
    iter1 = itertools.permutations(matrix, num)   #在列表中取出num个数进行全排列
    list_m = (list(iter1))

    found = False
    for el in list_m:
        strlist = ''.join(el)
        strlist_sha1 = hashlib.sha1(strlist.decode('hex')).hexdigest()   #对全排列的数据进行sha1的计算，并与加密数据进行对比
        if pswd_hex == strlist_sha1:
            print '解密密码为:', strlist
            found = True
            break

    if found :
        break
