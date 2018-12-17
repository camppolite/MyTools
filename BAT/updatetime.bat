@echo off
:start
net use \\192.168.3.199 "123456" /user:"wudr"
net time \\192.168.3.199 /set /y
net use * /del /y
::每多少秒执行一次start
ping localhost -n 300 > nul

goto start
pause