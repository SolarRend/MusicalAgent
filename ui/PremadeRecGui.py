#!/usr/bin/python

##############################################################################
##
## File: PremadeRecGui.py
## Authors: James Kuczynski <jkuczyns@cs.uml.edu>
##          Joshua Rodriguez <jrodrigu@cs.uml.edu>
## File Description: This file contains options for using pre-made input for
##                   the AI to train on.
##
##
## Created: 11/10/2016 by J.K.
## Last Modified: 11/10/2016 by J.K
##
##############################################################################

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class PremadeRecGui(QWidget):
    def __init__(self):
        super(PremadeRecGui, self).__init__()
        self.initUi()

    """
    " Set up the UI elements.
    """
    def initUi(self):

        keyList = ["A", "A#", "Ab", "B", "B#", "Bb", "C",
                   "C#", "Cb", "D", "D#", "Db", "E", "E#",
                   "Eb", "F", "F#", "Fb", "G", "G#", "Gb"]
        modeList = ["Major", "Natural minor", "Harmonic minor", "Melodic minor"]

        self.keyListWid = QListWidget()
        for key in keyList:
            self.keyListWid.addItem(key)

        self.modeListWid = QListWidget()
        for mode in modeList:
            self.modeListWid.addItem(mode)




        self.outerLayout = QGridLayout()
        self.outerLayout.addWidget(self.keyListWid, 0, 0)
        self.outerLayout.addWidget(self.modeListWid, 0, 1)

        self.setLayout(self.outerLayout)