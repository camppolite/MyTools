# !/usr/bin/env python
# -*- coding: utf-8 -*-

sysNo = open("实际号码.txt")
sysMon = open("实际应缴费用.txt")
actNo = open("系统号码.txt")
actMon = open("系统应缴费用.txt")
sys_dict = {}
act_dict = {}

# sys_dict
sysNo_ls = []
sysMon_ls = []
# 读取数据并保存为list
for no in sysNo.readlines():
    sysNo_ls.append(no.replace("\n", ""))
for mon in sysMon.readlines():
    sysMon_ls.append(mon.replace("\n", ""))
# 将数据构造为字典
# for i in range(len(sysNo_ls)):
#     sys_dict[sysNo_ls[i]] = sysMon_ls[i]
sys_dict = dict(zip(sysNo_ls, sysMon_ls))
# act_dict
actNo_ls = []
actMon_ls = []
# 读取数据并保存为list
for no in actNo.readlines():
    actNo_ls.append(no.replace("\n", ""))
for mon in actMon.readlines():
    actMon_ls.append(mon.replace("\n", ""))
# 将数据构造为字典
# for i in range(len(actNo_ls)):
#     act_dict[actNo_ls[i]] = actMon_ls[i]
act_dict = dict(zip(actNo_ls, actMon_ls))

# 实际缴费名单不在系统名单内
print("实际缴费名单不在系统名单内的号码：")
for key in act_dict:
    if key in sys_dict:
        if act_dict[key] != sys_dict[key]:
            print("!!!!!%s%s%s" % (key, act_dict[key], sys_dict[key]))
    if key not in sys_dict:
        print(key)

# 系统名单不在实际缴费名单内
print("系统名单不在实际缴费名单内的号码：")
for key in sys_dict:
    if key in act_dict:
        if act_dict[key] != sys_dict[key]:
            print("!!!!!%s%s%s" % (key, act_dict[key], sys_dict[key]))
    if key not in act_dict:
        print(key)

sysNo.close()
sysMon.close()
actNo.close()
actMon.close()
