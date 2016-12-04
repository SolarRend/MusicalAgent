import random

class NoteOp:

    def __init__(self, primary, other):

        # on-beat compatable note
        self.primary = primary

        # off-beat optional notes
        self.other = other

class Notes:

    def __init__(self):
        print ""

    def getLegalNotes(self, note_letters, octave):
        self.legalNoteArr = []

        # 1st, 3rd, 5th
        # one step up/down

        #FIXME: assumes no sharps in key signature

        if note_letters == "C":
            #                           primary             option 1            option 2
            self.legalNoteArr.append(NoteOp(("C", octave + 1), [("D", octave + 1), ("B", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("E", octave + 1), [("F", octave + 1), ("D", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("G", octave + 1), [("A", octave + 1), ("F", octave + 1)]))
        elif note_letters == "C#":
            self.legalNoteArr.append(NoteOp(("C#", octave + 1), [("D", octave + 1), ("B", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("E", octave + 1), [("F", octave + 1), ("D", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("G", octave + 1), [("A", octave + 1), ("F", octave + 1)]))
        elif note_letters == "D":
            self.legalNoteArr.append(NoteOp(("D", octave + 1), [("E", octave + 1), ("C", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("F", octave + 1), [("G", octave + 1), ("E", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("A", octave + 1), [("B", octave + 1), ("G", octave + 1)]))
        elif note_letters == "D#":
            self.legalNoteArr.append(NoteOp(("D#", octave + 1), [("E", octave + 1), ("C", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("F", octave + 1), [("G", octave + 1), ("E", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("A", octave + 1), [("B", octave + 1), ("G", octave + 1)]))
        elif note_letters == "E":
            self.legalNoteArr.append(NoteOp(("E", octave + 1), [("F", octave + 1), ("D", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("G", octave + 1), [("A", octave + 1), ("F", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("B", octave + 1), [("C", octave + 1), ("A", octave + 1)]))
        elif note_letters == "F":
            self.legalNoteArr.append(NoteOp(("F", octave + 1), [("G", octave + 1), ("E", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("A", octave + 1), [("B", octave + 1), ("G", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("C", octave + 1), [("D", octave + 1), ("B", octave + 1)]))
        elif note_letters == "F#":
            self.legalNoteArr.append(NoteOp(("F#", octave + 1), [("G", octave + 1), ("E", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("A", octave + 1), [("B", octave + 1), ("G", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("C", octave + 1), [("D", octave + 1), ("B", octave + 1)]))
        elif note_letters == "G":
            self.legalNoteArr.append(NoteOp(("G", octave + 1), [("A", octave + 1), ("F", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("B", octave + 1), [("C", octave + 1), ("A", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("D", octave + 1), [("E", octave + 1), ("C", octave + 1)]))
        elif note_letters == "G#":
            self.legalNoteArr.append(NoteOp(("G#", octave + 1), [("A", octave + 1), ("F", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("B", octave + 1), [("C", octave + 1), ("A", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("D", octave + 1), [("E", octave + 1), ("C", octave + 1)]))
        elif note_letters == "A":
            self.legalNoteArr.append(NoteOp(("A", octave + 1), [("B", octave + 1), ("G", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("C", octave + 1), [("D", octave + 1), ("B", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("E", octave + 1), [("F", octave + 1), ("D", octave + 1)]))
        elif note_letters == "A#":
            self.legalNoteArr.append(NoteOp(("A#", octave + 1), [("B", octave + 1), ("G", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("C", octave + 1), [("D", octave + 1), ("B", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("E", octave + 1), [("F", octave + 1), ("D", octave + 1)]))
        elif note_letters == "B":
            self.legalNoteArr.append(NoteOp(("B", octave + 1), [("C", octave + 1), ("A", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("D", octave + 1), [("E", octave + 1), ("C", octave + 1)]))
            self.legalNoteArr.append(NoteOp(("F", octave + 1), [("G", octave + 1), ("E", octave + 1)]))

    def getCounterpoint(self, note_letters, octave):

        self.getLegalNotes(note_letters, octave)

        primaryAnd2ndOpt = random.choice(self.legalNoteArr)
        print "primaryAnd2ndOpt=", primaryAnd2ndOpt.primary, primaryAnd2ndOpt.other
        primaryTuple = primaryAnd2ndOpt.primary
        opt = random.choice(primaryAnd2ndOpt.other)

        print "Accompaniment: ", primaryTuple[0], opt[0]

        return (primaryTuple, opt)