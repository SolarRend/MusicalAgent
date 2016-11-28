#!/usr/bin/python

##############################################################################
##
## File: Player.py
## Authors: James Kuczynski <jkuczyns@cs.uml.edu>
##          Joshua Rodriguez <jrodrig1@cs.uml.edu>
## File Description: midi audio playback.  The user can select the tempo,
##                   notes, and instrument.
##
## Created: 11/26/2016 by J.K.
## Last Modified: 11/27/2016 by J.K.
##
##############################################################################

import pygame.midi
import time


# pygame uses integers (0-127 inclusive) to represent instruments.
class Instrument:
    GRAND_PIANO = 0
    CHURCH_ORGAN = 19
    VIOLA = 40


# representation of notes (compatible with pygame's representation).
class Note:
    C_4 = 60
    C_SHARP_4 = 61
    D_4 = 62
    D_SHARP_4 = 63
    E_4 = 64
    F_4 = 65
    F_SHARP_4 = 66
    G_4 = 67
    G_SHARP_4 = 68
    A_4 = 69
    A_SHARP_4 = 70
    B_4 = 71
    C_5 = 72
    C_SHARP_5 = 73
    D_5 = 74
    D_SHARP_5 = 75
    E_5 = 76
    F_5 = 77
    F_SHARP_5 = 78
    G_5 = 79
    G_SHARP_5 = 80
    A_5 = 81
    A_SHARP_5 = 82
    B_5 = 83


class Player:

    def __init__(self, port, instrument = Instrument.GRAND_PIANO, velocity = 127, sleepDuration = 1.0):
        self.instrument = instrument # the instrument used
        self.velocity = velocity # don't touch this
        self.sleepDuration = sleepDuration #how long the program pauses between notes

        # initialize the output
        pygame.midi.init()

        # set the audio port and instrument
        self.player = pygame.midi.Output(port)
        self.player.set_instrument(self.instrument)


    def playNote(self, note, octave):

        # map string representation to "enum"
        if note == "C" and octave == 4:
            currNote = Note.C_4
        elif note == "C#" and octave == 4:
            currNote = Note.C_SHARP_4
        elif note == "D" and octave == 4:
            currNote = Note.D_4
        elif note == "D#" and octave == 4:
            currNote = Note.D_SHARP_4
        elif note == "E" and octave == 4:
            currNote = Note.E_4
        elif note == "F" and octave == 4:
            currNote = Note.F_4
        elif note == "F#" and octave == 4:
            currNote = Note.F_SHARP_4
        elif note == "G" and octave == 4:
            currNote = Note.G_4
        elif note == "G#" and octave == 4:
            currNote = Note.G_SHARP_4
        elif note == "A" and octave == 4:
            currNote = Note.A_4
        elif note == "A#" and octave == 4:
            currNote = Note.A_SHARP_4
        elif note == "B" and octave == 4:
            currNote = Note.B_4
        elif note == "C" and octave == 5:
            currNote = Note.C_5
        elif note == "C#" and octave == 5:
            currNote = Note.C_SHARP_5
        elif note == "D" and octave == 5:
            currNote = Note.D_5
        elif note == "D#" and octave == 5:
            currNote = Note.D_SHARP_5
        elif note == "E" and octave == 5:
            currNote = Note.E_5
        elif note == "F" and octave == 5:
            currNote = Note.F_5
        elif note == "F#" and octave == 5:
            currNote = Note.F_SHARP_5
        elif note == "G" and octave == 5:
            currNote = Note.G_5
        elif note == "G#" and octave == 5:
            currNote = Note.G_SHARP_5
        elif note == "A" and octave == 5:
            currNote = Note.A_5
        elif note == "A#" and octave == 5:
            currNote = Note.A_SHARP_5
        elif note == "B" and octave == 5:
            currNote = Note.B_5
        else:
            print "ERROR: using default of middle-C"
            currNote = Note.C_4

        # start playing the note
        # pause for a duration to let the note play
        # stop the note
        self.player.note_on(currNote, self.velocity)
        time.sleep(self.sleepDuration)
        self.player.note_off(currNote, self.velocity)


    # delete/shut down the audio player
    def destroy(self):
        del self.player
        pygame.midi.quit()


# test case
if __name__ == "__main__":

    player = Player(3, Instrument.GRAND_PIANO, 127, 0.15)

    # "every" note in an octave
    octave = [("C", 4), ("C#", 4), ("D", 4), ("D#", 4),
              ("E", 4), ("F", 4), ("F#", 4), ("G", 4),
              ("G#", 4), ("A", 4), ("A#", 4), ("B", 4),
              ("C", 5), ("C#", 5), ("D", 5), ("D#", 5),
              ("E", 5), ("F", 5), ("F#", 5), ("G", 5),
              ("G#", 5), ("A", 5), ("A#", 5), ("B", 5),]

    # play a chromatic run
    # if program quits before finishing, delete the audio player object.
    try:
        for note in octave:
            player.playNote(note[0], note[1])

        player.destroy()
    except:
        # TODO: stop the current note(s)
        player.destroy() #speaker trouble if the program is killed without deleting the audio player