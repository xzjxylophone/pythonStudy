#!/usr/bin/python
# coding=utf-8


# 题目：两个乒乓球队进行比赛，各出三人。
# 甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。
# a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。



x = ord('x')
z = ord('z')

for a in range(x, z + 1):
    for b in range(x, z + 1):
        if a!= b:
            for c in range(x, z + 1):
                if (a != c) and (b != c):
                    if (a != x) and (c != x) and (c != z):
                        print "order is a VS %s, b VS %s, c VS %s" %(chr(a), chr(b), chr(c))





