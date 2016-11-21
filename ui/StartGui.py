#!/usr/bin/python

##############################################################################
##
## File: PremadeRecGui.py
## Authors: James Kuczynski <jkuczyns@cs.uml.edu>
##          Joshua Rodriguez <jrodrigu@cs.uml.edu>
## File Description: This file contains the "start page" of the UI.  It
##                   allows the user to choose audio input or to use
##                   pre-recording input.
##
## Created: 11/10/2016 by J.K.
## Last Modified: 11/10/2016 by J.K.
##
##############################################################################

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class StartGui(QWidget):
    def __init__(self):
        super(StartGui, self).__init__()
        self.initUi()

    def initUi(self):
        self.outerLayout = QGridLayout()

        self.newInputRadBtn = QRadioButton("New input")
        self.newInputRadBtn.setChecked(True)
        self.oldInputRadBtn = QRadioButton("Old input")
        self.btnGroup = QButtonGroup()
        self.btnGroup.addButton(self.newInputRadBtn, 0)
        self.btnGroup.addButton(self.oldInputRadBtn, 1)
        self.btnGroupLay = QGridLayout()
        self.btnGroupLay.addWidget(self.newInputRadBtn, 0, 0)
        self.btnGroupLay.addWidget(self.oldInputRadBtn, 1, 0)

        self.outerLayout.addLayout(self.btnGroupLay, 0, 0)

        self.setLayout(self.outerLayout)
