#!/usr/bin/python
# coding=utf-8

import sys

print "file script name:", sys.argv[0]
for i in range(1, len(sys.argv)):
    print "param index:", i, " param value:", sys.argv[i]

# 1 表示是从tx_dev更换成tx_test
# 2 表示是从tx_test更换成tx_dev
# 传参
type = sys.argv[1]
print "type:", type

# 这里只能用字符串1,不能用数字1
if type == "1":
    oldText = "tx_dev"
    newText = "tx_test"
else:
    oldText = "tx_test"
    newText = "tx_dev"

print "oldText:", oldText, " newText:", newText

webType = ["verified", "manage", "train"]
fileNamePrefix = "/Users/ceshi/Documents/svn/yyzc_kzh/P002_AIWMWEBSITE/Trunk/Code/aiwm-parent/aiwm-"
fileNameSuffix = "-web/src/main/resources/config/application-database.properties"

for i in range(0, len(webType)):
    fileName = fileNamePrefix + webType[i] + fileNameSuffix
    print "fileName:", fileName
    with open(fileName, "r") as f:
        lines = f.readlines()

    with open(fileName, "w") as f_w:
        for line in lines:
            line = line.replace(oldText, newText)
            f_w.write(line)



