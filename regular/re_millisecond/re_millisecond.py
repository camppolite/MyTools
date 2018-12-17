# _*_ coding:utf-8 _*_
import re


def getmillisecond():

    """获取毫秒的数值"""
    receive = open("receivetime.txt", "r")
    sendtime = open("sendtime.txt", "r")
    receive_txt = receive.read()
    sendtime_txt = sendtime.read()

    # 匹配.号后面的数字
    r_time = re.findall(r"\.(\d+)", receive_txt)
    s_time = re.findall(r"\.(\d+)", sendtime_txt)
    f1 = open("receive_s.txt", "w")
    for i in r_time:
        f1.truncate()
        f1.write(i)
        f1.write("\n")
    f1.close()

    f2 = open("sendtime_s.txt", "w")
    for i in s_time:
        f2.truncate()
        f2.write(i)
        f2.write("\n")
    f2.close()

    receive.close()
    sendtime.close()


def gettime():
    """获取时间"""
    receive = open("receivetime.txt", "r")
    sendtime = open("sendtime.txt", "r")
    receive_txt = receive.read()
    sendtime_txt = sendtime.read()

    # 匹配空格后面的时间
    r_time = re.findall(r" (.*)", receive_txt)
    # 匹配空格前面的时间
    s_time = re.findall(r"(.*) ", sendtime_txt)

    f1 = open("receive.txt", "w")
    for i in r_time:
        f1.truncate()
        f1.write(i)
        f1.write("\n")
    f1.close()

    f2 = open("send.txt", "w")
    for i in s_time:
        f2.truncate()
        f2.write(i)
        f2.write("\n")
    f2.close()

    receive.close()
    sendtime.close()

if __name__ == '__main__':
    getmillisecond()
    gettime()
