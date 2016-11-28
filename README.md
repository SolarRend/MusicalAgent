#**musical_agent**
:musical_note:*Artificial Intelligence Final Project*:musical_note:


*Authors:*

James Kuczynski,<br>
Undergraduate Researcher,<br>
[Robotics Laboratory][1],<br>
[University of Massachusetts Lowell][2].<br>
*Email:* jkuczyns@cs.uml.edu

Joshua Rodriguez,<br>
Undergraduate Researcher,<br>
[Robotics Laboratory][1],<br>
[University of Massachusetts Lowell][2].<br>
*Email:* jrodrig1@cs.uml.edu

=====

###**Index**

- [Project Synopsis](#project_synopsis)
- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Build & Run](#build_run)
- [Future Work](#future_work)
- [Acknowledgments](#acknowledgments)


###**Project Synopsis**

This is an AI which the user can teach to play--and indeed compose--music.


###**Introduction**

*TBA...*


###**Dependencies**

- Python 2 *(tested with 2.7)*
- PyQT4 *(Python language bindings for the QT Project)*
- pygame *(the midi module)*
 - timidity
- aubio
 - cffi
 - pysoundcard


**Install** *(Linux)*
```
sudo apt-get install python-qt4
sudo apt-get install python-pygame
sudo apt-get install python-cffi
sudo pip install pysoundcard
sudo apt-get install libavformat-dev
sudo apt-get install timidity
```


###**Build & Run**

Test user interface
```
python musical_agent.py
```


Test pitch detection
```
python Au2Hz.py audio_file_name.wav sample_rate
```


Test audio output (Linux):
*(Note: You may have to change the audio port number)*
```
timidity -Os -iA
```
open a second terminal and run:
```
python Player.py
```


Test World (with audio)
```
timidity -Os -iA
```
In a second terminal run:
```
python World.py
```


###**Future Work**

Because this is a college software course final project, it is unlikely that
we will continue to develope it past the end of the semester of Fall 2016.


###**Acknowledgments**

- This work was supported in part by Dr. Fred Martin


[1]: http://robotics.cs.uml.edu/
[2]: http://www.uml.edu/
