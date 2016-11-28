'''
Internal representation of the musical agent world.
Contains: States, Actions, Rewards and Penalties
'''
import random
import Player

# create audio player; use audio port 3
global_player = Player.Player(3)

class MusicWorld:

    def __init__(self, scale):

        # setting unique start state
        self.startState = (None, -1)

        # setting unique end state
        self.terminalState = (None, 15)

        # scale that the agent is trying to learn
        # contains 7 elements which are notes
        self.goalScale = scale

        # getting 180 states into list
        self.stateSpace = self.initStateSpace()



    def getStartState(self):
        return self.startState

    def getTerminalState(self):
        return self.terminalState

    #Initialize states
    def initStateSpace(self):

        stateList = []

        for notes in range(12):
            for numOfPrevNotesPlayed in range(15):

                if (notes == 0):
                    stateList.append(("A", numOfPrevNotesPlayed))
                elif (notes == 1):
                    stateList.append(("A#", numOfPrevNotesPlayed))
                elif (notes == 2):
                    stateList.append(("B", numOfPrevNotesPlayed))
                elif (notes == 3):
                    stateList.append(("C", numOfPrevNotesPlayed))
                elif (notes == 4):
                    stateList.append(("C#", numOfPrevNotesPlayed))
                elif (notes == 5):
                    stateList.append(("D", numOfPrevNotesPlayed))
                elif (notes == 6):
                    stateList.append(("D#", numOfPrevNotesPlayed))
                elif (notes == 7):
                    stateList.append(("E", numOfPrevNotesPlayed))
                elif (notes == 8):
                    stateList.append(("F", numOfPrevNotesPlayed))
                elif (notes == 9):
                    stateList.append(("F#", numOfPrevNotesPlayed))
                elif (notes == 10):
                    stateList.append(("G", numOfPrevNotesPlayed))
                elif (notes == 11):
                    stateList.append(("G#", numOfPrevNotesPlayed))

        return stateList

    #returns a list of available actions given a state
    def getLegalActions(self, currState):

        legalActions = []
        # if this is start state then there are 180 actions
        if currState == self.startState:
            for state in self.stateSpace:
                legalActions.append(("play", state))

        # if this is last note in a sequence OR a note
        # not in the goal scale then there is just
        # one action to finish
        elif (currState[1] == 14 or (currState[0] not in self.goalScale)):
            legalActions.append(("finish", self.terminalState))

        # this is an intermediate state  with 179 actions
        else:
            for state in self.stateSpace:
                if state == currState:
                    continue
                legalActions.append(("play", state))

        return legalActions


    #simple transition function for playing notes
    def takeAction(self, currState, action):

        # select octave
        try:
            if currState[1] == 7:
                octave = 5
            else:
                octave = 4
            #print "playing: note=", currState[0], "octave=", octave
            global_player.playNote(currState[0], octave)
        except:
            global_player.destroy()
        return action[1]

    #Determines reward(or penalty) for state, action and state'
    def getReward(self, state, action, statePrime):

        #total rewards
        bounty = 0

        # taking data from states
        prevNotePlayed = state[0]
        prevNumOfNotesPlayed = state[1]
        currNotePlayed = statePrime[0]
        currNumOfNotesPlayed = statePrime[1]



        #collect massive reward for finishing scale crescendo + decrescendo
        if  (action[0] == "finish"):
             bounty += 75

        #receive massive penalty for playing out of number sequence
        if (currNumOfNotesPlayed != prevNumOfNotesPlayed+1):
            bounty += -100

        #recive penalty for not not being in scale
        # **this is where differently weighted penalties will take place **
        if (currNotePlayed not in self.goalScale):
            bounty += -50

        return bounty


scaleList = ["C", "D", "E", "F", "G", "A", "B"]

agent = MusicWorld(scaleList)

currState = agent.getStartState()

while (currState != agent.getTerminalState()):

    print "currState:"
    print currState

    legalActions = agent.getLegalActions(currState)
    randomAction = random.choice(legalActions)
    print "taking action:"
    print randomAction

    nextState = agent.takeAction(currState, randomAction)
    print "nextState:"
    print nextState

    reward = agent.getReward(currState, randomAction, nextState)
    print "claiming reward:"
    print reward
    currState = nextState

print "currState:"
print currState

global_player.destroy()