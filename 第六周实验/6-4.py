#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from xml.dom.minidom import Document

phone_dict=[{'品牌':'苹果','型号':'iphoneX','价格':'9599'},{'品牌':'华为','型号':'mate20pro','价格':'6888'},{'品牌':'小米','型号':'mi8','价格':'2899'},{'品牌':'三星','型号':'S10+','价格':'8699'}]
#print (phone_dict[0])

doc = Document()
root = doc.createElement('root')
doc.appendChild(root)

for phone_name in phone_dict:
    name = doc.createElement('品牌')
    name.setAttribute('name',phone_name)
    print (phone_name)
    root.appendChild(name)

XML_File = open('XML_Phone.xml', 'w',  encoding='utf-8')
XML_File.write(doc.toprettyxml(indent='    '))
XML_File.close()