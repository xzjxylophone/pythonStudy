#!/usr/bin/python
# coding=utf-8



# 题目:有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？




'''
for i in range(1, 5):
	for j in range(1, 5):
		for k in range(1, 5):
			if (i != j) and (i != k) and (j != k):
				print i,j,k
'''


# scope = [1, 2, 3]
scope = [1, 2, 3, 4]
result = []

for i in scope:
	for j in scope:
		for k in scope:
			if (i != j) and (i != k) and (j != k):
				tmpResult = str(i) + str(j) + str(k)
				result.append(tmpResult)

for tmp in result:
	print tmp







