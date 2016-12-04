##############################################################################
##
## File Description: convert our internal representation of (letter, octave)
##                   tuples to ABC to LilyPond
##
##############################################################################


class LilyPy:

    def __init__(self, clef = "treble", timeSig = "4/4", tempo = "\"Andante\" 4 = 80", key = ("c", "m")):
        self.clef = clef
        self.timeSig = timeSig
        self.tempo = tempo
        self.key = key

        self.file = open("musical_agent.ly", "w")

        #write header boilerplate
        self.file.write("\\version \"2.16.2\"\n")
        self.file.write("\\language \"english\"\n")
        self.file.write("{\n")
        self.file.write("\t\\clef \"" + self.clef + "\"\n")
        self.file.write("\t\\time " + self.timeSig + "\n")
        self.file.write("\t\\tempo " + self.tempo + "\n")
        self.file.write("\t")


    def toLy(self, tuple):
        note = tuple[0]
        octave = tuple[1]
        octaveRepresentation = ""

        if octave > 3:
            for i in range(octave-3):
                octaveRepresentation += "'"
        elif octave < 4:
            for i in range(octave):
                octaveRepresentation += ","

        print note + octaveRepresentation, "--> file"
        self.file.write(note.lower() + octaveRepresentation + " ")