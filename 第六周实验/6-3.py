#!/usr/bin/env python3
# -*- coding=utf-8 -*-

#创建一个基础类，类名为Person
class Person:
#创建类初始化方法，定义基础属性
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

#创建类里面的方法，方法名为personinfo，用于打印基础属性
    def personinfo(self):
        print('*'*30)
        print('{0:<10}{1:<10}'.format('姓名：',self.name))
        print('{0:<10}{1:<10}'.format('年龄：',self.age))
        print('{0:<10}{1:<10}'.format('性别：',self.sex))

#创建一个子类，类名为Student，继承父类Person
class Student(Person):
#创建子类初始化方法，定义基础属性
    def __init__(self,name,age,sex,college,classr):
        Person.__init__(self,name,age,sex)
        self.college = college
        self.classr = classr

#创建子类方法，方法名为study
    def study(self,teacher):
        print('老师，%s我终于学会了' % teacher)

#重写父类personinfo方法
    def personinfo(self):
         Person.personinfo(self)
         print('{0:<8}{1:<10}'.format('所属学院：',self.college))
         print('{0:<8}{1:<10}'.format('所属班级：',self.classr))

#创建一个子类，类名为Teacher，继承父类Person
class Teacher(Person):
#创建子类初始化方法，定义基础属性
    def __init__(self,name,age,sex,college,professional):
        Person.__init__(self,name,age,sex)
        self.college = college
        self.professional = professional

#创建子类一个方法，方法名为teachObj，返回一个信息
    def teachObj(self):
        return '用面向对象设计程序'

#重写父类personinfo方法
    def personinfo(self):
         Person.personinfo(self)
         print('{0:<8}{1:<10}'.format('所属学院：',self.college))
         print('{0:<8}{1:<10}'.format('专业信息：',self.professional))

stu1 = Student('Rong Huan',41,'男','广州大学','大一4班')
teacher = Teacher('Li Jian',39,'Male','广州大学','Python')
stu1.personinfo()
stu1.study(teacher.teachObj())
teacher.personinfo()

