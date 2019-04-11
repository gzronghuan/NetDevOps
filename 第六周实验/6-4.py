#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from xml.dom.minidom import Document

phone_dict=[{'品牌':'苹果','型号':'iphoneX','价格':'9599'},{'品牌':'华为','型号':'mate20pro','价格':'6888'},{'品牌':'小米','型号':'mi8','价格':'2899'},{'品牌':'三星','型号':'S10+','价格':'8699'}]
#phone_dict={'手机':{'品牌':'苹果','型号':'iphoneX','价格':'9599'}}
#print (phone_dict[0])

doc = Document()
root = doc.createElement('root')
doc.appendChild(root)

# type_name = doc.createElement('类别')
# type_name.setAttribute('name','手机')
#
# root.appendChild(type_name)

############################################################
#列表测试环境
i = 1
# for phone_name in phone_dict:
#     phone = {'手机' + str(i+1) + '':phone_name}
#     i += 1
#
# print (phone)
#print (phone_dict[0])
#for i in range(0,3):
phone ={}
for p_dict in phone_dict:
#    phone_name = phone_dict[i]
#  dict[i] = {'手机': phone_name}
# name = doc.createElement('类别')
# name.setAttribute('name',phone_dict)
# print (type(phone_dict))
#    print (phone_name)
#    print (len(phone_dict))
    phone[i] = p_dict
    print ('手机' + str(i),phone[i])
    for key in phone[i]:
        print (phone[i][key])
#     for phone_name in phone[i]:
# #        for j in range(1,len(p_dict)):
        name = doc.createElement(key)
        name.setAttribute('name',phone[i][key])
#         model = doc.createElement('型号')
#         model.setAttribute('name',phone_name)
#         price = doc.createElement('价格')
#         price.setAttribute('name',phone_name)
#         print (len(p_dict))
        root.appendChild(name)
#         root.appendChild(model)
#         root.appendChild(price)
    i += 1

# root.appendChild(name)



#     name = doc.createElement('型号')
#     name.setAttribute('name',phone_name)
# #    print (phone_name)
#     type_name.appendChild(name)

XML_File = open('XML_Phone.xml', 'w',  encoding='utf-8')
XML_File.write(doc.toprettyxml(indent='    '))
XML_File.close()