# -*- coding: utf-8 -*-

# Copyright 2018 Wudr. All Rights Reserved.
#
#
# https://github.com/camppolite/ECW.git
# ==============================================================================

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWizard, QFileDialog, QPushButton, QVBoxLayout, QRadioButton

import sip, os.path
import xlrd

from selectexcel import SelectExcel
from selectcolumn import SelectColumn


class QWizardDialog(QWizard):
    '''向导控制中心，用户的操作都在这里进行解析和判断'''
    def __init__(self):
        super().__init__()
        self.FirstRow = []
        self.radioBoxs = []
        self.excel = []
        self.targetWord = []

        self.vbox = QVBoxLayout()
        self.initUI()
        self.BindSignal()

    def initUI(self):
        """初始化UI界面"""
        self.slt_excel = SelectExcel()
        self.slt_column = SelectColumn()

        self.slt_excel.sltExcel_ui.groupBox_workbook.setLayout(self.vbox)

        self.btnNext = QPushButton("Next")
        self.btnFinish = QPushButton("Finish")
        self.btnRestart = QPushButton("Restart")

        self.setPage(0, self.slt_excel)   #添加选择excel页面到向导
        self.setPage(1, self.slt_column)    #添加转换成word页面到向导

        self.setButton(self.CustomButton1, self.btnNext)
        self.setButton(self.CustomButton2, self.btnFinish)
        self.setButton(self.CustomButton3, self.btnRestart)

        self.setButtonText(self.BackButton, "上一步")
        self.setButtonText(self.CustomButton1, "下一步")
        self.setButtonText(self.CancelButton, "取消")
        self.setButtonText(self.CustomButton2, "完成")
        self.setButtonText(self.CustomButton3, "重新开始")

        self.layout = [self.Stretch, self.BackButton, self.CustomButton1,
                  self.CustomButton2, self.CustomButton3, self.CancelButton]
        self.setButtonLayout(self.layout)

        self.btnNext.setEnabled(False)
        self.btnFinish.setVisible(False)
        self.btnRestart.setVisible(False)

        self.setWindowTitle("Excel Convert Word")
        self.setWizardStyle(QWizard.ModernStyle)
        self.show()

    def BindSignal(self):
        """绑定信号槽"""
        self.currentIdChanged.connect(self.onCurrentIdChanged)
        self.btnNext.clicked.connect(self.next)
        self.btnFinish.clicked.connect(self.onFinished)
        self.btnRestart.clicked.connect(self.onRestarted)
        self.slt_excel.sltExcel_ui.pBtnChoosePath.clicked.connect(self.on_pBtnChoosePath_clicked)
        #当用户手动修改文件路径时触发该信号
        self.slt_excel.sltExcel_ui.lePath.textChanged.connect(self.on_FileName_Changed)

    @pyqtSlot()
    def on_pBtnChoosePath_clicked(self):
        """响应点击选择文件按钮信号"""
        fileDir = QFileDialog.getOpenFileName(self, "选择文件",
                                              self.slt_excel.sltExcel_ui.lePath.text(),
                                              "Excel Files (*.xlsx *.xls)",
                                              options=QFileDialog.DontResolveSymlinks)
        # #fileDir是一个tuple，没有选择文件时为空
        if not fileDir[0]:
            if not self.slt_excel.sltExcel_ui.lePath.text():
                self.slt_excel.sltExcel_ui.labErrTip.setText("请选择文件.")
                self.btnNext.setEnabled(False)
                self.CleanupSheetNames()
                return
        else:
            #保存的目标文件
            (filepath, name_with_exten) = os.path.split(fileDir[0])
            (fielname, extension) = os.path.splitext(name_with_exten)
            self.targetWord = filepath + '/' + fielname + ".docx"

            self.btnNext.setEnabled(True)
            """选择文件完成后，显示文件路径"""
            self.slt_excel.sltExcel_ui.lePath.setText(fileDir[0]) #此操作会触发lePath.textChanged信号

    @pyqtSlot(str)
    def on_FileName_Changed(self, FileName):
        """响应文件路径修改信号"""
        self.btnNext.setEnabled(True)
        self.slt_excel.sltExcel_ui.labErrTip.clear()

        if not self.slt_excel.sltExcel_ui.lePath.text():
            self.btnNext.setEnabled(False)
            self.CleanupSheetNames()
            return

        try:
            #打开excel文件
            self.excel = xlrd.open_workbook(FileName)
            # 获取工作表的全部名称
            names = self.excel.sheet_names()
        except (IOError, NameError, FileNotFoundError) as e:
            self.slt_excel.sltExcel_ui.labErrTip.setText("打开文件失败！！！" + str(e))
            self.btnNext.setEnabled(False)
            self.CleanupSheetNames()
            return

        self.ShowSheetNames(names)

    @pyqtSlot(int)
    def onCurrentIdChanged(self, int):
        """响应向导页面切换信号"""
        if self.slt_column == self.page(int):
            self.btnFinish.setVisible(True)
            self.btnFinish.setEnabled(True)
            btnNext = self.button(self.CustomButton1)
            btnNext.setEnabled(False)
            self.btnFinish.setFocus()

            if not self.radioBoxs:
                return

            """获取用户选择的Sheet"""
            radioBox = []
            for tempbox in self.radioBoxs:
                if tempbox.isChecked():
                    radioBox = tempbox
                    break
            self.ParseFirstRow(radioBox.text())
            #模板1的数据
            self.slt_column.model1.ShowFirstRow(self.FirstRow)
            # 模板2-用例说明的数据
            self.slt_column.model2_testinstruction.ShowFirstRow(self.FirstRow)
            # 模板2-用例报告的数据
            self.slt_column.model2_testreport.ShowFirstRow(self.FirstRow)
            # 模板2-bug的数据
            self.slt_column.model2_bug.ShowFirstRow(self.FirstRow)

        else:
            self.btnFinish.setVisible(False)

    @pyqtSlot()
    def onFinished(self):
        """响应点击完成按钮信号"""
        self.btnFinish.setEnabled(False)
        btnBack = self.button(self.BackButton)
        btnCancel = self.button(self.CancelButton)
        btnBack.setEnabled(False)
        btnCancel.setEnabled(False)

        tab_index = self.slt_column.sltColumn_ui.tabWidget.currentIndex()
        switcher = {
            # 模板1的数据
            0: "self.slt_column.model1.CreateWord(self.targetWord)",
            # 模板2-用例说明的数据
            1: "self.slt_column.model2_testinstruction.CreateWord(self.targetWord)",
            # 模板2-用例报告的数据
            2: "self.slt_column.model2_testreport.CreateWord(self.targetWord)",
            # 模板2-bug的数据
            3: "self.slt_column.model2_bug.CreateWord(self.targetWord)",

            4: "None",
        }
        eval(switcher.get(tab_index))

        self.btnRestart.setVisible(True)
        self.btnRestart.setFocus()

        btnCancel.setEnabled(True)
        btnCancel.setText("关闭")

    @pyqtSlot()
    def onRestarted(self):
        """响应点击重新开始信号"""
        self.restart()

        self.slt_excel.sltExcel_ui.lePath.clear()
        self.setButtonLayout(self.layout)

        self.btnNext.setEnabled(False)
        self.btnFinish.setVisible(False)
        self.btnRestart.setVisible(False)

    def CleanupSheetNames(self):
        """删除QVBoxLayout()布局的控件"""
         #删除QVBoxLayout()布局的控件
        for r_box in self.radioBoxs:
            self.vbox.removeWidget(r_box)
            sip.delete(r_box)
        self.radioBoxs.clear()

    def ShowSheetNames(self, SheetNames):
        """将可以选择的Sheet显示出来"""

        self.CleanupSheetNames()

        #将工作表显示在页面上并保存到列表里
        for name in SheetNames:
            rdo_Box = QRadioButton(name)
            self.vbox.addWidget(rdo_Box)
            self.radioBoxs.append(rdo_Box)

        #默认选择第一个工作表
        self.radioBoxs[0].setChecked(True)

    def ParseFirstRow(self, SheetName):
        """解析工作表的第一行有效行，作为可选择列"""
        # 获取工作表
        table = self.excel.sheet_by_name(SheetName)

        firstRow = 0
        # 过滤excel开头的空白行
        for r in range(table.nrows):
            if (table.cell_value(r, 0) == ''):
                Empty = True
                for c in range(table.ncols):
                    if (table.cell_value(r, c) != ''):
                        firstRow = r
                        Empty = False
                        break
                if Empty == False:
                    break
            else:
                firstRow = r
                break

        self.FirstRow.clear()
        # 保存第一行有效数据
        for cell in table.row(firstRow):
            self.FirstRow.append(cell.value)
        #模板1的用例数据
        self.slt_column.model1.Cases.clear()
        #模板2-用例说明的用例数据
        self.slt_column.model2_testinstruction.Cases.clear()
        #模板2-用例报告的用例数据
        self.slt_column.model2_testreport.Cases.clear()
        #模板2-bug的数据
        self.slt_column.model2_bug.Cases.clear()
        #提取Cases并保存
        for r_index in range(firstRow+1, table.nrows):
            temp = []
            for c_index in range(table.ncols):
                temp.append(str(table.cell_value(r_index, c_index)))
            self.slt_column.model1.Cases.append(temp)
            self.slt_column.model2_testreport.Cases.append(temp)
            self.slt_column.model2_testinstruction.Cases.append(temp)
            self.slt_column.model2_bug.Cases.append(temp)