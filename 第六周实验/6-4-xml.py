#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from xml.dom.minidom import Document

phone_dict=[{'品牌':'苹果','型号':'iphoneX','价格':'9599'},{'品牌':'华为','型号':'mate20pro','价格':'6888'},\
            {'品牌':'小米','型号':'mi8','价格':'2899'},{'品牌':'三星','型号':'S10+','价格':'8699'}]

doc = Document()
root = doc.createElement('root')
doc.appendChild(root)

i = 1
phone ={}
for p_dict in phone_dict:
    phone[i] = p_dict
#    print ('手机' + str(i),phone[i])
    for key in phone[i]:
#        print (phone[i][key])
        name = doc.createElement(key)
        name.setAttribute('name',phone[i][key])
        root.appendChild(name)
    i += 1

XML_File = open('XML_Phone.xml', 'w',  encoding='utf-8')
XML_File.write(doc.toprettyxml(indent='    '))
XML_File.close()