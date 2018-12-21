#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""批量生成256个插件"""

import shutil
import os
import xml.etree.ElementTree as ET


def replaceplugnname(srcname, name, plugintype="dll"):
    """替换插件名称"""
    plugindir = "plugins/" + name + "/"  # 新插件的目录

    # 替换MANIFEST.MF文件
    with open(plugindir + "MANIFEST.MF", "r+", encoding="utf-8") as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        content_new = content.replace(srcname, name)
        f.write(content_new)

    # 替换resource.qrc文件
    with open(plugindir + "resource.qrc", "r+", encoding="utf-8") as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        content_new = content.replace(srcname, name)
        f.write(content_new)

    # 替换mypluginclassname.cpp文件
    with open(plugindir + "mypluginclassname.cpp", "r+", encoding="utf-8") as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        content_new = content.replace(srcname, name)
        f.write(content_new)

    # 替换mypluginclassname.h文件
    with open(plugindir + "mypluginclassname.h", "r+", encoding="utf-8") as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        content_new = content.replace(srcname, name)
        f.write(content_new)

    # 替换mypluginclassname.cpp文件
    with open(plugindir + "mypluginclassname.cpp", "r+", encoding="utf-8") as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        content_new = content.replace(srcname, name)
        f.write(content_new)

    # 替换plug.xml文件
    with open(plugindir + "plug.xml", "r+", encoding="utf-8") as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        content_new = content.replace(srcname, name)
        f.write(content_new)

    # 替换plugin.pro文件
    with open(plugindir + srcname + ".pro", "r+", encoding="utf-8") as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        content_new = content.replace(srcname, name)
        f.write(content_new)

    # 重命名插件的pro文件
    os.renames(plugindir + srcname + ".pro", plugindir + name + ".pro")

    if plugintype == "exe":
        # 替换main.cpp文件
        with open(plugindir + "main.cpp", "r+", encoding="utf-8") as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            content_new = content.replace(srcname, name)
            f.write(content_new)


def replacexmlattrib(xml):
    """替换插件plug.xml文件的属性，包括id，name，title等"""
    tree = ET.parse(xml)
    root = tree.getroot()

    backboradExtData = root.find(".//*[@extendPoint='qtez.mainwindow.pad.backboard']")
    backboradExtDataID = backboradExtData.attrib["id"] + str(i)
    backboradExtData.set("id", backboradExtDataID)

    BackBoardData = root.find(".//*[@key='BackBoard']")
    BackBoardDataID = BackBoardData.attrib["id"] + str(i)
    BackBoardDataTitle = BackBoardData.attrib["title"] + str(i)
    BackBoardData.set("id", BackBoardDataID)
    BackBoardData.set("title", BackBoardDataTitle)

    floatingwindowExtData = root.find(".//*[@extendPoint='qtez.mainwindow.pad.floatingwindow']")
    floatingwindowExtDataID = floatingwindowExtData.attrib["id"] + str(i)
    floatingwindowExtData.set("id", floatingwindowExtDataID)

    FloatingWindowData = root.find(".//*[@key='FloatingWindow']")
    FloatingWindowDataID = FloatingWindowData.attrib["id"] + str(i)
    FloatingWindowDataTitle = FloatingWindowData.attrib["title"] + str(i)
    FloatingWindowData.set("id", FloatingWindowDataID)
    FloatingWindowData.set("title", FloatingWindowDataTitle)

    navigationExtData = root.find(".//*[@extendPoint='qtez.mainwindow.pad.navigation']")
    navigationExtDataID = navigationExtData.attrib["id"] + str(i)
    navigationExtData.set("id", navigationExtDataID)

    NavigationMenuData = root.find(".//*[@key='NavigationMenu']")
    NavigationMenuDataID = NavigationMenuData.attrib["id"] + str(i)
    NavigationMenuDataName = NavigationMenuData.attrib["name"] + str(i)
    NavigationMenuData.set("id", NavigationMenuDataID)
    NavigationMenuData.set("name", NavigationMenuDataName)

    NavigationActionData = root.find(".//*[@key='NavigationAction']")
    NavigationActionDataID = NavigationActionData.attrib["id"] + str(i)
    NavigationActionDataName = NavigationActionData.attrib["name"] + str(i)
    NavigationActionData.set("id", NavigationActionDataID)
    NavigationActionData.set("name", NavigationActionDataName)

    tree.write(xml, encoding="utf-8")


if __name__ == '__main__':
    srcpluginname = "plugin001"  # 原始插件名
    quantity = 257  # 插件数量

    file_pro = open("plugins.pro", "r+")
    content_plgs = file_pro.read()
    # 清空文件
    file_pro.seek(0)
    file_pro.truncate()

    dllpluginname = "dll.mypluginname"
    exepluginname = "exe.mypluginname"

    shutil.rmtree("plugins", ignore_errors=True)

    # 批量生成多个插件
    for i in range(quantity):
        newname = dllpluginname + str(i)
        shutil.copytree(srcpluginname, "plugins/" + newname)  # 拷贝文件夹

        replaceplugnname(srcpluginname, newname, plugintype="dll")

        plug_xml = "plugins/" + newname + "/" + "plug.xml"
        replacexmlattrib(plug_xml)

        file_pro.write("SUBDIRS += " + newname + "\n")  # 生成pro要包含的插件名称
    file_pro.close()
