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
import time


class Learning(World.MusicWorld):

    def __init__(self, scale = ["C", "D", "E", "F", "G", "A", "B"], alpha=0.5, epsilon=0.0, gamma=1.0, numTraining = 10):

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

        self.file = open("log", "w")


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


            #print "currMaxActino=", currMaxAction[0]

            #get the next state
            r = random.random()
            #if r < self.epsilon:
            #    nextState = self.takeAction(self.currState, random.choice(actions))
            #else:
            nextState = self.takeAction(self.currState, currMaxAction[0], False)
            #print "nextState (real)=", nextState

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

            #print "currMaxAction (2nd)=", currMaxAction2nd

            r = self.getReward(self.currState, currMaxAction[0], nextState)

            sample = r + (self.gamma * nextActionAndNextQValue[currMaxAction2nd[0]])

            self.qvalues[(self.currState, currMaxAction[0])] = \
                (1 - self.alpha) * (self.qvalues[(self.currState, currMaxAction[0])] if (self.currState, currMaxAction[0]) in self.qvalues else 0) + self.alpha * sample

            #print "qvalue=", self.qvalues[(self.currState, currMaxAction[0])]
            #print "qvalues=", self.qvalues

            #print "currState=", self.currState
            #print "nextState=", nextState

            self.currState = nextState


        self.currState = self.getStartState()

    def computeBestAction(self, state):


        # get all legal actions from state
        actions = self.getLegalActions(state)
        actionAndQValue = {}

        # randomly choose an action
        for action in actions:
            if (state, action) in self.qvalues:
                actionAndQValue[action] = self.qvalues[(state, action)]
            else:
                actionAndQValue[action] = 0

        # TODO: choose BEST action
        # currAction = random.choice(actions)

        all = actionAndQValue.items()
        values = [x[1] for x in all]
        maxIndex = values.index(max(values))
        currMaxAction = all[maxIndex]

        return currMaxAction[0]

        # do what be did before...


# --- test ---
#scale = ["C", "D", "E", "F", "G", "A", "B"] #c Major
#scale = ["C", "D", "D#", "F", "G", "G#", "A#"] #c minor
#scale = ["D", "E", "F#", "G", "A", "B", "C#"] #D Major
scale = ["E", "F#", "G#", "A", "B", "C#", "D#"] #E Major
learning = Learning(scale)
#iter = 0
for x in range(2000):
    learning.qLearning()
    #iter += iter + 1
    #time.sleep(0.010)
    print "x=", x

state = learning.getStartState()

while state != learning.getTerminalState():
    print "state=", state
    state = learning.takeAction(state, learning.computeBestAction(state), True)


learning.file.write("qvalues=")
learning.file.write(str(learning.qvalues))
learning.file.write("\n")
print "qvalues="
print learning.qvalues

World.global_player.destroy()

