#!/usr/bin/python
# coding=utf-8


# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。


def getLeve(number):
    if (number >= 90):
        return "A"
    if (number <= 89 and number >= 60):
        return "B"
    if (number < 60 and number >= 0):
        return "C"
    return "data error"

level = getLeve(99)
print "level: ", level

level = getLeve(88)
print "level: ", level

level = getLeve(56)
print "level: ", level

level = getLeve(-1)
print "level: ", level
