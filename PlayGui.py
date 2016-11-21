#!/usr/bin/python

##############################################################################
##
## File: PremadeRecGui.py
## Authors: James Kuczynski <jkuczyns@cs.uml.edu>
##          Joshua Rodriguez <jrodrigu@cs.uml.edu>
## File Description: This file allows the user to watch the robot learning,
##                   and customize different parameters during and after
##                   it is learning.
##
## Created: 11/10/2016 by J.K.
## Last Modified: 11/10/2016 by J.K
##
##############################################################################

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


"""
"
"
"""
class PlayGui(QWidget):
    """
    " Constructor
    """
    def __init__(self):
        super(PlayGui, self).__init__()
        self.truthNotesStr = ""
        self.aiNotesStr = ""
        self.initUi()

    """
    " Initializes the UI elements
    """
    def initUi(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        ####################################################
        self.sliderLay = QGridLayout()

        self.tempoLbl = QLabel("Tempo")
        self.exploreLbl = QLabel("Exploration")
        self.volumeLbl = QLabel("Volume")

        self.tempoSlider = QSlider(Qt.Horizontal)
        self.tempoSlider.setMinimum(1)
        self.tempoSlider.setMaximum(50)
        self.tempoSlider.setValue(10)
        self.tempoSlider.setTickPosition(QSlider.TicksBelow)
        self.tempoSlider.setTickInterval(5)

        self.exploreSlider = QSlider(Qt.Horizontal)
        self.exploreSlider.setMinimum(0)
        self.exploreSlider.setMaximum(10)
        self.exploreSlider.setValue(0)
        self.exploreSlider.setTickPosition(QSlider.TicksBelow)
        self.exploreSlider.setTickInterval(1)

        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setMinimum(0)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(50)
        self.volumeSlider.setTickPosition(QSlider.TicksBelow)
        self.volumeSlider.setTickInterval(10)

        self.voicesLbl = QLabel("Voices")
        self.voicesSpinBox = QSpinBox()
        self.voicesSpinBox.setMinimum(1)
        self.voicesSpinBox.setMaximum(3)

        self.accompanimentLbl = QLabel("Accompaniment")
        self.accompanimentCb = QCheckBox()


        self.sliderLay.addWidget(self.tempoLbl, 0, 0, Qt.AlignLeft)
        self.sliderLay.addWidget(self.tempoSlider, 0, 1)
        self.sliderLay.addWidget(self.exploreLbl, 1, 0, Qt.AlignLeft)
        self.sliderLay.addWidget(self.exploreSlider, 1, 1)
        self.sliderLay.addWidget(self.volumeLbl, 2, 0, Qt.AlignLeft)
        self.sliderLay.addWidget(self.volumeSlider, 2, 1)
        self.sliderLay.addWidget(self.voicesLbl, 3, 0)
        self.sliderLay.addWidget(self.voicesSpinBox, 3, 1)
        self.sliderLay.addWidget(self.accompanimentLbl, 4, 0)
        self.sliderLay.addWidget(self.accompanimentCb, 4, 1)
        ####################################################



        ####################################################
        self.notesLayout = QGridLayout()

        self.trainingLbl = QLabel("Training...")
        self.trainingLbl.setStyleSheet("QLabel{ background-color: red; }")

        self.truthNotesLbl = QLabel("Scale")
        self.aiNotesLbl = QLabel("AI Output")

        self.truthNotesLe = QLineEdit()
        self.truthNotesLe.setDragEnabled(True)

        self.aiNotesLe = QLineEdit()
        self.aiNotesLe.setDragEnabled(True)

        self.notesLayout.addWidget(self.truthNotesLbl, 0, 0, Qt.AlignHCenter)
        self.notesLayout.addWidget(self.truthNotesLe, 1, 0, Qt.AlignVCenter)
        self.notesLayout.addWidget(self.aiNotesLe, 2, 0, Qt.AlignVCenter)
        self.notesLayout.addWidget(self.aiNotesLbl, 3, 0, Qt.AlignHCenter)
        self.notesLayout.addWidget(self.trainingLbl, 2, 1)
        ####################################################

        #self.grid.addWidget(self.recordBtn, 0, 0)
        #self.grid.addWidget(self.tempoSlider, 1, 0)
        #self.grid.addWidget(self.exploreSlider, 2, 0)
        #self.grid.addWidget(self.volumeSlider, 3, 0)
        #self.grid.addWidget(self.truthNotesLe, 4, 0)
        #self.grid.addWidget(self.aiNotesLe, 5, 0)
        self.grid.addLayout(self.notesLayout, 0, 0, Qt.AlignCenter)
        self.grid.addLayout(self.sliderLay, 1, 0, Qt.AlignCenter)


    """
    " Adds a note to the "true" scale
    " @param note The note to be appended
    """
    def addTruthNote(self, note):
        self.truthNotesStr += note
        self.truthNotesLe.setText(self.truthNotesStr)


    """
    "
    """
    def addAiNote(self, note):
        self.aiNotesStr += note
        self.aiNotesLe.setText(self.aiNotesStr)
