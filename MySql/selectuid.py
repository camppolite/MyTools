# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql.cursors

# 连接MySQL数据库
connection = pymysql.connect(host='192.168.3.30', port=3306, user='root', password='123456', db='teacher',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

# 通过cursor创建游标
cursor = connection.cursor()

# 查询数据库多条数据
# result = cursor.fetchall()
# for data in result:
#     print(data)

# # 提交SQL
# connection.commit()

uid = open("name+uid.txt", 'w')

for i in range(1,103):
    for j in range(0,99):
        if j == 0:
            name = "'Ten-thousand{0}'".format(i)
        else:
            name = "'Ten-thousand{0}_{1}'".format(i, j)
        # 创建sql 语句，并执行
        uidsql = "SELECT varuuid FROM proj20180727_new_version_proj_variable WHERE varname={};\n".format(name)
        cursor.execute(uidsql)
        # 查询数据库单条数据
        result = cursor.fetchone()
        uid.write(name + ':' + result['varuuid'] + '\n')

# 关闭数据连接
connection.close()

uid.close()
