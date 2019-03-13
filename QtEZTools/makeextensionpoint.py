#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""批量生成扩展点实现"""

f = open("extensionpoint.txt", "r+")
content = f.read()
f.seek(0)
f.truncate()  # 清空文件

quantity = 1001  # 扩展点数量

for i in range(quantity):
    ExtensionID = "193cb6fbda3f"
    ExtensionName = "New Toolbar"
    ExtensionID_new = ExtensionID + str(i)
    ExtensionName_new = ExtensionName + str(i)
    content_new = content.replace(ExtensionID, ExtensionID_new).replace(ExtensionName, ExtensionName_new)

    # ExtensionID = "c1cc23d72a52"
    # ExtensionName = "New Action"
    # ExtensionID_new = ExtensionID + str(i)
    # ExtensionName_new = ExtensionName + str(i)
    # content_new = content_new.replace(ExtensionID, ExtensionID_new).replace(ExtensionName, ExtensionName_new)

    f.write(content_new + "\n")

f.close()
