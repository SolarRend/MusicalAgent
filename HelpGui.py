#!/usr/bin/python

##############################################################################
##
## File: HelpGui.py
## Authors: James Kuczynski <jkuczyns@cs.uml.edu>
##          Joshua Rodriguez <jrodrigu@cs.uml.edu>
## File Description: This file implements a help gui popup, triggered if the
##                   user presses the "help" button.
##
##
## Created: 11/10/2016 by J.K.
## Last Modified: 11/19/2016 by J.K.
##
##############################################################################

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class HelpGui(QWidget):
    def __init__(self, stylePath):
        super(HelpGui, self).__init__()
        self.initUi(stylePath)

    """
    " Set up the UI elements.
    """
    def initUi(self, cssFileName):
        self.outerLayout = QGridLayout()

        self.titleLbl = QLabel("Help")
        self.textEdit = QTextEdit()
        self.textEdit.setEnabled(False)

        with open('res/help.txt', 'r') as helpFile:
            self.textEdit.setText(helpFile.read().replace('\n', '') )

        self.outerLayout.addWidget(self.titleLbl, 0, 0, Qt.AlignHCenter | Qt.AlignTop)
        self.outerLayout.addWidget(self.textEdit)

        style = open(cssFileName).read()
        self.setStyleSheet(style)

        self.setLayout(self.outerLayout)
        self.resize(300, 200)