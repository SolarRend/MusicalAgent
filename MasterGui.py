#!/usr/bin/python

##############################################################################
##
## File: MasterGui.py
## Authors: James Kuczynski <jkuczyns@cs.uml.edu>
##          Joshua Rodriguez <jrodrig1@cs.uml.edu>
## File Description: This file contains the main control code for the
##                   frontend.
##
## Created: 11/07/2016 by J.K.
## Last Modified: 11/19/2016 by J.K.
##
##############################################################################

import sys
import random
import time

# Import QT modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Import local files
import StartGui
import RecordGui
import PremadeRecGui
import PlayGui
import HelpGui

import Learning

# Enumeration type for swapping between "pages"
class Page:
    START_GUI, RECORD_GUI, PREMADE_RECORD_GUI, PLAY_GUI = range(4)


"""
" This class contains the outermost widget/window of the user interface.
"
"""
class MasterGui(QWidget):
    """
    " Constructor
    """
    def __init__(self):
        super(MasterGui, self).__init__()
        self.page = Page.START_GUI
        self.counter = 0
        self.initUi()

    """
    " Initializes the UI elements
    """
    def initUi(self):

        # create the widgets
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
        self.finishBtn = QPushButton("Train")
        self.finishBtn.clicked.connect(self.finishBtnSlot)
        self.cancelBtn = QPushButton("Cancel")
        self.cancelBtn.clicked.connect(self.cancelBtnSlot)
        self.helpBtn = QPushButton("Help")
        self.helpBtn.clicked.connect(self.helpBtnSlot)

        # add back, next, finish, cancel, help to a separate layout
        self.btnLayout = QHBoxLayout()
        self.btnLayout.addWidget(self.backBtn)
        self.btnLayout.addWidget(self.nextBtn)
        self.btnLayout.addWidget(self.finishBtn)
        self.btnLayout.addWidget(self.cancelBtn)
        self.btnLayout.addWidget(self.helpBtn)

        # initially, the user cannot go back or finish
        self.backBtn.setEnabled(False)
        self.finishBtn.setEnabled(False)

        self.outerLayout = QGridLayout()
        self.outerLayout.addWidget(self.startGui, 0, 0, Qt.AlignCenter)
        self.outerLayout.addLayout(self.btnLayout, 1, 0, Qt.AlignRight)

        # load the style file
        style = open('css/damascus_steel.css').read() # damascus_steel.css
        self.setStyleSheet(style)

        # window orientation/resizing, etc.
        self.move(800, 400)
        self.resize(500, 400)
        self.setWindowTitle('Xavier - The Musical Agent')

        self.setLayout(self.outerLayout)


    """
    " The back button is pressed.
    """
    def backBtnSlot(self):

        print "back; current page:", self.page

        # enable the back button to unload/load pages
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
            self.nextBtn.setEnabled(True)
            self.finishBtn.setEnabled(True)
            self.page = Page.PLAY_GUI

            self.playGui.truthNotesLe.setText(self.recordGui.heardInput.text())

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
        if self.counter >= 7:
            return

        try:

            # scale = ["C", "D", "E", "F", "G", "A", "B"]#listen()
            # scale = ["C", "E", "G", "B", "D", "F", "A"]
            #scale = ["E", "F#", "G#", "A", "B", "C#", "D#"]  # E Major
            if self.counter == 0:
                scale = self.recordGui.scale
                self.xavier = Learning.Learning(scale)

            # learning for 2k iterations
            for x in range(250):
                if x > 0 and x < 30 and self.counter == 0:
                    self.xavier.qLearn(True, 0.05)
                elif x % 250 == 0 and self.counter != 0:
                    if random.random() > 0.5:
                        self.xavier.qLearn(True, 0.07)
                    else:
                        self.xavier.qLearn(True, 0.1)
                else:
                    self.xavier.qLearn(False, None)
                #print "x=", x
            # agent is done learning
            self.playGui.aiNotesLe.setText(self.playGui.aiNotesLe.text() + self.xavier.goalScale[self.counter] + " ")
            self.counter += 1

        except KeyboardInterrupt:
            Learning.World.global_player.destroy()

        if self.counter == 7:
            self.playGui.trainingLbl.setStyleSheet("QLabel{ background-color: green; }")
            self.playGui.trainingLbl.setText("Ready")
            self.playGui.playBtn.setVisible(True)
            self.playGui.playBtn.setEnabled(True)

            self.xavier.createExplorationQvalues()
            self.playGui.xavier = self.xavier

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

