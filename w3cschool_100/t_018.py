#!/usr/bin/python
# coding=utf-8

# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。


def calculate(number, len):
    if (number <= 0 or number > 9):
        print "data error"
        return

    result = 0
    for i in range(0, len):
        numberLen = i + 1
        # 具体的第几位数字
        for j in range(0, numberLen):
            result += (number * (10 ** j))

    print "result :", result


calculate(1, 3)
calculate(1, 4)

