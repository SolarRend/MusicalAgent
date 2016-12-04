'''
The music learning agent
Authors: James Kuczynski <jkuczyns@cs.uml.edu>
         Joshua Rodriguez <jrodrig1@cs.uml.edu>
'''
import Learning
import PitchDetection
import random

def listen():
    detector = PitchDetection.PitchDetection()
    scale = detector.detect()
    return scale

try:

    scale = ["C", "D", "E", "F", "G", "A", "B"]#listen()
    #scale = ["C", "E", "G", "B", "D", "F", "A"]

    xavier = Learning.Learning(scale)

    # learning for 2k iterations
    for x in range(2000):
        if x > 0 and x < 30:
            xavier.qLearn(True, 0.05)
        elif x % 250 == 0:
            if random.random() > 0.5:
                xavier.qLearn(True, 0.1)
            else:
                xavier.qLearn(True, 0.2)
        else:
            xavier.qLearn(False, None)
        print "x=", x
    # agent is done learning

    # create modified qValue list for exploration
    xavier.createExplorationQvalues()
    r = 0 #random.random()
    print "epsilon: ", r
    while True:

        state = xavier.getStartState()

        while state != xavier.getTerminalState():
            tempo = 0.5
            print "state: ", state
            state = xavier.takeAction(state, xavier.computeAction(state, r), True, False, tempo)

    #Learning.World.global_player.destroy()

except KeyboardInterrupt:
    Learning.World.global_player.destroy()

