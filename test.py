#!/usr/bin/python
#coding=utf-8


# 中文乱码的问题
# 以上出错信息显示了我们为指定编码，解决方法为只要在文件开头加入 # -*- coding: UTF-8 -*- 或者 #coding=utf-8 就行了。

import os


money = 2000

def addMoney():
    global money
    money = money + 1

def main():
    print 'Hello World!'
    print "This is Alice\'的问候"
    print 'This is Bob\'的问候'
    foo(42, 24)
    print '=' * 10
    print '这将直接执行' + os.getcwd();

    counter = 0
    counter += 1
    food = ['苹果', '杏子', '李子', '梨']
    for i in food:
        print '我就爱整只' + i

    print '数到10'

    dict = {'name': 'xzj', 'age': 30}
    dict.keys()

    print money
    addMoney()
    print money


    for i in range(10):
        print i



def foo(param1, secondParam):
    res = param1 + secondParam
    print '%s 加 %s 等于 %s'%(param1, secondParam, res)
    if res < 50:
        print 'lesser than 50'
    elif (res >= 50) and ((param1 == 42) or (secondParam == 24)):
        print 'greater than 50 and value = 42'
    else:
        print 'greater than 50'

        '''这是多
        行注释........'''

    abc = '''kkkkkksklgkslgjsg'''

    print abc;

if __name__ == '__main__':
        main()








