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

class Learning:

    def __init__(self, actionFn = None, alpha=1.0, epsilon=0.05, gamma=0.8, numTraining = 10):
        self.values = dict() #util.Counter()  # key, square; each square has four wedges

        self.alpha = float(alpha)
        self.epsilon = float(epsilon)
        self.discount = float(gamma)
        self.numTraining = int(numTraining)

        #FIXME: this is from the ReinforcementAgent
        if actionFn == None:
            actionFn = lambda state: state.getLegalActions()
        self.actionFn = actionFn


    def getQValue(self, state, action):
        square = self.values[state]
        qvalue = 0.0
        if not square == 0:
            qvalue = square.values[action]

        return qvalue


    def computeValueFromQValues(self, state):

        legalActions = self.getLegalActions(state)
        currBestQVal = float('-inf')
        if len(legalActions) == 0:
            currBestQVal = 0.0
        else:
            for action in legalActions:
                qvalue = self.getQValue(state, action)
                if currBestQVal < qvalue:
                    currBestQVal = qvalue

        if currBestQVal == float('-inf'):
            currBestQVal = 0.0

        return currBestQVal


    def computeActionFromQValues(self, state):

        currBestAction = None
        currBestCost = float('-inf')
        legalActions = self.getLegalActions(state)

        currBestAction = None
        currBesCost = float('-inf')
        legalActions = self.getLegalActions(state)

        currSquare = self.values[state]
        if not currSquare == 0:
            for action in legalActions:
                if currSquare.values[action] > currBestCost:
                    currBestCost = currSquare.values[action]
                    currBestAction = action

        return currBestAction


    def getAction(self, state):

        legalActions = self.getLegalActions(state)
        currBestAction = None
        currBestValue = float('-inf')
        prob = self.epsilon

        actLst = []
        valLst = []

        if len(legalActions) == 0:
            print "no legal actions available"
        else:
            if self.flipCoin(prob):
                currBestAction = random.choice(legalActions)
            else:
                for action in legalActions:
                    valLst.append(self.getQValue(state, action) )
                    actLst.append(action)
                    if len(valLst) == 0:
                        currBestAction = random.choice(actLst)
                    else:
                        currMax = float('-inf')
                        currAct = None
                        currIdx = -1
                        for i in range(0, len(valLst), 1):
                            if currMax < valLst[i]:
                                currMax = valLst[i]
                                currIdx = i
                                currAct = actLst[i]
                            currBestAction = currAct
                            currBestValue = currMax
                            if currIdx == -1:
                                print "Uh-oh, correct action was never updated in loop"

        return currBestAction


    def update(self, state, action, nextState, reward):

        prevSquare = self.values[state]
        prevWedge = 0.0
        if not prevSquare == 0:
            prevWedge = prevSquare.values[action]

        nextWedge = reward + (self.discount * self.computeValueFromQValues(nextState) )

        if not prevSquare == 0:
            self.values[state].values[action] = self.computationHelper(prevWedge, nextWedge)
        else:
            nextSquare = dict() #util.Counter()
            nextSquare[action] = self.computationHelper(prevWedge, nextWedge)
            self.values[state] = nextSquare



    def computationHelper(self, oldVal, newVal):
        return ((1 - self.alpha) * oldVal) + (self.alpha * newVal)


    def getPolicy(self, state):
        return self.computeActionFromQValues(state)


    def getValue(self, state):
        return self.computeValueFromQValues(state)


    def flipCoin(self, p):
        r = random.random()
        return r < p


    def getLegalActions(self, state):
        """
          Get the actions available for a given
          state. This is what you should use to
          obtain legal actions for a state
        """
        return self.actionFn(state) #FIXME: this is from learningAgents.py
