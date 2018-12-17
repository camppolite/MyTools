#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2018 Wudr. All Rights Reserved.
#
#
# https://github.com/camppolite/MyTools
# ==============================================================================

import socket
import sys
import json
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.QtCore import pyqtSlot, QRegExp, Qt
from PyQt5.QtGui import QIntValidator, QSyntaxHighlighter, QCursor, QTextCharFormat, QFont, QColor
from ui_tcpclient import Ui_tcpclient_Dialog


class TCPClient(QDialog):

    def __init__(self):
        super().__init__()

        self.ui_tcpcli = Ui_tcpclient_Dialog()
        self.ui_tcpcli.setupUi(self)
        self.ui_tcpcli.pBtn_break.setDisabled(True)
        self.ui_tcpcli.pBtn_connserv.setDisabled(True)
        self.ui_tcpcli.LEdit_timeout.setValidator(QIntValidator(0, 10000, self))  # 为输入设置整数限制
        self.sock = None
        self.highlighter = PythonHighlighter(self.ui_tcpcli.textEdit.document())  # 设置关键字高亮显示"
        self.bindsignal()  # 绑定信号槽

    def bindsignal(self):
        """绑定信号槽"""
        self.ui_tcpcli.pBtn_connserv.clicked.connect(self.connecttcpserver)
        self.ui_tcpcli.pBtn_break.clicked.connect(self.shutdowntcp)
        self.ui_tcpcli.pBtn_send.clicked.connect(self.sendmessage)

    @pyqtSlot()
    def connecttcpserver(self):
        """连接TCP服务端,目前没有什么用途"""
        self.ui_tcpcli.lab_connstatu.setText("连接服务端...")
        host = self.ui_tcpcli.LEdit_ipaddr.text()
        prot = self.ui_tcpcli.LEdit_port.text()
        address = (host, int(prot))
        # Create a socket (SOCK_STREAM means a TCP socket)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置超时时间，以秒为单位
        self.sock.settimeout(10)
        try:
            self.sock.connect(address)
            self.ui_tcpcli.lab_connstatu.setText("已连接...")
            self.ui_tcpcli.pBtn_connserv.setDisabled(True)
            self.ui_tcpcli.pBtn_break.setDisabled(False)
            self.ui_tcpcli.pBtn_break.setFocus()
        except socket.timeout as e:
            m_box = QMessageBox(parent=self)
            m_box.setWindowTitle("提示")
            m_box.setText("连接：" + str(e))
            m_box.exec_()
            return

        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()

    @pyqtSlot()
    def shutdowntcp(self):
        """
        使用shutdown来关闭socket的功能
        SHUT_RDWR：关闭读写，即不能使用send/write/recv/read等
        SHUT_RD：关闭读，即不能使用read/recv等
        SHUT_WR:关闭写功能，即不能使用send/write等
        除此之外，还将缓冲区中的内容清空
        """
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()

        self.ui_tcpcli.lab_connstatu.clear()
        self.ui_tcpcli.pBtn_break.setDisabled(True)
        self.ui_tcpcli.pBtn_connserv.setDisabled(False)
        self.ui_tcpcli.pBtn_connserv.setFocus()

    @pyqtSlot()
    def sendmessage(self):
        """发送TCP消息"""
        data = self.ui_tcpcli.textEdit.toPlainText()
        if not data:
            return
        # 将 Python 对象编码成 JSON 字符串
        data = json.dumps(data, ensure_ascii=False)

        timeout = self.ui_tcpcli.LEdit_timeout.text()
        host = self.ui_tcpcli.LEdit_ipaddr.text()
        prot = self.ui_tcpcli.LEdit_port.text()
        address = (host, int(prot))
        # Create a socket (SOCK_STREAM means a TCP socket)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置连接超时时间，以秒为单位
        self.sock.settimeout(10)
        try:
            self.sock.connect(address)
        except (Exception, socket.timeout) as e:
            m_box = QMessageBox(parent=self)
            m_box.setWindowTitle("提示")
            m_box.setText("连接：" + str(e))
            m_box.exec_()
            return
        try:
            # 设置超时时间，以秒为单位
            self.sock.settimeout(int(timeout))
            self.sock.sendall(bytes(data, "utf-8"))
            # Receive data from the server and shut down
            received = str(self.sock.recv(1024), "utf-8")
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
            # 在控件上显示服务器返回的消息
            self.ui_tcpcli.textBrowser.setText(received)
        except (Exception, socket.timeout) as e:
            m_box = QMessageBox(parent=self)
            m_box.setWindowTitle("提示")
            m_box.setText("接收：" + str(e))
            m_box.exec_()
            return


class PythonHighlighter(QSyntaxHighlighter):
    """设置关键字高亮显示"""
    Rules = []
    Formats = {}

    def __init__(self, parent=None):
        super(PythonHighlighter, self).__init__(parent)

        self.initializeFormats()

        KEYWORDS = ["set", "version", "param", "band", "rfmode","hwmode", "htmode", "transmission closed",
                    "changeangle strategy", "start", "end","step", "channel", "time", "changechannel strategy",
                    "angle", "changeall strategy","start angle", "end angle", "angle step", "channel step",
                    "start channel", "end channel", "nostrategy"]

        CONSTANTS = ["false", "true", "null"]

        PythonHighlighter.Rules.append((QRegExp(
            "|".join([r"\b%s\b" % keyword for keyword in KEYWORDS])),
                                        "keyword"))
        PythonHighlighter.Rules.append((QRegExp(
            "|".join([r"\b%s\b" % constant for constant in CONSTANTS])),
                                        "constant"))
        PythonHighlighter.Rules.append((QRegExp(
            r"\b[+-]?[0-9]+[lL]?\b"
            r"|\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b"
            r"|\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b"),
            "number"))

    @staticmethod
    def initializeFormats():
        baseFormat = QTextCharFormat()
        baseFormat.setFontFamily("courier")
        baseFormat.setFontPointSize(12)
        for name, color in (("normal", Qt.black), ("keyword", Qt.darkBlue), ("constant", Qt.darkGreen),
                            ("number", Qt.darkMagenta), ("error", Qt.darkRed)):
            format = QTextCharFormat(baseFormat)
            format.setForeground(QColor(color))
            if name == "keyword":
                format.setFontWeight(QFont.Bold)
            if name == "comment":
                format.setFontItalic(True)
            PythonHighlighter.Formats[name] = format

    def highlightBlock(self, text):
        NORMAL, ERROR = range(2)

        textLength = len(text)
        prevState = self.previousBlockState()

        self.setFormat(0, textLength,
                       PythonHighlighter.Formats["normal"])

        if text.startswith("Traceback") or text.startswith("Error: "):
            self.setCurrentBlockState(ERROR)
            self.setFormat(0, textLength,
                           PythonHighlighter.Formats["error"])
            return
        if (prevState == ERROR and
            not (text.startswith(sys.ps1) or text.startswith("#"))):
            self.setCurrentBlockState(ERROR)
            self.setFormat(0, textLength,
                           PythonHighlighter.Formats["error"])
            return

        for regex, format in PythonHighlighter.Rules:
            i = regex.indexIn(text)
            while i >= 0:
                length = regex.matchedLength()
                self.setFormat(i, length,
                               PythonHighlighter.Formats[format])
                i = regex.indexIn(text, i + length)

        self.setCurrentBlockState(NORMAL)

    def rehighlight(self):
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        QSyntaxHighlighter.rehighlight(self)
        QApplication.restoreOverrideCursor()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tcpcli = TCPClient()
    tcpcli.show()
    sys.exit(app.exec_())
