# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql.cursors


def sqlvar():
    """通过sql语句插入数据库变量"""
    data = {
        'table_name': "`teacher`.`wdr3000modbusio_variable`",
        'varname': "",
        'vargroup': repr('fun03'),
        'varisRead': 1,
        'varisWrite': 1,
        'varisRecord': 1,
        'varDataType': repr('int'),
        'varvalue': repr(''),
        'varvalueInit': repr('0'),
        'varmin': repr(''),
        'varmax': repr(''),
        'varisSaveValueInit': 1,
        'varformula': repr(''),
        'varformatString': repr(''),
        'varunit': repr(''),
        'vardescribe': repr(''),
        'varuuid': repr('2079341082'),
        'varType': repr('1'),
        'varBoundSource': repr('')
    }

    insertsql = open("insertsql.txt", 'w')

    for i in range(1, 3001):
        # 创建sql 语句
        data['varname'] = repr("fun03x%s") % (i)
        data['varuuid'] = repr("207934108%s") % (i)
        sql = "INSERT INTO {table_name} (`varname`, `vargroup`, `varisRead`, `varisWrite`, `varisRecord`, " \
              "`varDataType`, `varvalue`, `varvalueInit`, `varmin`, `varmax`, `varisSaveValueInit`," \
              " `varformula`, `varformatString`, `varunit`, `vardescribe`, `varuuid`, `varType`, " \
              "`varBoundSource`) VALUES ({varname}, {vargroup}, {varisRead}, {varisWrite}, {varisRecord}, " \
              "{varDataType}, {varvalue}, {varvalueInit}, {varmin}, {varmax}, {varisSaveValueInit}, " \
              "{varformula}, {varformatString}, {varunit}, {vardescribe}, {varuuid}, {varType}, {varBoundSource});"\
            .format(table_name=data['table_name'],
                    varname=data['varname'],
                    vargroup=data['vargroup'],
                    varisRead=data['varisRead'],
                    varisWrite=data['varisWrite'],
                    varisRecord=data['varisRecord'],
                    varDataType=data['varDataType'],
                    varvalue=data['varvalue'],
                    varvalueInit=data['varvalueInit'],
                    varmin=data['varmin'],
                    varmax=data['varmax'],
                    varisSaveValueInit=data['varisSaveValueInit'],
                    varformula=data['varformula'],
                    varformatString=data['varformatString'],
                    varunit=data['varunit'],
                    vardescribe=data['vardescribe'],
                    varuuid=data['varuuid'],
                    varType=data['varType'],
                    varBoundSource=data['varBoundSource'])
        print(sql)
        insertsql.write(sql + "\n")

    insertsql.close()


def sqlvarfortcp():
    """通过sql语句插入数据库变量"""
    data = {
        'table_name': "`teacher`.`project_variable`",
        'varname': "",
        'vargroup': repr('tcpvar'),
        'varisRead': 1,
        'varisWrite': 1,
        'varisRecord': 1,
        'varDataType': repr('int'),
        'varvalue': repr(''),
        'varvalueInit': repr('0'),
        'varmin': repr(''),
        'varmax': repr(''),
        'varisSaveValueInit': 1,
        'varformula': repr(''),
        'varformatString': repr(''),
        'varunit': repr(''),
        'vardescribe': repr(''),
        'varuuid': repr('2079341082'),
        'varType': repr('1'),
        'varBoundSource': repr('')
    }

    insertsql = open("insertsqlfortcp.txt", 'w')

    for i in range(1, 1251):
        for j in ["01", "02", "03", "04", "05", "06", "15", "16"]:
            # 创建sql 语句
            data['varname'] = repr("fun%sx%s") % (j, i)
            data['varuuid'] = repr("2079341082%s%s") % (j, i)
            sql = "INSERT INTO {table_name} (`varname`, `vargroup`, `varisRead`, `varisWrite`, `varisRecord`, " \
                  "`varDataType`, `varvalue`, `varvalueInit`, `varmin`, `varmax`, `varisSaveValueInit`," \
                  " `varformula`, `varformatString`, `varunit`, `vardescribe`, `varuuid`, `varType`, " \
                  "`varBoundSource`) VALUES ({varname}, {vargroup}, {varisRead}, {varisWrite}, {varisRecord}, " \
                  "{varDataType}, {varvalue}, {varvalueInit}, {varmin}, {varmax}, {varisSaveValueInit}, " \
                  "{varformula}, {varformatString}, {varunit}, {vardescribe}, {varuuid}, {varType}, {varBoundSource});"\
                .format(table_name=data['table_name'],
                        varname=data['varname'],
                        vargroup=data['vargroup'],
                        varisRead=data['varisRead'],
                        varisWrite=data['varisWrite'],
                        varisRecord=data['varisRecord'],
                        varDataType=data['varDataType'],
                        varvalue=data['varvalue'],
                        varvalueInit=data['varvalueInit'],
                        varmin=data['varmin'],
                        varmax=data['varmax'],
                        varisSaveValueInit=data['varisSaveValueInit'],
                        varformula=data['varformula'],
                        varformatString=data['varformatString'],
                        varunit=data['varunit'],
                        vardescribe=data['vardescribe'],
                        varuuid=data['varuuid'],
                        varType=data['varType'],
                        varBoundSource=data['varBoundSource'])
            print(sql)
            insertsql.write(sql + "\n")

    insertsql.close()


