# !/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Wu Dirui'
__version__ = "0.2"

from io import StringIO
import xml.etree.ElementTree as ET


class ModifyFile:
    """
    修改文件
    """
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        self.TmpFile = None
        self.getservice_dll = "call interface directly."
        self.getservice_exe = "call interface cross process."
        self.getservice_return = "The return value is:"
        self.sync = "sync"
        self.async = "async"
        self.servicefile = "getserviceresult.txt"
        self.eventfile = "eventresult.txt"
        self.msgfile_sync = "msgrecevieresult_sync.txt"
        self.msgfile_async = "msgrecevieresult_async.txt"

    def modify_servicename_h(self, file):
        """
        ----------------------------------------------------------------------------------------------------------------

        [参数]
        file(文件名)   文件名：servicename.h
        ----------------------------------------------------------------------------------------------------------------
        [描述]
        修改插件的服务名.h文件，声明具体的服务方法
        """
        with open(file, "r", encoding='utf-8') as f:
            self.TmpFile = StringIO(f.read())
        with open(file, "r+", encoding='utf-8') as f:
            index = 0
            for line in self.TmpFile:
                index += 1
                # 在第i行插入内容
                if index == 8:
                    # 在class里增加内容
                    f.write("    virtual int show(const QString &msg) = 0;\n")
                f.write(line)
                f.flush()

    def modify_serviceclassname_h(self, file):
        """
        ----------------------------------------------------------------------------------------------------------------

        [参数]
        file(文件名)   文件名:serviceclassname.h
        ----------------------------------------------------------------------------------------------------------------
        [描述]
        修改插件的服务类名.h文件，并实现服务
        """
        with open(file, "r", encoding='utf-8') as f:
            self.TmpFile = StringIO(f.read())
        with open(file, "r+", encoding='utf-8') as f:
            index = 0
            for line in self.TmpFile:
                index += 1
                # 在第i行插入内容
                if index == 8:
                    # 在开头增加内容
                    f.write("#include <QMessageBox>\n")
                if index == 20:
                    # 在class里增加内容
                    f.write('    Q_INVOKABLE int show(const QString &msg)\n')
                    f.write('    {\n')
                    f.write('        return QMessageBox::warning(0, "WarningMessageBox", msg,\n')
                    f.write('                                    QMessageBox::Ok | QMessageBox::Cancel);\n')
                    f.write('    }\n')
                f.write(line)
                f.flush()

    def modify_dll_getservice_cpp(self, file):
        """
        ----------------------------------------------------------------------------------------------------------------

        [参数]
        file(文件名)   文件名:serviceclassname.cpp
        ----------------------------------------------------------------------------------------------------------------
        [描述]
        修改动态库插件的.cpp文件，获取并调用服务，最后会在app目录下生成getserviceresult.txt文件，保存调用的结果。
        """
        with open(file, "r", encoding='utf-8') as f:
            self.TmpFile = StringIO(f.read())
        with open(file, "r+", encoding='utf-8') as f:
            index = 0
            for line in self.TmpFile:
                index += 1
                # 在第i行插入内容
                if index == 12:
                    # 在开头增加内容
                    f.write('#include <QFile>\n')
                if index == 150:
                    # 在getServices函数里的foreach循环里增加内容
                    f.write('            m_IMessageBox_WarningMessageBox = qobject_cast<IMessageBox*>'
                            '(reg.getService());\n')
                    f.write('            QString msg = QString("%1: {first}").arg(m_proxy->symbolic());\n'.
                            format(first=self.getservice_dll))
                    f.write('            int ret = m_IMessageBox_WarningMessageBox->show(msg);\n')
                    f.write('            QFile file("{servicefile}");\n'.format(servicefile=self.servicefile))
                    f.write('            file.open(QIODevice::ReadWrite);\n')
                    f.write('            QString data = msg + "{first}" + QString(ret);\n'.
                            format(first=self.getservice_return))
                    f.write('            qDebug()<<data;\n')
                    f.write('            file.write(data.toLocal8Bit());\n')
                    f.write('            file.close();\n')
                f.write(line)
                f.flush()

    def modify_exe_getservice_cpp(self, file):
        """
        ----------------------------------------------------------------------------------------------------------------

        [参数]
        file(文件名)   文件名:serviceclassname.cpp
        ----------------------------------------------------------------------------------------------------------------
        [描述]
        修改可执行程序插件的.cpp文件，获取并调用服务，最后会在app目录下生成getserviceresult.txt文件，保存调用的结果。
        """
        with open(file, "r", encoding='utf-8') as f:
            self.TmpFile = StringIO(f.read())
        with open(file, "r+", encoding='utf-8') as f:
            index = 0
            for line in self.TmpFile:
                index += 1
                # 在第i行插入内容
                if index == 12:
                    # 在开头增加内容
                    f.write('#include <QFile>\n')
                if index == 150:
                    # 在getServices函数里的foreach循环里增加内容
                    f.write('            int ret = 0;\n')
                    f.write('            QString msg = QString("%1: {first}").arg(m_proxy->symbolic());\n'.
                            format(first=self.getservice_exe))
                    f.write('            reg.callInterface("show", QtEZ_RETURN_ARG(int, ret),'
                            'QtEZ_ARG(QString, msg));\n')
                    f.write('            QFile file("{servicefile}");\n'.format(servicefile=self.servicefile))
                    f.write('            file.open(QIODevice::ReadWrite);\n')
                    f.write('            QString data = msg + "{first}" + QString(ret);\n'.
                            format(first=self.getservice_return))
                    f.write('            qDebug()<<msg << "{first}" << ret;\n'.
                            format(first=self.getservice_return))
                    f.write('            file.write(data.toLocal8Bit());\n')
                    f.write('            file.close();\n')
                f.write(line)
                f.flush()

    def modify_event_sync_cpp(self, file):
        """
        ----------------------------------------------------------------------------------------------------------------

        [参数]
        file(文件名)   文件名:eventhandler.cpp
        ----------------------------------------------------------------------------------------------------------------
        [描述]
        修改同步事件.cpp文件，包括动态库和可执行程序类型插件，接收事件信息，
        最后会在app目录下生成eventresult.txt文件，保存调用的结果。
        """
        with open(file, "r", encoding='utf-8') as f:
            self.TmpFile = StringIO(f.read())
        with open(file, "r+", encoding='utf-8') as f:
            index = 0
            for line in self.TmpFile:
                index += 1
                # 在第i行插入内容
                if index == 3:
                    # 在开头增加内容
                    f.write('#include <QFile>\n')
                    f.write('QFile file("{eventfile}");\n'.format(eventfile=self.eventfile))
                if index == 9:
                    # 在构造函数里增加内容
                    f.write('    file.open(QIODevice::ReadWrite);\n')
                if index == 15:
                    # 在析构函数里增加内容
                    f.write('    file.close();\n')
                if index == 27:
                    # 在handleEvent函数内增加内容
                    f.write('    QString data = QString("handle event %1 by {sync}.\\r\\n").arg(event.type());\n'.
                            format(sync=self.sync))
                    f.write('    qDebug()<<data;\n')
                    f.write('    file.write(data.toLocal8Bit());\n')
                f.write(line)
                f.flush()

    def modify_event_async_cpp(self, file):
        """
        ----------------------------------------------------------------------------------------------------------------

        [参数]
        file(文件名)   文件名:eventhandler.cpp
        ----------------------------------------------------------------------------------------------------------------
        [描述]
        修改异步事件.cpp文件，包括动态库和可执行程序类型插件，接收事件信息，
        最后会在app目录下生成eventresult.txt文件，保存调用的结果。
        """
        with open(file, "r", encoding='utf-8') as f:
            self.TmpFile = StringIO(f.read())
        with open(file, "r+", encoding='utf-8') as f:
            index = 0
            for line in self.TmpFile:
                index += 1
                # 在第i行插入内容
                if index == 3:
                    # 增加头文件
                    f.write('#include <QFile>\n')
                    f.write('QFile file("{eventfile}");\n'.format(eventfile=self.eventfile))
                if index == 9:
                    # 在构造函数内增加内容
                    f.write('    file.open(QIODevice::ReadWrite);\n')
                if index == 15:
                    # 在析构函数内增加内容
                    f.write('    file.close();\n')
                if index == 27:
                    # 在自定义处理函数内增加内容
                    f.write('    QString data = QString("handle event %1 by {async}.\\r\\n").arg(event.type());\n'.
                            format(async=self.async))
                    f.write('    qDebug()<<data;\n')
                    f.write('    file.write(data.toLocal8Bit());\n')
                f.write(line)
                f.flush()

    def modify_msgadmin_sync_sender_cpp_v1(self, file, topic):
        """
        ----------------------------------------------------------------------------------------------------------------

        [参数]
        file(文件名)   文件名: messagesenderhandler.cpp
        topic（消息主题）   消息主题：topic
        ----------------------------------------------------------------------------------------------------------------
        [描述]
        v1:针对MessageAdmin 1.0版本的用法，即使用扩展点，配置xml文件的用法。
        修改同步消息通讯.cpp文件，包括动态库和可执行程序类型插件，发送消息。
        """
        with open(file, "r", encoding='utf-8') as f:
            self.TmpFile = StringIO(f.read())
        with open(file, "r+", encoding='utf-8') as f:
            index = 0
            for line in self.TmpFile:
                index += 1
                # 在第i行插入内容
                if index == 2:
                    # 在开头增加内容
                    f.write('#include <QVariantHash>\n')
                if index == 18:
                    # 在active函数里增加内容
                    f.write('    QVariantHash event;\n')
                    f.write('    event.insert("key1", "Hello, World");\n')
                    f.write('    event.insert("key2", "I come from sync topic");\n')
                    f.write('    m_messageManager->sendMessage("{topic}",event);\n'.format(topic=topic))
                f.write(line)
                f.flush()

    def modify_msgadmin_sync_recevier_cpp_v1(self, file):
        """
        ----------------------------------------------------------------------------------------------------------------

        [参数]
        file(文件名)   文件名: messagereceiverhandler.cpp
        ----------------------------------------------------------------------------------------------------------------
        [描述]
        v1:针对MessageAdmin 1.0版本的用法，即使用扩展点，配置xml文件的用法。
        修改同步消息通讯.cpp文件，包括动态库和可执行程序类型插件，接收消息，
        最后会在app目录下生成msgrecevieresult_sync.txt文件，保存调用的结果。
        """
        with open(file, "r", encoding='utf-8') as f:
            self.TmpFile = StringIO(f.read())
        with open(file, "r+", encoding='utf-8') as f:
            index = 0
            for line in self.TmpFile:
                index += 1
                # 在第i行插入内容
                if index == 2:
                    # 在开头增加内容
                    f.write('#include <QVariantHash>\n')
                    f.write('#include <QFile>\n')
                    f.write('QFile file("{msgfile_sync}");\n'.format(msgfile_sync=self.msgfile_sync))
                if index == 7:
                    # 在构造函数里增加内容
                    f.write('    file.open(QIODevice::ReadWrite);\n')
                if index == 12:
                    # 在析构函数里增加内容
                    f.write('    file.close();\n')
                if index == 18:
                    # 在handleMessage函数里增加内容
                    f.write('    QString data = QString("Recevie message by sync:")\n')
                    f.write('    qDebug()<<data<<event.value("key1").toString()<<", "'
                            '<<event.value("key2").toString();\n')
                    f.write('    file.write(data.toLocal8Bit());\n')
                    f.write('    file.write(event.value("key1").toString().toLocal8Bit());\n')
                    f.write('    file.write(", ");\n')
                    f.write('    file.write(event.value("key2").toString().toLocal8Bit());\n')
                f.write(line)
                f.flush()

    def modify_msgadmin_async_sender_h_v1(self, file):
        """
        ----------------------------------------------------------------------------------------------------------------

        [参数]
        file(文件名)   文件名: messagesenderhandler.h
        ----------------------------------------------------------------------------------------------------------------
        [描述]
        v1:针对MessageAdmin 1.0版本的用法，即使用扩展点，配置xml文件的用法。
        修改异步消息通讯.h文件，包括动态库和可执行程序类型插件，发送消息。
        """
        with open(file, "r", encoding='utf-8') as f:
            self.TmpFile = StringIO(f.read())
        with open(file, "r+", encoding='utf-8') as f:
            index = 0
            for line in self.TmpFile:
                index += 1
                # 在第i行插入内容
                if index == 22:
                    # 在signals里增加内容
                    f.write('    void SendMessage(const QVariantHash &message);\n')
                if index == 25:
                    # 在public slots里增加内容
                    f.write('    void onsendMessage();\n')
                f.write(line)
                f.flush()

    def modify_msgadmin_async_sender_cpp_v1(self, file):
        """
        ----------------------------------------------------------------------------------------------------------------

        [参数]
        file(文件名)   文件名: messagesenderhandler.cpp
        ----------------------------------------------------------------------------------------------------------------
        [描述]
        v1:针对MessageAdmin 1.0版本的用法，即使用扩展点，配置xml文件的用法。
        修改异步消息通讯.cpp文件，包括动态库和可执行程序类型插件，发送消息。
        """
        with open(file, "r", encoding='utf-8') as f:
            self.TmpFile = StringIO(f.read())
        with open(file, "r+", encoding='utf-8') as f:
            index = 0
            for line in self.TmpFile:
                index += 1
                # 在第i行插入内容
                if index == 2:
                    # 在开头增加内容
                    f.write('#include <QTimer>\n')
                    f.write('#include <QVariantHash>\n')
                if index == 7:
                    # 在构造函数里增加内容
                    f.write('QTimer::singleShot(10, this, SLOT(onsendMessage()));\n')
                if index == 15:
                    # 实现槽函数
                    f.write('void MessageSenderHandler::onsendMessage()\n')
                    f.write('{\n')
                    f.write('    QVariantHash event;\n')
                    f.write('    event.insert("key1", "Hello, World");\n')
                    f.write('    event.insert("key2", "I come from async topic");\n')
                    f.write('    emit SendMessage(event);\n')
                    f.write('}\n')
                f.write(line)
                f.flush()

    @staticmethod
    def modify_msgadmin_async_sender_xml_v1(file):
        """
        ----------------------------------------------------------------------------------------------------------------

        [参数]
        file(文件名)   文件名: plug.xml
        ----------------------------------------------------------------------------------------------------------------
        [描述]
        v1:针对MessageAdmin 1.0版本的用法，即使用扩展点，配置xml文件的用法。
        修改异步消息通讯.xml文件，包括动态库和可执行程序类型插件，发送消息。
        """
        tree = ET.parse(file)
        root = tree.getroot()
        data = root.find(".//*[@role='MessageReceiver']")
        data.set("method", "SendMessage(const QVariantHash)")
        tree.write(file, encoding="utf-8")

    def modify_msgadmin_async_recevier_h_v1(self, file):
        """
        ----------------------------------------------------------------------------------------------------------------

        [参数]
        file(文件名)   文件名: messagereceiverhandler.h
        ----------------------------------------------------------------------------------------------------------------
        [描述]
        v1:针对MessageAdmin 1.0版本的用法，即使用扩展点，配置xml文件的用法。
        修改异步消息通讯.h文件，包括动态库和可执行程序类型插件，接收消息，
        """
        with open(file, "r", encoding='utf-8') as f:
            self.TmpFile = StringIO(f.read())
        with open(file, "r+", encoding='utf-8') as f:
            index = 0
            for line in self.TmpFile:
                index += 1
                # 在第i行插入内容
                if index == 23:
                    # 在public slots增加内容
                    f.write('void GetMessage(const QVariantHash &event);\n')
                f.write(line)
                f.flush()

    def modify_msgadmin_async_recevier_cpp_v1(self, file):
        """
        ----------------------------------------------------------------------------------------------------------------

        [参数]
        file(文件名)   文件名: messagereceiverhandler.cpp
        ----------------------------------------------------------------------------------------------------------------
        [描述]
        v1:针对MessageAdmin 1.0版本的用法，即使用扩展点，配置xml文件的用法。
        修改异步消息通讯.cpp文件，包括动态库和可执行程序类型插件，接收消息，
        最后会在app目录下生成msgrecevieresult_async.txt文件，保存调用的结果。
        """
        with open(file, "r", encoding='utf-8') as f:
            self.TmpFile = StringIO(f.read())
        with open(file, "r+", encoding='utf-8') as f:
            index = 0
            for line in self.TmpFile:
                index += 1
                # 在第i行插入内容
                if index == 2:
                    # 在开头增加内容
                    f.write('#include <QVariantHash>\n')
                    f.write('#include <QFile>\n')
                    f.write('QFile file("{msgfile_async}");\n'.format(msgfile_async=self.msgfile_async))
                if index == 7:
                    # 在构造函数里增加内容
                    f.write('    file.open(QIODevice::ReadWrite);\n')
                if index == 12:
                    # 在析构函数里增加内容
                    f.write('    file.close();\n')
                f.write(line)
                f.flush()
            # 在文件末尾增加内容
            f.write('\n')
            f.write('void MessageReceiverHandler::GetMessage(const QVariantHash &event)\n')
            f.write('{\n')
            f.write('\n')
            f.write('    QString data = QString("Recevie message by async:")\n')
            f.write('    qDebug()<<data<<event.value("key1").toString()<<", "'
                    '<<event.value("key2").toString();\n')
            f.write('    file.write(data.toLocal8Bit());\n')
            f.write('    file.write(event.value("key1").toString().toLocal8Bit());\n')
            f.write('    file.write(", ");\n')
            f.write('    file.write(event.value("key2").toString().toLocal8Bit());\n')
            f.write('}\n')

    @staticmethod
    def modify_msgadmin_async_recevier_xml_v1(file):
        """
        ----------------------------------------------------------------------------------------------------------------

        [参数]
        file(文件名)   文件名: plug.xml
        ----------------------------------------------------------------------------------------------------------------
        [描述]
        v1:针对MessageAdmin 1.0版本的用法，即使用扩展点，配置xml文件的用法。
        修改异步消息通讯.xml文件，包括动态库和可执行程序类型插件，发送消息。
        """
        tree = ET.parse(file)
        root = tree.getroot()
        data = root.find(".//*[@role='MessageReceiver']")
        data.set("method", "GetMessage(const QVariantHash)")
        tree.write(file, encoding="utf-8")


