'''
Internal representation of the musical agent world.
Contains: States, Actions, Rewards and Penalties
'''
class MusicWorld:

    def __init__(self):

        # getting 180 states into list
        self.stateSpace = self.initStateSpace()
        ## getting unique start state
        self.startState = (None, -1)

    def getStartState(self):
        return self.startState

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

        # if this is last note in sequence then there is just
        # one action to finish
        elif (currState[1] == 14):
            legalActions.append("finish")

        # this is an intermediate state  with 179 actions
        else:
            for state in self.stateSpace:
                if state == currState:
                    continue
                legalActions.append(state)

        return legalActions


    #Determines reward(or penalty) for state, action and state'
    def getReward(self, state, action, nextState):
        #if  ()
        return

world = MusicWorld()

#world.getLegalActions(("G", 0))


