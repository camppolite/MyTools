# -*- coding: utf-8 -*-

# Copyright 2018 Wudr. All Rights Reserved.
#
#
# https://github.com/camppolite/ECW.git
# ==============================================================================

from PyQt5.QtWidgets import QWizardPage

from ui_file import ui_selectexcel

class SelectExcel(QWizardPage):
    '''向导第一页，提示用户选择文件，根据用户输入的Excel文件，解析文件的工作表'''
    def __init__(self):
        super().__init__()

        self.sltExcel_ui = ui_selectexcel.Ui_WizardPage()
        self.sltExcel_ui.setupUi(self)