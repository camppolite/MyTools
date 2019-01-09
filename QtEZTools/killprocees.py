#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""清理QtEZ退出后没有自动结束的进程"""

import subprocess
import threading

p = subprocess.Popen("TASKKILL /IM  %s /F" % "CanvaExecute.exe", shell=True, stdout=subprocess.PIPE)
print("kill process:", p.communicate()[0].decode("utf-8"))
p = subprocess.Popen("TASKKILL /IM  %s /F" % "DbusDaemon.exe", shell=True, stdout=subprocess.PIPE)
print("kill process:", p.communicate()[0].decode("utf-8"))
p = subprocess.Popen("TASKKILL /IM  %s /F" % "dbus-daemon.exe", shell=True, stdout=subprocess.PIPE)
print("kill process:", p.communicate()[0].decode("utf-8"))


def fun1():
    name = "getserver"
    for i in range(1,1000):
        p = subprocess.Popen("TASKKILL /IM  %s /F" % (name + str(i) + ".exe"), shell=True, stdout=subprocess.PIPE)
        print("kill process:", p.communicate()[0].decode("utf-8"))


def fun2():
    name = "servers"
    for i in range(1,1000):
        p = subprocess.Popen("TASKKILL /IM  %s /F" % (name + str(i) + ".exe"), shell=True, stdout=subprocess.PIPE)
        print("kill process:", p.communicate()[0].decode("utf-8"))

t1 = threading.Thread(target=fun1, name="Thread-1")
t2 = threading.Thread(target=fun2, name="Thread-2")
t1.start()
t2.start()
t1.join()
t2.join()
