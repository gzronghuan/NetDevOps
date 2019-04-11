#!/usr/bin/env python3
# -*- coding=utf-8 -*-

def strings(str):
    alp_num = 0
    dig_num = 0
    spa_num = 0
    oth_num = 0
    for i in range(0,len(str)):
        #判断字符
        if str[i].isalpha():
            alp_num += 1
        #判断数字
        elif str[i].isdigit():
            dig_num += 1
        #判断空格
        elif str[i].isspace():
            spa_num += 1
        #其他
        else: oth_num +=1

    print ("字母总数为：",alp_num)
    print ("数字总数为：",dig_num)
    print ("空格总数为：",spa_num)
    print ("其他总数为：",oth_num)

str = input('请输入字符串：')
strings(str)
