#!/usr/bin/python

##############################################################################
##
## File: musical_agent.py
## Authors: James Kuczynski <jkuczyns@cs.uml.edu>
##          Joshua Rodriguez <jrodrigu@cs.uml.edu>
## File Description: This file contains the driver function.
##
##
## Created: 11/07/2016 by J.K.
## Last Modified: 11/08/2016 by J.K
##
##############################################################################

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import MasterGui

"""
" Main method of the project.
"""
def main():
    # Start frontend
    app = QApplication(sys.argv)
    masterGui = MasterGui.MasterGui()
    masterGui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()