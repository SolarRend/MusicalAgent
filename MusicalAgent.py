'''
The music learning agent
Authors: James Kuczynski <jkuczyns@cs.uml.edu>
         Joshua Rodriguez <jrodrig1@cs.uml.edu>
'''
import Learning
import PitchDetection

def listen():
    detector = PitchDetection.PitchDetection()
    scale = detector.detect()
    return scale

scale = listen()

xavier = Learning.Learning(scale)

for x in range(2000):
    if x > 0 and x < 30:
        xavier.qLearn(True)
    elif x > 800 and x < 808:
        xavier.qLearn(True)
    elif x > 1200 and x < 1205:
        xavier.qLearn(True)
    else:
        xavier.qLearn(False)
    #iter += iter + 1
    #time.sleep(0.010)
    print "x=", x


state = xavier.getStartState()

while state != xavier.getTerminalState():
    print "state=", state
    state = xavier.takeAction(state, xavier.computeBestAction(state), True, False)

Learning.World.global_player.destroy()


