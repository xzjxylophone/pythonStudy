#!/usr/bin/python
#coding=utf-8



# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？




def calculateReward(profit):
	values = [1000000, 600000, 400000, 200000, 100000, 0]
	rats = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
	results = []
	length = len(values)
	tmpProfit = profit
	for idx in range(0, length):
		tmpValue = values[idx]
		tmpRat = rats[idx]
		if (tmpProfit > tmpValue):
			remain = tmpProfit - tmpValue
			tmpResult = remain * tmpRat
			results.append(tmpResult)
			tmpProfit = tmpValue
		else:
			continue



	result = 0
	for tmpResult in results:
		print "tmpResult: ", tmpResult
		result += tmpResult
	return result


# profit = int(raw_input('净利润:'))
# result = calculateReward(profit)
# print result

result = calculateReward(1000)
print "result: ", result

result = calculateReward(100000 + 1000)
print "result: ", result

result = calculateReward(200000 + 1000)
print "result: ", result

result = calculateReward(400000 + 1000)
print "result: ", result

result = calculateReward(600000 + 1000)
print "result: ", result

result = calculateReward(1000000 + 1000)
print "result: ", result







































