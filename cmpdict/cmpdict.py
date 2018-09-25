# !/usr/bin/env python
# -*- coding: utf-8 -*-

sysNo = open("实际号码.txt")
sysMon = open("实际应缴费用.txt")
actNo = open("系统号码.txt")
actMon = open("系统应缴费用.txt")
sys_dict = {}
act_dict = {}

# sys_dict 读取数据并保存为list
sysNo_ls = [no.replace("\n", "") for no in sysNo.readlines()]
sysMon_ls = [mon.replace("\n", "") for mon in sysMon.readlines()]
# 将数据构造为字典
sys_dict = dict(zip(sysNo_ls, sysMon_ls))

# act_dict 读取数据并保存为list
actNo_ls = [no.replace("\n", "") for no in actNo.readlines()]
actMon_ls = [mon.replace("\n", "") for mon in actMon.readlines()]
# 将数据构造为字典
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
