#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from xml.dom.minidom import Document
from Source_DB import *

doc = Document()
root = doc.createElement('root')
doc.appendChild(root)

i = 1
phone ={}
for p_dict in phone_dict:
    phone[i] = p_dict
#    print ('手机' + str(i),phone[i])
    prod_name = doc.createElement('产品')
    prod_name.setAttribute('name','手机' + str(i))
    root.appendChild(prod_name)
    for key in phone[i]:
#        print (phone[i][key])
        phone_name = doc.createElement(key)
        phone_name.setAttribute('name',phone[i][key])
        prod_name.appendChild(phone_name)
    i += 1

XML_File = open('XML_Phone.xml', 'w',  encoding='utf-8')
XML_File.write(doc.toprettyxml(indent='    '))
XML_File.close()