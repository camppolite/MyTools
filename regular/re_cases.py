#_*_ coding:utf-8 _*_
import re
from xlwt import *
f = open("D:/PycharmProjects/meiyoukongge.txt", "r")
meiyoukongge = f.read().strip().replace('\t','')
# print(txt)
#用例名称
caseName = re.findall("测试用例名称(.*)用例标识", meiyoukongge)
# print(caseName)
print(len(caseName))
#用例标识
caseSymblic = re.findall("用例标识(.*)", meiyoukongge)
# print(caseSymblic)
print(len(caseSymblic))
#先决条件
tiaojian = re.findall("前提和约束(.*)", meiyoukongge)
# print(tiaojian)
print(len(tiaojian))
#用例综述
casedecrip = re.findall("测试用例综述(.*)", meiyoukongge)
# print(casedecrip)
print(len(casedecrip))
#通过准则
casepass = re.findall("通过准则(.*)", meiyoukongge)
# print(casepass)
print(len(casepass))

# print(txt)
f.close()

file = open("D:/PycharmProjects/myword.txt", "r")
myword = file.read()
#输入及操作
someinput = re.findall("期望结果\s(.+)", myword)
# print(someinput)
# print(myword)
file.close()
# p =open("D:/PycharmProjects/test11.txt", "w")
# retxt = re.findall("\S", txt)
# p.write(str(myword))
# print(retxt)
# p.close()
mydata = []
for i in range(len(caseName)):
    print(i)
    tempList = []
    tempList.append(caseName[i])
    tempList.append(caseSymblic[i])
    tempList.append(tiaojian[i])
    tempList.append(casedecrip[i])
    tempList.append(casepass[i])
    mydata.append(tempList)

print(mydata)
# 需要xlwt库的支持
# import xlwt
file = Workbook(encoding='utf-8')
# 指定file以utf-8的格式打开
table = file.add_sheet('data')
# 指定打开的文件名

data = {
    "1": ["张三", 150, 120, 100],
    "2": ["李四", 90, 99, 95],
    "3": ["王五", 60, 66, 68]
}
# 字典数据

ldata = []
num = [a for a in data]
print(num)
# for循环指定取出key值存入num中
num.sort()
# 字典数据取出后无需，需要先排序

for x in num:
    # for循环将data字典中的键和值分批的保存在ldata中
    t = [int(x)]
    for a in data[x]:
        t.append(a)
    ldata.append(t)
print(ldata)
for i, p in enumerate(mydata):
    # 将数据写入文件,i是enumerate()函数返回的序号数
    for j, q in enumerate(p):
        # print i,j,q
        table.write(i, j, q)
file.save('data.xls')