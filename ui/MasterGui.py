#!/usr/bin/python

##############################################################################
##
## File: MasterGui.py
## Authors: James Kuczynski <jkuczyns@cs.uml.edu>
##          Joshua Rodriguez <jrodrigu@cs.uml.edu>
## File Description: This file contains the main control code for the
##                   frontend.
##
## Created: 11/07/2016 by J.K.
## Last Modified: 11/19/2016 by J.K.
##
##############################################################################

import sys

# Import QT modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Import local files
import StartGui
import RecordGui
import PremadeRecGui
import PlayGui
import HelpGui

# Enumeration type for swapping between "pages"
class Page:
    START_GUI, RECORD_GUI, PREMADE_RECORD_GUI, PLAY_GUI = range(4)


"""
"
"
"""
class MasterGui(QWidget):
    """
    " Constructor
    """
    def __init__(self):
        super(MasterGui, self).__init__()
        self.page = Page.START_GUI
        self.initUi()

    """
    " Initializes the UI elements
    """
    def initUi(self):
        self.startGui = StartGui.StartGui()
        self.recordGui = RecordGui.RecordGui()
        self.premadeRecGui = PremadeRecGui.PremadeRecGui()
        self.playGui = PlayGui.PlayGui()
        self.helpGui = HelpGui.HelpGui('css/damascus_steel.css') #damascus_steel.css
        self.pages = [self.startGui, self.recordGui, self.premadeRecGui, self.playGui]

        self.backBtn = QPushButton("<Back")
        self.backBtn.clicked.connect(self.backBtnSlot)
        self.nextBtn = QPushButton("next>")
        self.nextBtn.clicked.connect(self.nextBtnSlot)
        self.finishBtn = QPushButton("Finish")
        self.finishBtn.clicked.connect(self.finishBtnSlot)
        self.cancelBtn = QPushButton("Cancel")
        self.cancelBtn.clicked.connect(self.cancelBtnSlot)
        self.helpBtn = QPushButton("Help")
        self.helpBtn.clicked.connect(self.helpBtnSlot)


        self.btnLayout = QHBoxLayout()
        self.btnLayout.addWidget(self.backBtn)
        self.btnLayout.addWidget(self.nextBtn)
        self.btnLayout.addWidget(self.finishBtn)
        self.btnLayout.addWidget(self.cancelBtn)
        self.btnLayout.addWidget(self.helpBtn)

        self.backBtn.setEnabled(False)
        self.finishBtn.setEnabled(False)

        self.outerLayout = QGridLayout()
        self.outerLayout.addWidget(self.startGui, 0, 0, Qt.AlignCenter)
        self.outerLayout.addLayout(self.btnLayout, 1, 0, Qt.AlignRight)

        style = open('css/damascus_steel.css').read() # damascus_steel.css
        self.setStyleSheet(style)

        self.move(800, 400)
        self.resize(500, 400)
        self.setWindowTitle('Calculator')

        self.setLayout(self.outerLayout)


    """
    " The back button is pressed.
    """
    def backBtnSlot(self):

        print "back; current page:", self.page
        if self.page == Page.RECORD_GUI:
            self.unloadPage(1)
            self.loadPage(0)
            self.page = Page.START_GUI
        elif self.page == Page.PREMADE_RECORD_GUI:
            self.unloadPage(2)
            self.loadPage(0)
            self.page = Page.START_GUI
        elif self.page == Page.PLAY_GUI:
            self.unloadPage(3)
            self.loadPage(0)
            self.nextBtn.setEnabled(True)
            self.page = Page.START_GUI


    """
    " When the "next" button is pressed, this function is triggered.  It
    " unloads the previous UI and loads the next one.
    """
    def nextBtnSlot(self):
        #
        if self.page == Page.START_GUI:
            if self.startGui.btnGroup.checkedId() == 0:
                print "next..."
                self.unloadPage(0)
                self.loadPage(1)
                self.backBtn.setEnabled(True)
                self.finishBtn.setEnabled(True) # TODO: this should ONLY get enabled after the audio has been recorded!
                self.page = Page.RECORD_GUI
            elif self.startGui.btnGroup.checkedId() == 1:
                self.unloadPage(0)
                self.loadPage(2)
                self.backBtn.setEnabled(True)
                self.finishBtn.setEnabled(True)
                self.page = Page.PREMADE_RECORD_GUI
        elif self.page == Page.RECORD_GUI:
            self.unloadPage(1)
            self.loadPage(3)
            self.nextBtn.setEnabled(False)
            self.finishBtn.setEnabled(False)
            self.page = Page.PLAY_GUI
        elif self.page == Page.PREMADE_RECORD_GUI:
            self.unloadPage(2)
            self.loadPage(3)
            self.nextBtn.setEnabled(False)
            self.finishBtn.setEnabled(False)
            self.page = Page.PLAY_GUI


    """
    " The Finish button is pressed.
    """
    def finishBtnSlot(self):
        print "finish triggered"


    """
    " The Cancel button is pressed.
    """
    def cancelBtnSlot(self):
        print "cancel triggered--bye!"
        exit()


    """
    " The Help button is pressed.
    """
    def helpBtnSlot(self):
        print "help triggered"
        self.helpGui.show()


    """
    " Loads a page into the container UI.
    """
    def loadPage(self, idx):
        self.outerLayout.addWidget(self.pages[idx], 0, 0, Qt.AlignCenter)
        self.pages[idx].setVisible(True)
        self.pages[idx].setEnabled(True)


    """
    " Unloads a page currently in the container UI.
    """
    def unloadPage(self, idx):
        self.outerLayout.removeWidget(self.pages[idx])
        self.pages[idx].setVisible(False)
        self.pages[idx].setEnabled(False)