def modbusfun05():
    """通过sql语句插入TCP功能码为05的变量"""
    data = {
        'table_name': "`teacher`.`project_iovariable_modbus`",
        'groupid': 39,
        'name': "",
        'slaveid': repr('1'),
        'function': repr('5'),
        'startaddress': repr('0'),
        'datatype': repr('bool'),
        'variable': repr(''),
        'variableid': repr(''),
        'mode': 2,
        'devicename': repr('modbus/tcp_test1'),
        'deviceid': repr('{00eb8e82-c5fd-488d-b475-4715df3b3aed}'),
        'period': 1000,
    }

    insertsql = open("insertsqltcp05.txt", 'w')

    for i in range(1, 1251):
        # 创建sql 语句
        data['name'] = repr("fun05x%s") % i
        sql = "INSERT INTO {table_name} (`groupid`, `name`, `slaveid`, `function`, `startaddress`, " \
              "`datatype`, `variable`, `variableid`, `mode`, `devicename`, `deviceid`," \
              " `period`) VALUES ({groupid}, {name}, {slaveid}, {function}, {startaddress}, " \
              "{datatype}, {variable}, {variableid}, {mode}, {devicename}, {deviceid}, " \
              "{period});"\
            .format(table_name=data['table_name'],
                    groupid=data['groupid'],
                    name=data['name'],
                    slaveid=data['slaveid'],
                    function=data['function'],
                    startaddress=data['startaddress'],
                    datatype=data['datatype'],
                    variable=data['variable'],
                    variableid=data['variableid'],
                    mode=data['mode'],
                    devicename=data['devicename'],
                    deviceid=data['deviceid'],
                    period=data['period'])
        print(sql)
        insertsql.write(sql + "\n")

    insertsql.close()


def modbusfun06():
    """通过sql语句插入TCP功能码为06的变量"""
    data = {
        'table_name': "`teacher`.`project_iovariable_modbus`",
        'groupid': 40,
        'name': "",
        'slaveid': repr('1'),
        'function': repr('6'),
        'startaddress': repr('0'),
        'datatype': repr('short'),
        'variable': repr(''),
        'variableid': repr(''),
        'mode': 2,
        'devicename': repr('modbus/tcp_test1'),
        'deviceid': repr('{00eb8e82-c5fd-488d-b475-4715df3b3aed}'),
        'period': 1000,
    }

    insertsql = open("insertsqltcp06.txt", 'w')

    for i in range(1, 1251):
        # 创建sql 语句
        data['name'] = repr("fun06x%s") % i
        sql = "INSERT INTO {table_name} (`groupid`, `name`, `slaveid`, `function`, `startaddress`, " \
              "`datatype`, `variable`, `variableid`, `mode`, `devicename`, `deviceid`," \
              " `period`) VALUES ({groupid}, {name}, {slaveid}, {function}, {startaddress}, " \
              "{datatype}, {variable}, {variableid}, {mode}, {devicename}, {deviceid}, " \
              "{period});"\
            .format(table_name=data['table_name'],
                    groupid=data['groupid'],
                    name=data['name'],
                    slaveid=data['slaveid'],
                    function=data['function'],
                    startaddress=data['startaddress'],
                    datatype=data['datatype'],
                    variable=data['variable'],
                    variableid=data['variableid'],
                    mode=data['mode'],
                    devicename=data['devicename'],
                    deviceid=data['deviceid'],
                    period=data['period'])
        print(sql)
        insertsql.write(sql + "\n")

    insertsql.close()


