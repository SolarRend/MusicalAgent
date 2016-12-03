##############################################################################
##
## File: Learning.py
## Authors:
## File Description: Q-Learning agent (based on the Pacman one).
##                   util.Counter objects have been converted to dict ones,
##                   some code from the parent class learningAgent has
##                   been included.
##
## Created: 11/26/2016
## Last Modified 11/26/2016
##
##############################################################################

import random
import World


class Learning(World.MusicWorld):

    def __init__(self, scale = ["C", "D", "E", "F", "G", "A", "B"], alpha=1.0, epsilon=0.05, gamma=0.8, numTraining = 10):

        #set the goal scale
        #super(Learning, self).__init__(scale)
        World.MusicWorld.__init__(self, scale)

        self.values = {} #util.Counter()  # key, square; each square has four wedges

        self.alpha = float(alpha)
        self.epsilon = float(epsilon)
        self.gamma = float(gamma)
        self.numTraining = int(numTraining)

        #current state
        self.currState = self.getStartState()

        #list of q-values
        self.qvalues = {}


    def qLearning(self):

        while self.currState != self.getTerminalState():
            # get the list of available actions
            actions = self.getLegalActions(self.currState)

            actionAndQValue = {}

            #randomly choose an action
            for action in actions:
                if (self.currState, action) in self.qvalues:
                    actionAndQValue[action] = self.qvalues[(self.currState, action)]
                else:
                    actionAndQValue[action] = 0

            #TODO: choose BEST action
            #currAction = random.choice(actions)

            all = actionAndQValue.items()
            values = [x[1] for x in all]
            maxIndex = values.index(max(values))

            currMaxAction = all[maxIndex]


            print "currMaxActino=", currMaxAction[0]

            #get the next state
            nextState = self.takeAction(self.currState, currMaxAction[0])

            print "nextState (real)=", nextState

            nextActions = self.getLegalActions(nextState)

            nextActionAndNextQValue = {}

            for action in nextActions:
                if (nextState, action) in self.qvalues:
                    nextActionAndNextQValue[action] = self.qvalues[(nextState, action)]
                else:
                    nextActionAndNextQValue[action] = 0

            all = nextActionAndNextQValue.items()
            values = [x[1] for x in all]
            maxIndex = values.index(max(values))
            #print "maxIndex=", maxIndex
            currMaxAction2nd = all[maxIndex]

            print "currMaxAction (2nd)=", currMaxAction2nd

            r = self.getReward(self.currState, currMaxAction[0], nextState)

            sample = r + (self.gamma * nextActionAndNextQValue[currMaxAction2nd[0]])

            self.qvalues[(self.currState, currMaxAction[0])] = \
                (1 - self.alpha) * (self.qvalues[(self.currState, currMaxAction[0])] if (self.currState, currMaxAction[0]) in self.qvalues else 0) + self.alpha * sample

            #print "qvalue=", self.qvalues[(self.currState, currMaxAction[0])]
            print "qvalues=", self.qvalues
            print "currState=", self.currState
            print "nextState=", nextState

            self.currState = nextState

        self.currState = self.getStartState()


# --- test ---
learning = Learning()

for x in range(500):
    learning.qLearning()

World.global_player.destroy()

