# -*- coding: utf-8 -*-

import os
import re


def get_wifi_pwd():
    """
    获取/data/misc/wifi/wpa_supplicant.conf的wifi名称和密码，返回以{({ssid:''},{psk:''})}组成的字典
    """
    output = os.popen("su -c 'cat /data/misc/wifi/wpa_supplicant.conf'")
    # output = open("wpa_supplicant.conf", "r")
    pwa_text = output.read()

    ssid = re.findall("\s+ssid.*", pwa_text)
    psk = re.findall("\s+psk.*", pwa_text)

    for i in range(len(ssid)):
        ssid[i] = ssid[i].lstrip()
        key, value = ssid[i].split("=")
        dic = dict()
        dic[key] = value.lstrip('\"').rstrip('\"')
        ssid[i] = dic
    for i in range(len(psk)):
        psk[i] = psk[i].lstrip()
        key, value = psk[i].split("=")
        dic = dict()
        dic[key] = value.lstrip('\"').rstrip('\"')
        psk[i] = dic

    list1 = list(zip(ssid, psk))
    length = len(list1)
    list2 = [i for i in range(length)]
    wifi_pwd = {}
    for i in range(length):
        wifi_pwd[list2[i]] = list1[i]

    return wifi_pwd


if __name__ == '__main__':
    pwd = get_wifi_pwd()
    print(pwd)
    print(pwd[0][0]['ssid'])
    print(pwd[0][1]['psk'])
