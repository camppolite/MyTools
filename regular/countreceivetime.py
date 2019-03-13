import re
import datetime


def countreceivetime():
    """读取文件记录的时间，计算接收时间"""
    with open("20190221_100335.log", "r+", encoding='utf-8') as f:
        txt = f.readlines()

    print(txt)


if __name__ == '__main__':
    # countreceivetime()
    t1 = datetime.time(10, 16, 41, 83)
    t2 = datetime.time(10, 16, 41, 888)
    # length = t2 - t1
    # print(length)
    print(datetime.date.today())
