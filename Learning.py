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
        legalNoteArr = []

        # 1st, 3rd, 5th
        # one step up/down

        #FIXME: assumes no sharps in key signature

        if note_letters == "C":
            #                           primary             option 1            option 2
            legalNoteArr.append(NoteOp(("C", octave + 1), [("D", octave + 1), ("B", octave + 1)]))
            legalNoteArr.append(NoteOp(("E", octave + 1), [("F", octave + 1), ("D", octave + 1)]))
            legalNoteArr.append(NoteOp(("G", octave + 1), [("A", octave + 1), ("F", octave + 1)]))
        elif note_letters == "C#":
            x = 1
        elif note_letters == "D":
            legalNoteArr.append(NoteOp(("D", octave + 1), [("E", octave + 1), ("C", octave + 1)]))
            legalNoteArr.append(NoteOp(("F", octave + 1), [("G", octave + 1), ("E", octave + 1)]))
            legalNoteArr.append(NoteOp(("A", octave + 1), [("B", octave + 1), ("G", octave + 1)]))
        elif note_letters == "D#":
            x = 1
        elif note_letters == "E":
            legalNoteArr.append(NoteOp(("E", octave + 1), [("F", octave + 1), ("D", octave + 1)]))
            legalNoteArr.append(NoteOp(("G", octave + 1), [("A", octave + 1), ("F", octave + 1)]))
            legalNoteArr.append(NoteOp(("B", octave + 1), [("C", octave + 1), ("A", octave + 1)]))
        elif note_letters == "F":
            legalNoteArr.append(NoteOp(("F", octave + 1), [("G", octave + 1), ("E", octave + 1)]))
            legalNoteArr.append(NoteOp(("A", octave + 1), [("B", octave + 1), ("G", octave + 1)]))
            legalNoteArr.append(NoteOp(("C", octave + 1), [("D", octave + 1), ("B", octave + 1)]))
        elif note_letters == "F#":
            x = 1
        elif note_letters == "G":
            legalNoteArr.append(NoteOp(("G", octave + 1), [("A", octave + 1), ("F", octave + 1)]))
            legalNoteArr.append(NoteOp(("B", octave + 1), [("C", octave + 1), ("A", octave + 1)]))
            legalNoteArr.append(NoteOp(("D", octave + 1), [("E", octave + 1), ("C", octave + 1)]))
        elif note_letters == "G#":
            x = 1
        elif note_letters == "A":
            legalNoteArr.append(NoteOp(("A", octave + 1), [("B", octave + 1), ("G", octave + 1)]))
            legalNoteArr.append(NoteOp(("C", octave + 1), [("D", octave + 1), ("B", octave + 1)]))
            legalNoteArr.append(NoteOp(("E", octave + 1), [("F", octave + 1), ("D", octave + 1)]))
        elif note_letters == "A#":
            x = 1
        elif note_letters == "B":
            legalNoteArr.append(NoteOp(("B", octave + 1), [("C", octave + 1), ("A", octave + 1)]))
            legalNoteArr.append(NoteOp(("D", octave + 1), [("E", octave + 1), ("C", octave + 1)]))
            legalNoteArr.append(NoteOp(("F", octave + 1), [("G", octave + 1), ("E", octave + 1)]))
