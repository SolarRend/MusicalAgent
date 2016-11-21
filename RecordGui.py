#!/usr/bin/python

##############################################################################
##
## File: RecordGui.py
## Authors: James Kuczynski <jkuczyns@cs.uml.edu>
##          Joshua Rodriguez <jrodrigu@cs.uml.edu>
## File Description: This file is the frontend which allows the user to
##                   train the AI with audio input.
##
## Created: 11/10/2016 by J.K.
## Last Modified: 11/10/2016 by J.K.
##
##############################################################################

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class RecordGui(QWidget):
    def __init__(self):
        super(RecordGui, self).__init__()
        self.initUi()

    """
    " Set up the UI elements.
    """
    def initUi(self):
        self.outerLayout = QGridLayout()

        self.recordBtn = QPushButton("Record")
        self.stopBtn = QPushButton("Stop")

        self.recordBtn.clicked.connect(self.recordBtnSlot)
        self.stopBtn.clicked.connect(self.stopBtnSlot)

        self.outerLayout.addWidget(self.recordBtn, 0, 0)
        self.outerLayout.addWidget(self.stopBtn, 0, 1)

        self.setLayout(self.outerLayout)


    """
    " Triggered when the Record button is pressed
    " @#see recordBtn
    """
    def recordBtnSlot(self):
        print "recordBtn was clicked"


    """
    "
    "
    """
    def stopBtnSlot(self):
        print "stop recording"