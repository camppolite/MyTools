# -*- coding: utf-8 -*-

# Copyright 2018 Wudr. All Rights Reserved.
#
#
# https://github.com/camppolite/ECW.git
# ==============================================================================

from PyQt5.QtWidgets import QApplication
import sys

from qwizarddialog import QWizardDialog

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ECW_Wizard = QWizardDialog()
    ECW_Wizard.resize(600, 550)
    sys.exit(app.exec_())
