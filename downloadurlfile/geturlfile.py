import urllib.request
import os

fileurl = 'http://soft.huweishen.com/action/down.asp?id=78&s=1'
filename = os.getcwd() + "/" + "111.txt"
local_filename, headers = urllib.request.urlretrieve(fileurl, filename)
