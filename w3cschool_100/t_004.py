#!/usr/bin/python
#coding=utf-8


def calculateNumber(year, month, day):
    if year < 0:
        print "year data error"
        return 0

    if month <= 0 or month > 12:
        print "month data error"
        return 0

    leap = 0
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = 1

    days = (31, 28 + leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    maxDay = days[month - 1];
    if day > maxDay:
        print "day data error"
        return 0

    result = 0
    for i in range(0, month - 1):
        result += days[i]

    result += day

    return result;



# year = int(raw_input('year:\n'))
# month = int(raw_input('month:\n'))
# day = int(raw_input('day:\n'))

year = 2015
month = 6
day = 7
result = calculateNumber(year, month, day)

print 'it is the %dth day.' %result





