# -*- coding: utf-8 -*-

import os
import re


def get_wifi_pwd():
    """
    获取/data/misc/wifi/wpa_supplicant.conf的wifi名称和密码，返回以[(ssid,psk)]组成的列表,
    如果没有密码，则返回None
    """
    output = os.popen("su -c 'cat /data/misc/wifi/wpa_supplicant.conf'")
    # output = open("wpa_supplicant.conf", "r")
    pwa_text = output.read()

    ssid = re.findall("\Wssid.*", pwa_text)
    psk = re.findall("\Wpsk.*", pwa_text)
    if not ssid or not psk:
        return None
    for i in range(len(ssid)):
        ssid[i] = re.sub('\tssid=', '', ssid[i])
        ssid[i] = re.sub('^"', '', ssid[i])
        ssid[i] = re.sub('"$', '', ssid[i])
    for i in range(len(psk)):
        psk[i] = re.sub('\tpsk=', '', psk[i])
        psk[i] = re.sub('^"', '', psk[i])
        psk[i] = re.sub('"$', '', psk[i])

    return list(zip(ssid, psk))


if __name__ == '__main__':
    pwd = get_wifi_pwd()
    if pwd:
        for key, value in pwd:
            print(key, value)
    else:
        print("没有密码")