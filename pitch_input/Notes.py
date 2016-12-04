class MathNote:
    C_4 =       0
    C_SHARP_4 = 0.5
    D_4 =       1.0
    D_SHARP_4 = 1.5
    E_4 =       2.0
    F_4 =       2.5
    F_SHARP_4 = 3.0
    G_4 =       3.5
    G_SHARP_4 = 4.0
    A_4 =       4.5
    A_SHARP_4 = 5.0
    B_4 =       5.5
    C_5 =       6.0
    C_SHARP_5 = 6.5
    D_5 =       7.0
    D_SHARP_5 = 7.5
    E_5 =       8.0
    F_5 =       8.5
    F_SHARP_5 = 9.0
    G_5 =       9.5
    G_SHARP_5 = 10.0
    A_5 =       10.5
    A_SHARP_5 = 11.0
    B_5 =       11.5
    C_6 =       12.0
    C_SHARP_6 = 12.5
    D_6 =       13.0
    D_SHARP_6 = 13.5
    E_6 =       14.0
    E_SHARP_6 = 14.5
    F_6 =       15.0
    F_SHARP_6 = 15.5
    G_6 =       16.0
    G_SHARP_6 = 16.5
    A_6 =       17.0
    A_SHARP_6 = 17.5
    B_6 =       18.0
    C_7 =       18.5

    def getLegalNotes(self, note_letters, octave):
        legalNoteArr = []

        # 1st, 3rd, 5th
        # one step up/down

        if note_letters == "C":
            #FIXME: create a container class
            legalNoteArr.append((("C", octave + 1), list(("D", octave + 1), ("B", octave + 1))))
            legalNoteArr.append((("E", octave + 1), ()))
            legalNoteArr.append((("G", octave + 1), ()))
        elif note_letters == "C#":
            x = 1
        elif note_letters == "D":
            x = 1
        elif note_letters == "D#":
            x = 1
        elif note_letters == "E":
            x = 1
        elif note_letters == "F":
            x = 1
        elif note_letters == "F#":
            x = 1
        elif note_letters == "G":
            x = 1
        elif note_letters == "G#":
            x = 1
        elif note_letters == "A":
            x = 1
        elif note_letters == "A#":
            x = 1
        elif note_letters == "B":
            x = 1
