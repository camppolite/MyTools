# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tcpclient.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_tcpclient_Dialog(object):
    def setupUi(self, tcpclient_Dialog):
        tcpclient_Dialog.setObjectName("tcpclient_Dialog")
        tcpclient_Dialog.resize(960, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tcpclient_Dialog.sizePolicy().hasHeightForWidth())
        tcpclient_Dialog.setSizePolicy(sizePolicy)
        self.label = QtWidgets.QLabel(tcpclient_Dialog)
        self.label.setGeometry(QtCore.QRect(10, 9, 111, 16))
        self.label.setObjectName("label")
        self.LEdit_ipaddr = QtWidgets.QLineEdit(tcpclient_Dialog)
        self.LEdit_ipaddr.setGeometry(QtCore.QRect(50, 40, 133, 20))
        self.LEdit_ipaddr.setObjectName("LEdit_ipaddr")
        self.label_3 = QtWidgets.QLabel(tcpclient_Dialog)
        self.label_3.setGeometry(QtCore.QRect(8, 70, 36, 16))
        self.label_3.setObjectName("label_3")
        self.pBtn_connserv = QtWidgets.QPushButton(tcpclient_Dialog)
        self.pBtn_connserv.setGeometry(QtCore.QRect(190, 30, 61, 31))
        self.pBtn_connserv.setObjectName("pBtn_connserv")
        self.pBtn_send = QtWidgets.QPushButton(tcpclient_Dialog)
        self.pBtn_send.setGeometry(QtCore.QRect(450, 150, 51, 31))
        self.pBtn_send.setObjectName("pBtn_send")
        self.label_4 = QtWidgets.QLabel(tcpclient_Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(tcpclient_Dialog)
        self.label_2.setGeometry(QtCore.QRect(8, 40, 36, 16))
        self.label_2.setObjectName("label_2")
        self.LEdit_port = QtWidgets.QLineEdit(tcpclient_Dialog)
        self.LEdit_port.setGeometry(QtCore.QRect(50, 70, 133, 20))
        self.LEdit_port.setObjectName("LEdit_port")
        self.lab_connstatu = QtWidgets.QLabel(tcpclient_Dialog)
        self.lab_connstatu.setGeometry(QtCore.QRect(10, 100, 171, 16))
        self.lab_connstatu.setText("")
        self.lab_connstatu.setObjectName("lab_connstatu")
        self.pBtn_break = QtWidgets.QPushButton(tcpclient_Dialog)
        self.pBtn_break.setGeometry(QtCore.QRect(190, 70, 61, 31))
        self.pBtn_break.setObjectName("pBtn_break")
        self.label_5 = QtWidgets.QLabel(tcpclient_Dialog)
        self.label_5.setGeometry(QtCore.QRect(510, 120, 201, 16))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(tcpclient_Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 140, 431, 651))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(tcpclient_Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(510, 140, 431, 651))
        self.textBrowser.setObjectName("textBrowser")
        self.label_8 = QtWidgets.QLabel(tcpclient_Dialog)
        self.label_8.setGeometry(QtCore.QRect(260, 30, 281, 51))
        self.label_8.setObjectName("label_8")
        self.layoutWidget = QtWidgets.QWidget(tcpclient_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(330, 110, 115, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.LEdit_timeout = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LEdit_timeout.sizePolicy().hasHeightForWidth())
        self.LEdit_timeout.setSizePolicy(sizePolicy)
        self.LEdit_timeout.setMaximumSize(QtCore.QSize(41, 20))
        self.LEdit_timeout.setInputMask("")
        self.LEdit_timeout.setAlignment(QtCore.Qt.AlignCenter)
        self.LEdit_timeout.setObjectName("LEdit_timeout")
        self.horizontalLayout.addWidget(self.LEdit_timeout)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)

        self.retranslateUi(tcpclient_Dialog)
        QtCore.QMetaObject.connectSlotsByName(tcpclient_Dialog)

    def retranslateUi(self, tcpclient_Dialog):
        _translate = QtCore.QCoreApplication.translate
        tcpclient_Dialog.setWindowTitle(_translate("tcpclient_Dialog", "TCP Fake"))
        self.label.setText(_translate("tcpclient_Dialog", "1.连接TCP服务端"))
        self.LEdit_ipaddr.setText(_translate("tcpclient_Dialog", "192.168.1.1"))
        self.label_3.setText(_translate("tcpclient_Dialog", "端口号"))
        self.pBtn_connserv.setText(_translate("tcpclient_Dialog", "连接"))
        self.pBtn_send.setText(_translate("tcpclient_Dialog", "发送"))
        self.label_4.setText(_translate("tcpclient_Dialog", "2.发送消息"))
        self.label_2.setText(_translate("tcpclient_Dialog", "IP地址"))
        self.LEdit_port.setText(_translate("tcpclient_Dialog", "8000"))
        self.pBtn_break.setText(_translate("tcpclient_Dialog", "断开"))
        self.label_5.setText(_translate("tcpclient_Dialog", "3.接收消息(以字符串形式显示)"))
        self.textEdit.setHtml(_translate("tcpclient_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &quot;set&quot;: true,    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &quot;version&quot;: 1,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &quot;param&quot;:    {</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        &quot;band&quot;: 0,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        &quot;rfmode&quot;: 0,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        &quot;hwmode&quot;: ‘b’,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        &quot;htmode&quot;:     20,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        &quot;transmission closed&quot;: 0,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        &quot;changeangle strategy&quot;: {</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot;start&quot;: 0,    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot;end &quot;: 120,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot;step&quot;: 10,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot;channel&quot;: 1,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot;time&quot;: 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        },    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        &quot;changechannel strategy&quot;: {</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot;start&quot;: 1,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot;end&quot;: 14,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot;step&quot;: 1,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot;angle&quot;: 120,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot;time&quot;: 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        },</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        &quot;changeall strategy&quot;:    {</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot;start angle &quot;: 1,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot;end angle &quot;: 14,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot; angle step&quot;: 1,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot; channel step&quot;: 1,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot;start channel&quot;: 1,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot;end  channel&quot;: 13,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot;time&quot;: 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        },</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        &quot;nostrategy&quot;:    {</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot;channel&quot;: 1,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot;angle&quot;: 120</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        }</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">}</p></body></html>"))
        self.label_8.setText(_translate("tcpclient_Dialog", "<html><head/><body><p>使用的是短连接，输入内容直接点击发送即可。</p><p>本地tcp服务端ip为127.0.0.1:9999</p></body></html>"))
        self.label_6.setText(_translate("tcpclient_Dialog", "超时时间"))
        self.LEdit_timeout.setText(_translate("tcpclient_Dialog", "1"))
        self.label_7.setText(_translate("tcpclient_Dialog", "秒"))

