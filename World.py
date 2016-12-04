'''
Internal representation of the musical agent world.
Contains: States, Actions, Rewards and Penalties
Authors: James Kuczynski <jkuczyns@cs.uml.edu>
         Joshua Rodriguez <jrodrig1@cs.uml.edu>
'''

import random
import Player
import time
import Notes
import LilyPy
# create audio player; use audio port 3
global_player = Player.Player(3)
global_player2 = Player.Player(2)

class MusicWorld:

    def __init__(self, scale):

        # setup for print to file
        self.lilyPy = LilyPy.LilyPy()

        # setting unique start state
        self.startState = (None, -1)

        # setting unique end state
        self.terminalState = (None, 15)

        # scale that the agent is trying to learn
        # contains 14 elements which are notes
        self.goalScale = list(scale)

        self.counterpoint = Notes.Notes()

        #copy decrescendo
        self.goalScale.append(scale[0])
        tmpScale = scale[::-1]
        for note in tmpScale:
            self.goalScale.append(note)

        #world stores the first audio note played
        self.firstPerformanceNote = ""


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
    def takeAction(self, currState, action, shouldPlay, isTraining, tempo, isCoda = False):

        # finish action
        if (action[0] != "finish"):
            if shouldPlay:


                # store the first note played
                if self.firstPerformanceNote == "" and not isTraining:
                    self.firstPerformanceNote = action[1][0]
                    print "in the key of: ", self.firstPerformanceNote


                if self.firstPerformanceNote == "C" and action[1][1] >=7 and action[1][1] <= 7:
                    octave = 5
                elif self.firstPerformanceNote == "C":
                    octave = 4
                elif self.firstPerformanceNote == "D" and action[1][1] >=6 and action[1][1] <= 8:
                    octave = 5
                elif self.firstPerformanceNote == "D":
                    octave = 4
                elif self.firstPerformanceNote == "E" and action[1][1] >=5 and action[1][1] <= 9:
                    octave = 5
                elif self.firstPerformanceNote == "E":
                    octave = 4
                elif self.firstPerformanceNote == "F" and action[1][1] >=4 and action[1][1] <= 10:
                    octave = 5
                elif self.firstPerformanceNote == "F":
                    octave = 4
                elif self.firstPerformanceNote == "G" and action[1][1] >=3 and action[1][1] <= 11:
                    octave = 5
                elif self.firstPerformanceNote == "G":
                    octave = 4
                elif self.firstPerformanceNote == "A" and action[1][1] >=2 and action[1][1] <= 12:
                    octave = 5
                elif self.firstPerformanceNote == "A":
                    octave = 4
                elif self.firstPerformanceNote == "B" and action[1][1] >= 1 and action[1][1] <= 13:
                    octave = 5
                elif self.firstPerformanceNote == "B":
                    octave = 4
                else:
                    octave = 4


                try:

                    tupleOfTuples = self.counterpoint.getCounterpoint(action[1][0], octave)
                    #play note
                    global_player.playNote(action[1][0], octave, tempo, Player.Instrument.VIOLA)
                    global_player2.playNote(tupleOfTuples[0][0], tupleOfTuples[0][1], tempo/2.0, Player.Instrument.GRAND_PIANO)
                    time.sleep(tempo/2.0)
                    global_player2.playNote(tupleOfTuples[1][0], tupleOfTuples[1][1], tempo / 2.0, Player.Instrument.GRAND_PIANO)
                    time.sleep(tempo/2.0)

                    self.lilyPy.toLy( (action[1][0], octave) )


                except KeyboardInterrupt:
                    global_player.destroy()
                    global_player2.destroy()


        if isCoda:
            try:
                print "playing coda..."
                time.sleep(0.5)
                global_player.playNote(action[1][0], 5, tempo * 2, Player.Instrument.VIOLA)
                global_player2.playNote(action[1][0], 5 + 1, tempo * 2, Player.Instrument.GRAND_PIANO)
                time.sleep(2.0) # give the reads time to exit

                self.lilyPy.file.write("\n}")
                self.lilyPy.file.close()
            except:
                global_player.destroy()
                global_player2.destroy()


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



        #collect massive reward for finishing scale crescendo + decrescendo AND previous note was ending note
        if  (action[0] == "finish"):

            if prevNotePlayed == self.goalScale[14]:
                bounty += 75
            else:
                bounty -= 75

        # not is in the scale, and is out of sequence
        if (currNotePlayed in self.goalScale and currNotePlayed != self.goalScale[currNumOfNotesPlayed]):
            bounty -= 800

        #receive massive penalty for playing out of number sequence
        if (currNumOfNotesPlayed != prevNumOfNotesPlayed+1):
            bounty += -1600

        #recive penalty for not not being in scale
        # **this is where differently weighted penalties will take place **
        if (currNotePlayed not in self.goalScale):
            bounty += -50

        #print "mod test: ", self.goalScale[prevNumOfNotesPlayed%7]

        """
        if currNotePlayed in self.goalScale:

            idx = self.goalScale.index(currNumOfNotesPlayed)

            print "idx=", idx
            print "prevNotePlayed=", prevNotePlayed, " =? ", "goalScale[idx]=", self.goalScale[idx-1]
            print "currNotePlayed=", currNotePlayed

            # correct note in the scale, and is played in sequence
            if ((prevNotePlayed == self.goalScale[idx-1] or (prevNotePlayed == None and self.goalScale[0] == currNotePlayed)) and
                        currNumOfNotesPlayed == prevNumOfNotesPlayed + 1):
                bounty += 500
                print "collected LARGE reward"
                print "prevNotePlayed=", prevNotePlayed
                print "currNotePlayed=", currNotePlayed

            """
            #print ""

        #print "prevNotePlayed=", prevNotePlayed
        #print "currNotePlayed=", currNotePlayed

        if currNotePlayed in self.goalScale:
            if (currNumOfNotesPlayed == prevNumOfNotesPlayed + 1):
                if currNotePlayed == self.goalScale[currNumOfNotesPlayed]:
                    if prevNotePlayed == None and self.goalScale[0] == currNotePlayed:
                        bounty += 50
                        #print "collected large reward: state=", state, "statePrime=", statePrime
                    elif prevNotePlayed == self.goalScale[currNumOfNotesPlayed-1]:
                        bounty += 50
                        #print "collected large reward (elif): state=", state, "statePrime=", statePrime


        #print "total reward=", bounty
        return bounty

"""

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
"""