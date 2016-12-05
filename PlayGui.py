#!/usr/bin/python

##############################################################################
##
## File: PremadeRecGui.py
## Authors: James Kuczynski <jkuczyns@cs.uml.edu>
##          Joshua Rodriguez <jrodrig1@cs.uml.edu>
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
        self.tempoSlider.setMinimum(-50)
        self.tempoSlider.setMaximum(5)
        self.tempoSlider.setValue(30)
        self.tempoSlider.setTickPosition(QSlider.TicksBelow)
        self.tempoSlider.setTickInterval(10)

        self.exploreSlider = QSlider(Qt.Horizontal)
        self.exploreSlider.setMinimum(0)
        self.exploreSlider.setMaximum(100)
        self.exploreSlider.setValue(0)
        self.exploreSlider.setTickPosition(QSlider.TicksBelow)
        self.exploreSlider.setTickInterval(10)

        self.voicesLbl = QLabel("Voices")
        self.voicesSpinBox = QSpinBox()
        self.voicesSpinBox.setMinimum(1)
        self.voicesSpinBox.setMaximum(3)

        self.accompanimentLbl = QLabel("Accompaniment")
        self.accompanimentCb = QCheckBox()

        self.xavier = None


        self.sliderLay.addWidget(self.tempoLbl, 0, 0, Qt.AlignLeft)
        self.sliderLay.addWidget(self.tempoSlider, 0, 1)
        self.sliderLay.addWidget(self.exploreLbl, 1, 0, Qt.AlignLeft)
        self.sliderLay.addWidget(self.exploreSlider, 1, 1)
        self.sliderLay.addWidget(self.accompanimentLbl, 2, 0)
        self.sliderLay.addWidget(self.accompanimentCb, 2, 1)
        ####################################################



        ####################################################
        self.notesLayout = QGridLayout()

        self.playBtn = QPushButton("Play")
        #self.playBtn = QCheckBox("Play")
        self.playBtn.setEnabled(False)
        self.playBtn.setVisible(False)
        self.playBtn.clicked.connect(self.play)
        #self.playBtn.stateChanged.connect(self.play)

        self.trainingLbl = QLabel("Training...")
        self.trainingLbl.setStyleSheet("QLabel{ background-color: red; }")

        self.truthNotesLbl = QLabel("Scale")
        self.aiNotesLbl = QLabel("AI Output")

        self.truthNotesLe = QLineEdit() #the correct scale
        self.truthNotesLe.setDragEnabled(True)

        self.aiNotesLe = QLineEdit() #what the AI is playing
        self.aiNotesLe.setDragEnabled(True)

        self.notesLayout.addWidget(self.truthNotesLbl, 0, 0, Qt.AlignHCenter)
        self.notesLayout.addWidget(self.truthNotesLe, 1, 0, Qt.AlignVCenter)
        self.notesLayout.addWidget(self.aiNotesLe, 2, 0, Qt.AlignVCenter)
        self.notesLayout.addWidget(self.aiNotesLbl, 3, 0, Qt.AlignHCenter)
        self.notesLayout.addWidget(self.trainingLbl, 2, 1)
        self.notesLayout.addWidget(self.playBtn, 2, 2)


        ####################################################

        #self.grid.addWidget(self.recordBtn, 0, 0)
        #self.grid.addWidget(self.tempoSlider, 1, 0)
        #self.grid.addWidget(self.exploreSlider, 2, 0)
        #self.grid.addWidget(self.volumeSlider, 3, 0)
        #self.grid.addWidget(self.truthNotesLe, 4, 0)
        #self.grid.addWidget(self.aiNotesLe, 5, 0)
        self.grid.addLayout(self.notesLayout, 0, 0, Qt.AlignCenter)
        self.grid.addLayout(self.sliderLay, 1, 0, Qt.AlignCenter)

        self.exploreSlider.setValue(0)
        self.tempoSlider.setValue(30)


    def play(self):
        accomp = self.accompanimentCb.isChecked()
        try:
            #r = 0  # random.random() #FIXME: from exploration slider
            r = self.exploreSlider.value()/100.0
            tempo = abs(self.tempoSlider.value() / 100.0)  # tempo = 0.3 #FIXME: tempo slider value

            print "epsilon: ", r
            print "tempo: ", tempo

            #while self.playBtn.isChecked() == True:
            for i in range(2):

                state = self.xavier.getStartState()

                while state != self.xavier.getTerminalState():
                    print "state: ", state
                    state = self.xavier.takeAction(state, self.xavier.computeAction(state, r), True, False, tempo, accomp)

                    # Learning.World.global_player.destroy()
            self.xavier.createExplorationQvalues()

        except KeyboardInterrupt:
            Learning.World.global_player.destroy()

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