if __name__ == '__main__':
    try:
        import tkinter as tk
        from tkinter import filedialog
        from tkinter import messagebox
    except ImportError:
        import Tkinter as tk
        import tkFileDialog as filedialog
        import tkMessageBox as messagebox

    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.master.rowconfigure(0, weight=1)
            self.master.columnconfigure(0, weight=1)
            # 窗口标题
            self.master.title("名称不重要")

            sw = self.master.winfo_screenwidth()
            # 得到屏幕宽度
            sh = self.master.winfo_screenheight()
            # 得到屏幕高度
            ww = 550
            wh = 700
            # 窗口宽高为100
            x = (sw - ww) / 2
            y = (sh - wh) / 2
            self.master.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

            # 窗口UI
            self.msg_sync()
            self.msg_asnyc()
            self.server_regist()
            self.server_dll_get()
            self.server_exe_get()
            self.event_sync()
            self.event_async()

            self.Btn_frame = tk.Frame(self.master, borderwidth=5, relief="ridge")
            self.Btn_frame.grid(column=0, row=7, sticky="nsew")
            self.Btn_frame.rowconfigure(0, weight=1)
            self.Btn_frame.columnconfigure(0, weight=1)

            self.finish_btn = tk.Button(self.Btn_frame, text="完成", command=self.on_finish)
            self.finish_btn.grid(column=0, row=0)

        def msg_sync(self):
            self.msg_sync_frame = tk.Frame(self.master, borderwidth=5, relief="ridge")
            self.msg_sync_frame.grid(column=0, row=0, sticky="nsew")
            self.msg_sync_frame.rowconfigure(0, weight=1)
            self.msg_sync_frame.columnconfigure(0, weight=1)

            self.msg_sync_label = tk.Label(self.msg_sync_frame, text='消息通讯-同步连接')
            self.msg_sync_label.grid(column=0, row=0, columnspan=5, sticky="nsew")

            self.msg_sync_send_label = tk.Label(self.msg_sync_frame, text='选择发送方cpp文件:')
            self.msg_sync_send_label.grid(column=0, row=1)

            self.msg_sync_send_file = str()
            self.msg_sync_send_entry = tk.Entry(self.msg_sync_frame, textvariable=self.msg_sync_send_file)
            self.msg_sync_send_entry.grid(column=1, row=1, columnspan=3)
            self.msg_sync_send_entry.insert(0, "senderrolehandler.cpp")

            self.msg_sync_topic_label = tk.Label(self.msg_sync_frame, text='主题:')
            self.msg_sync_topic_label.grid(column=4, row=1)

            self.msg_sync_topic = str()
            self.msg_sync_topic_entry = tk.Entry(self.msg_sync_frame, textvariable=self.msg_sync_topic)
            self.msg_sync_topic_entry.grid(column=5, row=1)
            self.msg_sync_topic_entry.insert(0, "topic")

            self.msg_sync_send_btn = tk.Button(self.msg_sync_frame, text="选择文件",
                                               command=self.set_msg_sync_send_file)
            self.msg_sync_send_btn.grid(column=6, row=1)

            self.msg_sync_recv_btn = tk.Label(self.msg_sync_frame, text="选择接收方cpp文件")
            self.msg_sync_recv_btn.grid(column=0, row=3)

            self.msg_sync_recv_file = str()
            self.msg_sync_recv_entry = tk.Entry(self.msg_sync_frame, textvariable=self.msg_sync_recv_file)
            self.msg_sync_recv_entry.grid(column=1, row=3, columnspan=3)
            self.msg_sync_recv_entry.insert(0, "receiverrolehandler.cpp")

            self.msg_sync_recv_btn = tk.Button(self.msg_sync_frame, text="选择文件",
                                               command=self.set_msg_sync_recv_file)
            self.msg_sync_recv_btn.grid(column=6, row=3)

        def msg_asnyc(self):
            self.msg_async_frame = tk.Frame(self.master, borderwidth=5, relief="ridge")
            self.msg_async_frame.grid(column=0, row=1, sticky="nsew")
            self.msg_async_frame.rowconfigure(0, weight=1)
            self.msg_async_frame.columnconfigure(0, weight=1)

            self.msg_async_label = tk.Label(self.msg_async_frame, text='消息通讯-异步连接:')
            self.msg_async_label.grid(column=0, row=0, columnspan=5, sticky="nsew")

            self.msg_async_send_h_label = tk.Label(self.msg_async_frame, text='选择发送方h文件:')
            self.msg_async_send_h_label.grid(column=0, row=1)

            self.msg_async_send_h_file = str()
            self.msg_async_send_h_entry = tk.Entry(self.msg_async_frame, textvariable=self.msg_async_send_h_file)
            self.msg_async_send_h_entry.grid(column=1, row=1, columnspan=3)
            self.msg_async_send_h_entry.insert(0, "senderrolehandler.h")

            self.msg_async_send_h_btn = tk.Button(self.msg_async_frame, text="选择文件",
                                                  command=self.set_msg_async_send_h_file)
            self.msg_async_send_h_btn.grid(column=4, row=1)

            self.msg_async_send_cpp_label = tk.Label(self.msg_async_frame, text='选择发送方cpp文件:')
            self.msg_async_send_cpp_label.grid(column=0, row=2)

            self.msg_async_send_cpp_file = str()
            self.msg_async_send_cpp_entry = tk.Entry(self.msg_async_frame, textvariable=self.msg_async_send_cpp_file)
            self.msg_async_send_cpp_entry.grid(column=1, row=2, columnspan=3)
            self.msg_async_send_cpp_entry.insert(0, "senderrolehandler.cpp")

            self.msg_async_send_cpp_btn = tk.Button(self.msg_async_frame, text="选择文件",
                                                    command=self.set_msg_async_send_cpp_file)
            self.msg_async_send_cpp_btn.grid(column=4, row=2)

            self.msg_async_send_xml_label = tk.Label(self.msg_async_frame, text='选择发送方xml文件:')
            self.msg_async_send_xml_label.grid(column=0, row=3)

            self.msg_async_send_xml_file = str()
            self.msg_async_send_xml_entry = tk.Entry(self.msg_async_frame, textvariable=self.msg_async_send_xml_file)
            self.msg_async_send_xml_entry.grid(column=1, row=3, columnspan=3)
            self.msg_async_send_xml_entry.insert(0, "plug.xml")

            self.msg_async_send_xml_btn = tk.Button(self.msg_async_frame, text="选择文件",
                                                    command=self.set_msg_async_send_xml_file)
            self.msg_async_send_xml_btn.grid(column=4, row=3)

            self.msg_async_recv_h_btn = tk.Label(self.msg_async_frame, text="选择接收方h文件")
            self.msg_async_recv_h_btn.grid(column=0, row=4)

            self.msg_async_recv_h_file = str()
            self.msg_async_recv_h_entry = tk.Entry(self.msg_async_frame, textvariable=self.msg_async_recv_h_file)
            self.msg_async_recv_h_entry.grid(column=1, row=4, columnspan=3)
            self.msg_async_recv_h_entry.insert(0, "receiverrolehandler.h")

            self.msg_async_recv_h_btn = tk.Button(self.msg_async_frame, text="选择文件",
                                                  command=self.set_msg_async_recv_h_file)
            self.msg_async_recv_h_btn.grid(column=4, row=4)

            self.msg_async_recv_cpp_btn = tk.Label(self.msg_async_frame, text="选择接收方cpp文件")
            self.msg_async_recv_cpp_btn.grid(column=0, row=5)

            self.msg_async_recv_cpp_file = str()
            self.msg_async_recv_cpp_entry = tk.Entry(self.msg_async_frame, textvariable=self.msg_async_recv_cpp_file)
            self.msg_async_recv_cpp_entry.grid(column=1, row=5, columnspan=3)
            self.msg_async_recv_cpp_entry.insert(0, "receiverrolehandler.cpp")

            self.msg_async_recv_cpp_btn = tk.Button(self.msg_async_frame, text="选择文件",
                                                    command=self.set_msg_async_recv_cpp_file)
            self.msg_async_recv_cpp_btn.grid(column=4, row=5)

            self.msg_async_recv_xml_btn = tk.Label(self.msg_async_frame, text="选择接收方xml文件")
            self.msg_async_recv_xml_btn.grid(column=0, row=6)

            self.msg_async_recv_xml_file = str()
            self.msg_async_recv_xml_entry = tk.Entry(self.msg_async_frame, textvariable=self.msg_async_recv_xml_file)
            self.msg_async_recv_xml_entry.grid(column=1, row=6, columnspan=3)
            self.msg_async_recv_xml_entry.insert(0, "plug.xml")

            self.msg_async_recv_xml_btn = tk.Button(self.msg_async_frame, text="选择文件",
                                                    command=self.set_msg_async_recv_xml_file)
            self.msg_async_recv_xml_btn.grid(column=4, row=6)

        def server_regist(self):
            self.srv_reg_frame = tk.Frame(self.master, borderwidth=5, relief="ridge")
            self.srv_reg_frame.grid(column=0, row=2, sticky="nsew")
            self.srv_reg_frame.rowconfigure(0, weight=1)
            self.srv_reg_frame.columnconfigure(0, weight=1)

            self.srv_reg_label = tk.Label(self.srv_reg_frame, text='服务注册:')
            self.srv_reg_label.grid(column=0, row=0, columnspan=5)

            self.srv_reg_name_label = tk.Label(self.srv_reg_frame, text="选择服务名h文件")
            self.srv_reg_name_label.grid(column=0, row=1)

            self.srv_reg_name_file = str()
            self.srv_reg_name_entry = tk.Entry(self.srv_reg_frame, textvariable=self.srv_reg_name_file)
            self.srv_reg_name_entry.grid(column=1, row=1, columnspan=3)
            self.srv_reg_name_entry.insert(0, "servicename.h")

            self.srv_reg_name_btn = tk.Button(self.srv_reg_frame, text="选择文件",
                                         command=self.set_srv_reg_name_file)
            self.srv_reg_name_btn.grid(column=4, row=1)

            self.srv_reg_classname_label = tk.Label(self.srv_reg_frame, text="选择服务类名h文件")
            self.srv_reg_classname_label.grid(column=0, row=2)

            self.srv_reg_classname_file = str()
            self.srv_reg_classname_entry = tk.Entry(self.srv_reg_frame, textvariable=self.srv_reg_classname_file)
            self.srv_reg_classname_entry.grid(column=1, row=2, columnspan=3)
            self.srv_reg_classname_entry.insert(0, "serviceclassname.h")

            self.srv_reg_classname_btn = tk.Button(self.srv_reg_frame, text="选择文件",
                                         command=self.set_srv_reg_classname_file)
            self.srv_reg_classname_btn.grid(column=4, row=2)

        def server_dll_get(self):
            self.srv_dll_get_frame = tk.Frame(self.master, borderwidth=5, relief="ridge")
            self.srv_dll_get_frame.grid(column=0, row=3, sticky="nsew")
            self.srv_dll_get_frame.rowconfigure(0, weight=1)
            self.srv_dll_get_frame.columnconfigure(0, weight=1)

            self.srv_dll_get_label = tk.Label(self.srv_dll_get_frame, text='dll服务调用:')
            self.srv_dll_get_label.grid(column=0, row=1, columnspan=5)

            self.srv_dll_get_label = tk.Label(self.srv_dll_get_frame, text="选择dll服务调用cpp文件")
            self.srv_dll_get_label.grid(column=0, row=5)

            self.srv_dll_get_file = str()
            self.srv_dll_get_entry = tk.Entry(self.srv_dll_get_frame, textvariable=self.srv_dll_get_file)
            self.srv_dll_get_entry.grid(column=1, row=5, columnspan=3)
            self.srv_dll_get_entry.insert(0, "mypluginclassname.cpp")

            self.srv_dll_get_btn = tk.Button(self.srv_dll_get_frame, text="选择文件",
                                             command=self.set_srv_dll_get_file)
            self.srv_dll_get_btn.grid(column=4, row=5)

        def server_exe_get(self):
            self.srv_exe_get_frame = tk.Frame(self.master, borderwidth=5, relief="ridge")
            self.srv_exe_get_frame.grid(column=0, row=4, sticky="nsew")
            self.srv_exe_get_frame.rowconfigure(0, weight=1)
            self.srv_exe_get_frame.columnconfigure(0, weight=1)

            self.srv_exe_get_label = tk.Label(self.srv_exe_get_frame, text='exe服务调用:')
            self.srv_exe_get_label.grid(column=0, row=1, columnspan=5)

            self.srv_exe_get_label = tk.Label(self.srv_exe_get_frame, text="选择exe服务调用cpp文件")
            self.srv_exe_get_label.grid(column=0, row=5)

            self.srv_exe_get_file = str()
            self.srv_exe_get_entry = tk.Entry(self.srv_exe_get_frame, textvariable=self.srv_exe_get_file)
            self.srv_exe_get_entry.grid(column=1, row=5, columnspan=3)
            self.srv_exe_get_entry.insert(0, "mypluginclassname.cpp")

            self.srv_exe_get_btn = tk.Button(self.srv_exe_get_frame, text="选择文件",
                                             command=self.set_srv_exe_get_file)
            self.srv_exe_get_btn.grid(column=4, row=5)

        def event_sync(self):
            self.event_sync_frame = tk.Frame(self.master, borderwidth=5, relief="ridge")
            self.event_sync_frame.grid(column=0, row=5, sticky="nsew")
            self.event_sync_frame.rowconfigure(0, weight=1)
            self.event_sync_frame.columnconfigure(0, weight=1)

            self.event_sync_label = tk.Label(self.event_sync_frame, text='事件-同步连接:')
            self.event_sync_label.grid(column=0, row=1, columnspan=5)

            self.event_sync_label = tk.Label(self.event_sync_frame, text="选择同步事件cpp文件")
            self.event_sync_label.grid(column=0, row=5)

            self.event_sync_file = str()
            self.event_sync_entry = tk.Entry(self.event_sync_frame, textvariable=self.event_sync_file)
            self.event_sync_entry.grid(column=1, row=5, columnspan=3)
            self.event_sync_entry.insert(0, "eventhandler.cpp")

            self.event_sync_btn = tk.Button(self.event_sync_frame, text="选择文件",
                                             command=self.set_event_sync_file)
            self.event_sync_btn.grid(column=4, row=5)

        def event_async(self):
            self.event_async_frame = tk.Frame(self.master, borderwidth=5, relief="ridge")
            self.event_async_frame.grid(column=0, row=6, sticky="nsew")
            self.event_async_frame.rowconfigure(0, weight=1)
            self.event_async_frame.columnconfigure(0, weight=1)

            self.event_async_label = tk.Label(self.event_async_frame, text='事件-异步连接:')
            self.event_async_label.grid(column=0, row=1, columnspan=5)

            self.event_async_label = tk.Label(self.event_async_frame, text="选择异步事件cpp文件")
            self.event_async_label.grid(column=0, row=5)

            self.event_async_file = str()
            self.event_async_entry = tk.Entry(self.event_async_frame, textvariable=self.event_async_file)
            self.event_async_entry.grid(column=1, row=5, columnspan=3)
            self.event_async_entry.insert(0, "eventhandler.cpp")

            self.event_async_btn = tk.Button(self.event_async_frame, text="选择文件",
                                            command=self.set_event_async_file)
            self.event_async_btn.grid(column=4, row=5)

        def set_msg_sync_send_file(self):
            self.msg_sync_send_file = filedialog.askopenfilename(filetypes=[("cpp files", "*.cpp")])
            if self.msg_sync_send_file:
                self.msg_sync_send_entry.delete(0, tk.END)
                self.msg_sync_send_entry.insert(0, self.msg_sync_send_file)

        def set_msg_sync_recv_file(self):
            self.msg_sync_recv_file = filedialog.askopenfilename(filetypes=[("cpp files", "*.cpp")])
            if self.msg_sync_recv_file:
                self.msg_sync_recv_entry.delete(0, tk.END)
                self.msg_sync_recv_entry.insert(0, self.msg_sync_send_file)

        def set_msg_async_send_h_file(self):
            self.msg_async_send_h_file = filedialog.askopenfilename(filetypes=[("h files", "*.h")])
            if self.msg_async_send_h_file:
                self.msg_async_send_h_entry.delete(0, tk.END)
                self.msg_async_send_h_entry.insert(0, self.msg_async_send_h_file)

        def set_msg_async_send_cpp_file(self):
            self.msg_async_send_cpp_file = filedialog.askopenfilename(filetypes=[("cpp files", "*.cpp")])
            if self.msg_async_send_cpp_file:
                self.msg_async_send_cpp_entry.delete(0, tk.END)
                self.msg_async_send_cpp_entry.insert(0, self.msg_async_send_cpp_file)

        def set_msg_async_send_xml_file(self):
            self.msg_async_send_xml_file = filedialog.askopenfilename(filetypes=[("xml files", "*.xml")])
            if self.msg_async_send_xml_file:
                self.msg_async_send_xml_entry.delete(0, tk.END)
                self.msg_async_send_xml_entry.insert(0, self.msg_async_send_xml_file)

        def set_msg_async_recv_h_file(self):
            self.msg_async_recv_h_file = filedialog.askopenfilename(filetypes=[("h files", "*.h")])
            if self.msg_async_recv_h_file:
                self.msg_async_recv_h_entry.delete(0, tk.END)
                self.msg_async_recv_h_entry.insert(0, self.msg_async_recv_h_file)

        def set_msg_async_recv_cpp_file(self):
            self.msg_async_recv_cpp_file = filedialog.askopenfilename(filetypes=[("cpp files", "*.cpp")])
            if self.msg_async_recv_cpp_file:
                self.msg_async_recv_cpp_entry.delete(0, tk.END)
                self.msg_async_recv_cpp_entry.insert(0, self.msg_async_recv_cpp_file)

        def set_msg_async_recv_xml_file(self):
            self.msg_async_recv_xml_file = filedialog.askopenfilename(filetypes=[("xml files", "*.xml")])
            if self.msg_async_recv_xml_file:
                self.msg_async_recv_xml_entry.delete(0, tk.END)
                self.msg_async_recv_xml_entry.insert(0, self.msg_async_recv_xml_file)

        def set_srv_reg_name_file(self):
            self.srv_reg_name_file = filedialog.askopenfilename(filetypes=[("h files", "*.h")])
            if self.srv_reg_name_file:
                self.srv_reg_name_entry.delete(0, tk.END)
                self.srv_reg_name_entry.insert(0, self.srv_reg_name_file)

        def set_srv_reg_classname_file(self):
            self.srv_reg_classname_file = filedialog.askopenfilename(filetypes=[("h files", "*.h")])
            if self.srv_reg_classname_file:
                self.srv_reg_classname_entry.delete(0, tk.END)
                self.srv_reg_classname_entry.insert(0, self.srv_reg_classname_file)

        def set_srv_dll_get_file(self):
            self.srv_dll_get_file = filedialog.askopenfilename(filetypes=[("cpp files", "*.cpp")])
            if self.srv_dll_get_file:
                self.srv_dll_get_entry.delete(0, tk.END)
                self.srv_dll_get_entry.insert(0, self.srv_dll_get_file)

        def set_srv_exe_get_file(self):
            self.srv_exe_get_file = filedialog.askopenfilename(filetypes=[("cpp files", "*.cpp")])
            if self.srv_exe_get_file:
                self.srv_exe_get_entry.delete(0, tk.END)
                self.srv_exe_get_entry.insert(0, self.srv_exe_get_file)

        def set_event_sync_file(self):
            self.event_sync_file = filedialog.askopenfilename(filetypes=[("cpp files", "*.cpp")])
            if self.event_sync_file:
                self.event_sync_entry.delete(0, tk.END)
                self.event_sync_entry.insert(0, self.event_sync_file)

        def set_event_async_file(self):
            self.event_async_file = filedialog.askopenfilename(filetypes=[("cpp files", "*.cpp")])
            if self.event_async_file:
                self.event_async_entry.delete(0, tk.END)
                self.event_async_entry.insert(0, self.event_async_file)

        def on_finish(self):
            modify = ModifyFile()
            error = None

            try:
                if self.msg_sync_send_file and self.msg_sync_topic:
                    modify.modify_msgadmin_sync_sender_cpp_v1(self.msg_sync_send_file, self.msg_sync_topic)
            except IOError as e:
                error += str(e)

            try:
                if self.msg_sync_recv_file:
                    modify.modify_msgadmin_sync_recevier_cpp_v1(self.msg_sync_recv_file)
            except IOError as e:
                error += str(e)

            try:
                if self.msg_async_send_h_file:
                    modify.modify_msgadmin_async_sender_h_v1(self.msg_async_send_h_file)
            except IOError as e:
                error += str(e)

            try:
                if self.msg_async_send_cpp_file:
                    modify.modify_msgadmin_sync_sender_cpp_v1(self.msg_async_send_cpp_file)
            except IOError as e:
                error += str(e)

            try:
                if self.msg_async_send_xml_file:
                    modify.modify_msgadmin_async_sender_xml_v1(self.msg_async_send_xml_file)
            except IOError as e:
                error += str(e)

            try:
                if self.msg_async_recv_h_file:
                    modify.modify_msgadmin_async_recevier_h_v1(self.msg_async_recv_h_file)
            except IOError as e:
                error += str(e)

            try:
                if self.msg_async_recv_cpp_file:
                    modify.modify_msgadmin_async_recevier_cpp_v1(self.msg_async_recv_cpp_file)
            except IOError as e:
                error += str(e)

            try:
                if self.msg_async_recv_xml_file:
                    modify.modify_msgadmin_async_recevier_xml_v1(self.msg_async_recv_xml_file)
            except IOError as e:
                error += str(e)

            try:
                if self.srv_reg_name_file:
                    modify.modify_servicename_h(self.srv_reg_name_file)
            except IOError as e:
                error += str(e)

            try:
                if self.srv_reg_classname_file:
                    modify.modify_serviceclassname_h(self.srv_reg_classname_file)
            except IOError as e:
                error += str(e)

            try:
                if self.srv_dll_get_file:
                    modify.modify_dll_getservice_cpp(self.srv_dll_get_file)
            except IOError as e:
                error += str(e)

            try:
                if self.srv_exe_get_file:
                    modify.modify_exe_getservice_cpp(self.srv_exe_get_file)
            except IOError as e:
                error += str(e)

            try:
                if self.event_sync_file:
                    modify.modify_event_sync_cpp(self.event_sync_file)
            except IOError as e:
                error += str(e)

            try:
                if self.event_async_file:
                    modify.modify_event_async_cpp(self.event_async_file)
            except IOError as e:
                error += str(e)

            if error:
                print(error)
                messagebox.showinfo(message='生成文件失败，' + error)
            else:
                messagebox.showinfo(message='生成文件成功')

    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
