#!/usr/bin/python

import pygame.midi
import time


class Instrument:
    GRAND_PIANO = 0
    CHURCH_ORGAN = 19


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

class Player:

    def __init__(self, port, instrument = Instrument.GRAND_PIANO, velocity = 127, sleepDuration = 1.0):
        self.instrument = instrument #the instrument used
        self.velocity = velocity #don't touch this
        self.sleepDuration = sleepDuration #how long the program pauses between notes
        pygame.midi.init()
        self.player = pygame.midi.Output(2)
        self.player.set_instrument(self.instrument)



    def playNote(self, note, octave):
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
        else:
            print "ERROR: using default of middle-C"
            currNote = Note.C_4

        self.player.note_on(currNote, self.velocity)
        time.sleep(self.sleepDuration)
        self.player.note_off(currNote, self.velocity)


    def destroy(self):
        del self.player
        pygame.midi.quit()


if __name__ == "__main__":

    player = Player(3)

    octave = [("C", 4), ("C#", 4), ("D", 4), ("D#", 4),
              ("E", 4), ("F", 4), ("F#", 4), ("G", 4),
              ("G#", 4), ("A", 4), ("A#", 4), ("B", 4),
              ("C", 5)]

    try:
        for note in octave:
            player.playNote(note[0], note[1])

        player.destroy()
    except:
        player.destroy() #speaker trouble if the program is killed without deleting the audio player