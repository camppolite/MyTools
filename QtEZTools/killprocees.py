#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""清理QtEZ退出后没有自动结束的进程"""

import autoit

p1 = "getserver"
p2 = "servers"
for i in range(1,1000):
    autoit.process_close(p1 + str(i) + ".exe")
    autoit.process_close(p2 + str(i) + ".exe")