def bindQVartoTVar01():
    """将数据库变量与TCP功能码为01的变量绑定"""
    data = {
            'table_name': "`teacher`.`project_iovariable_modbus`",
            'name': "",
            'variable': repr(''),
            'variableid': repr('')
        }

    insertsql = open("bindSVartoTVar01.txt", 'w')

    connection = pymysql.connect(host="192.168.3.30",
                           port=3306,
                           user="root",
                           password="123456",
                           db="teacher",
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

    for i in range(1, 1251):
        # 创建sql 语句
        data['name'] = repr("fun01x%s") % i

        with connection.cursor() as cursor:
            # Create a new record
            selectSQL = "SELECT varname, varuuid FROM `project_variable` WHERE `varname` = {name};".format(name=data['name'])
            cursor.execute(selectSQL)
            result = cursor.fetchone()
            print(result)
            data['variable'] = result['varname']
            data['variableid'] = result['varuuid']

        data['name'] = repr("fun01_%s") % (i-1)
        sql = "UPDATE {table_name} SET `variable`='{variable}', `variableid`='{variableid}' WHERE `name` = {name};"\
            .format(table_name=data['table_name'],
                    name=data['name'],
                    variable=data['variable'],
                    variableid=data['variableid'])
        print(sql)
        insertsql.write(sql + "\n")

    insertsql.close()


def bindQVartoTVar02():
    """将数据库变量与TCP功能码为02的变量绑定"""
    data = {
            'table_name': "`teacher`.`project_iovariable_modbus`",
            'name': "",
            'variable': repr(''),
            'variableid': repr('')
        }

    insertsql = open("bindSVartoTVar02.txt", 'w')

    connection = pymysql.connect(host="192.168.3.30",
                           port=3306,
                           user="root",
                           password="123456",
                           db="teacher",
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

    for i in range(1, 1251):
        # 创建sql 语句
        data['name'] = repr("fun02x%s") % i

        with connection.cursor() as cursor:
            # Create a new record
            selectSQL = "SELECT varname, varuuid FROM `project_variable` WHERE `varname` = {name};".format(name=data['name'])
            cursor.execute(selectSQL)
            result = cursor.fetchone()
            print(result)
            data['variable'] = result['varname']
            data['variableid'] = result['varuuid']

        data['name'] = repr("fun02_%s") % (i-1)
        sql = "UPDATE {table_name} SET `variable`='{variable}', `variableid`='{variableid}' WHERE `name` = {name};"\
            .format(table_name=data['table_name'],
                    name=data['name'],
                    variable=data['variable'],
                    variableid=data['variableid'])
        print(sql)
        insertsql.write(sql + "\n")

    insertsql.close()


def bindQVartoTVar03():
    """将数据库变量与TCP功能码为03的变量绑定"""
    data = {
            'table_name': "`teacher`.`wdr3000modbusio_iovariable_modbus`",
            'name': "",
            'variable': repr(''),
            'variableid': repr('')
        }

    insertsql = open("bindSVartoTVar03.txt", 'w')

    connection = pymysql.connect(host="192.168.3.30",
                                port=3306,
                                user="root",
                                password="123456",
                                db="teacher",
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    for i in range(0, 3000):
        # 创建sql 语句
        data['name'] = repr("fun03_%s") % i
        sqlvarname = repr("fun03x%s") % (i+1)

        with connection.cursor() as cursor:
            # Create a new record
            selectSQL = "SELECT varname, varuuid FROM `wdr3000modbusio_variable` WHERE `varname` = {name};".format(name=sqlvarname)
            cursor.execute(selectSQL)
            result = cursor.fetchone()
            print(result)
            data['variable'] = result['varname']
            data['variableid'] = result['varuuid']

        sql = "UPDATE {table_name} SET `variable`='{variable}', `variableid`='{variableid}' WHERE `id` = {name};"\
            .format(table_name=data['table_name'],
                    name=i+1,
                    variable=data['variable'],
                    variableid=data['variableid'])
        print(sql)
        insertsql.write(sql + "\n")

    insertsql.close()


def bindQVartoTVar03_bak():
    """将数据库变量与TCP功能码为03的变量绑定"""
    data = {
            'table_name': "`teacher`.`wdr3000modbusio_iovariable_modbus`",
            'name': "",
            'variable': repr(''),
            'variableid': repr('')
        }

    insertsql = open("bindSVartoTVar03.txt", 'w')

    connection = pymysql.connect(host="192.168.3.30",
                           port=3306,
                           user="root",
                           password="123456",
                           db="teacher",
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

    for i in range(1, 126):
        for j in range(1,11):
            # 创建sql 语句
            data['name'] = repr("fun03x%s") % (i+(j-1)*125)

            with connection.cursor() as cursor:
                # Create a new record
                selectSQL = "SELECT varname, varuuid FROM `project_variable` WHERE `varname` = {name};".format(name=data['name'])
                cursor.execute(selectSQL)
                result = cursor.fetchone()
                print(result)
                data['variable'] = result['varname']
                data['variableid'] = result['varuuid']
            if j == 1:
                data['name'] = repr("fun03_%s") % (i-1)
            else:
                data['name'] = repr("fun03_%s_%s") % (j, (i - 1))
            sql = "UPDATE {table_name} SET `variable`='{variable}', `variableid`='{variableid}' WHERE `name` = {name};"\
                .format(table_name=data['table_name'],
                        name=data['name'],
                        variable=data['variable'],
                        variableid=data['variableid'])
            print(sql)
            insertsql.write(sql + "\n")

    insertsql.close()


def bindQVartoTVar04():
    """将数据库变量与TCP功能码为04的变量绑定"""
    data = {
            'table_name': "`teacher`.`project_iovariable_modbus`",
            'name': "",
            'variable': repr(''),
            'variableid': repr('')
        }

    insertsql = open("bindSVartoTVar04.txt", 'w')

    connection = pymysql.connect(host="192.168.3.30",
                           port=3306,
                           user="root",
                           password="123456",
                           db="teacher",
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

    for i in range(1, 126):
        for j in range(1,11):
            # 创建sql 语句
            data['name'] = repr("fun04x%s") % i

            with connection.cursor() as cursor:
                # Create a new record
                selectSQL = "SELECT varname, varuuid FROM `project_variable` WHERE `varname` = {name};".format(name=data['name'])
                cursor.execute(selectSQL)
                result = cursor.fetchone()
                print(result)
                data['variable'] = result['varname']
                data['variableid'] = result['varuuid']

            data['name'] = repr("fun04_%s_%s") % (j, (i-1))
            sql = "UPDATE {table_name} SET `variable`='{variable}', `variableid`='{variableid}' WHERE `name` = {name};"\
                .format(table_name=data['table_name'],
                        name=data['name'],
                        variable=data['variable'],
                        variableid=data['variableid'])
            print(sql)
            insertsql.write(sql + "\n")

    insertsql.close()


def bindQVartoTVar015():
    """将数据库变量与TCP功能码为015的变量绑定"""
    data = {
            'table_name': "`teacher`.`project_iovariable_modbus`",
            'name': "",
            'variable': repr(''),
            'variableid': repr('')
        }

    insertsql = open("bindSVartoTVar015.txt", 'w')

    connection = pymysql.connect(host="192.168.3.30",
                           port=3306,
                           user="root",
                           password="123456",
                           db="teacher",
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

    for i in range(1, 1251):
        # 创建sql 语句
        data['name'] = repr("fun15x%s") % i

        with connection.cursor() as cursor:
            # Create a new record
            selectSQL = "SELECT varname, varuuid FROM `project_variable` WHERE `varname` = {name};".format(name=data['name'])
            cursor.execute(selectSQL)
            result = cursor.fetchone()
            print(result)
            data['variable'] = result['varname']
            data['variableid'] = result['varuuid']

        data['name'] = repr("fun015_%s") % (i-1)
        sql = "UPDATE {table_name} SET `variable`='{variable}', `variableid`='{variableid}' WHERE `name` = {name};"\
            .format(table_name=data['table_name'],
                    name=data['name'],
                    variable=data['variable'],
                    variableid=data['variableid'])
        print(sql)
        insertsql.write(sql + "\n")

    insertsql.close()


def bindQVartoTVar016():
    """将数据库变量与TCP功能码为016的变量绑定"""
    data = {
            'table_name': "`teacher`.`project_iovariable_modbus`",
            'name': "",
            'variable': repr(''),
            'variableid': repr('')
        }

    insertsql = open("bindSVartoTVar016.txt", 'w')

    connection = pymysql.connect(host="192.168.3.30",
                           port=3306,
                           user="root",
                           password="123456",
                           db="teacher",
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

    for i in range(1, 121):
        for j in range(1,12):
            # 创建sql 语句
            data['name'] = repr("fun16x%s") % i

            with connection.cursor() as cursor:
                # Create a new record
                selectSQL = "SELECT varname, varuuid FROM `project_variable` WHERE `varname` = {name};".format(name=data['name'])
                cursor.execute(selectSQL)
                result = cursor.fetchone()
                print(result)
                data['variable'] = result['varname']
                data['variableid'] = result['varuuid']

            data['name'] = repr("fun016_%s_%s") % (j, (i-1))
            sql = "UPDATE {table_name} SET `variable`='{variable}', `variableid`='{variableid}' WHERE `name` = {name};"\
                .format(table_name=data['table_name'],
                        name=data['name'],
                        variable=data['variable'],
                        variableid=data['variableid'])
            print(sql)
            insertsql.write(sql + "\n")

    insertsql.close()


def bindQVartoTVar05():
    """将数据库变量与TCP功能码为05的变量绑定"""
    data = {
            'table_name': "`teacher`.`project_iovariable_modbus`",
            'name': "",
            'variable': repr(''),
            'variableid': repr('')
        }

    insertsql = open("bindSVartoTVar05.txt", 'w')

    connection = pymysql.connect(host="192.168.3.30",
                           port=3306,
                           user="root",
                           password="123456",
                           db="teacher",
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

    for i in range(1, 1251):
        # 创建sql 语句
        data['name'] = repr("fun05x%s") % i

        with connection.cursor() as cursor:
            # Create a new record
            selectSQL = "SELECT varname, varuuid FROM `project_variable` WHERE `varname` = {name};".format(name=data['name'])
            cursor.execute(selectSQL)
            result = cursor.fetchone()
            print(result)
            data['variable'] = result['varname']
            data['variableid'] = result['varuuid']

        data['name'] = repr("fun05x%s") % i
        sql = "UPDATE {table_name} SET `variable`='{variable}', `variableid`='{variableid}' WHERE `name` = {name};"\
            .format(table_name=data['table_name'],
                    name=data['name'],
                    variable=data['variable'],
                    variableid=data['variableid'])
        print(sql)
        insertsql.write(sql + "\n")

    insertsql.close()


def bindQVartoTVar06():
    """将数据库变量与TCP功能码为06的变量绑定"""
    data = {
            'table_name': "`teacher`.`project_iovariable_modbus`",
            'name': "",
            'variable': repr(''),
            'variableid': repr('')
        }

    insertsql = open("bindSVartoTVar06.txt", 'w')

    connection = pymysql.connect(host="192.168.3.30",
                           port=3306,
                           user="root",
                           password="123456",
                           db="teacher",
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

    for i in range(1, 1251):
        # 创建sql 语句
        data['name'] = repr("fun06x%s") % i

        with connection.cursor() as cursor:
            # Create a new record
            selectSQL = "SELECT varname, varuuid FROM `project_variable` WHERE `varname` = {name};".format(name=data['name'])
            cursor.execute(selectSQL)
            result = cursor.fetchone()
            print(result)
            data['variable'] = result['varname']
            data['variableid'] = result['varuuid']

        data['name'] = repr("fun06x%s") % i
        sql = "UPDATE {table_name} SET `variable`='{variable}', `variableid`='{variableid}' WHERE `name` = {name};"\
            .format(table_name=data['table_name'],
                    name=data['name'],
                    variable=data['variable'],
                    variableid=data['variableid'])
        print(sql)
        insertsql.write(sql + "\n")

    insertsql.close()


def updateperiod():
    """更新TCP变量的采集频率"""
    data = {
        'table_name': "`teacher`.`project_iovariable_modbus`",
        'name': ""
    }

    insertsql = open("updateperiod.txt", 'w')

    for i in range(1, 126):
        for j in range(1,5):
            # 创建sql 语句
            if j == 1:
                data['name'] = repr("fun03_%s") % (i-1)
            else:
                data['name'] = repr("fun03_%s_%s") % (j, (i - 1))
            sql = "UPDATE {table_name} SET `period`={period} WHERE `name` = {name};" \
                .format(table_name=data['table_name'],
                        name=data['name'],
                        period=100)
            print(sql)
            insertsql.write(sql + "\n")

    insertsql.close()


if __name__ == "__main__":
    # sqlvar()
    # modbusfun05()
    # modbusfun06()
    # bindQVartoTVar01()
    # bindQVartoTVar02()
    bindQVartoTVar03()
    # bindQVartoTVar04()
    # bindQVartoTVar015()
    # bindQVartoTVar016()
    # bindQVartoTVar05()
    # bindQVartoTVar06()
    # updateperiod()
