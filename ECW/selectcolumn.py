# -*- coding: utf-8 -*-

# Copyright 2018 Wudr. All Rights Reserved.
#
#
# https://github.com/camppolite/ECW.git
# ==============================================================================

from PyQt5.QtWidgets import QWizardPage, QWidget

from ui_file import ui_selectcolumn
from model1 import Model1
from model2_testinstruction import Model2_TestInstruction
from model2_testreport import Model2_TestReport
from model2_bug import Model2_Bug

class SelectColumn(QWizardPage):
    """向导第二页，用户选择列的页面"""
    def __init__(self):
        super().__init__()
        self.model1 = Model1()
        self.model2_testreport = Model2_TestReport()
        self.model2_testinstruction = Model2_TestInstruction()
        self.model2_bug = Model2_Bug()

        #绑定转换成word页面向导
        self.sltColumn_ui = ui_selectcolumn.Ui_WizardPage()
        self.sltColumn_ui.setupUi(self)

        #绑定模板1
        model1Page = QWidget(self.sltColumn_ui.tab)

        self.model1.model1_ui.setupUi(model1Page)
        self.sltColumn_ui.gridLayout_3.addWidget(model1Page)

        #绑定模板2-测试报告
        model2_testreportPage = QWidget(self.sltColumn_ui.tab_4)

        self.model2_testreport.model2_testreport_ui.setupUi(model2_testreportPage)
        self.sltColumn_ui.gridLayout_5.addWidget(model2_testreportPage)

        #绑定模板2-测试说明
        model2_testinstructionPage = QWidget(self.sltColumn_ui.tab_2)

        self.model2_testinstruction.model2_testinstruction_ui.setupUi(model2_testinstructionPage)
        self.sltColumn_ui.gridLayout_4.addWidget(model2_testinstructionPage)

        #绑定模板2-bug
        model2_bugPage = QWidget(self.sltColumn_ui.tab_5)

        self.model2_bug.model2_bug_ui.setupUi(model2_bugPage)
        self.sltColumn_ui.gridLayout_6.addWidget(model2_bugPage)