'''
Hello there! Let me introduce my piano program to you.
All you have to do is start this program and begin typing!
The two bottom rows of keys are used for the actual notes,
while the number row is used to control different functions.

Here is a diagram showing the layout of the keyboard:

			      Octave                                       Arpeggiator
	    Transpose       Transpose	      Tuning	   Duration          Control
	    -       +       -       +       -       +      -       +        -       +
┌───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬────────────────┐
│~	│!	│@	│#	│$	│%	│^	│&	│*	│(	│)	│_	│+	│Backspace	 │
│`	│1	│2	│3	│4	│5	│6	│7	│8	│9      │0	│-	│=	│		 │
│	│	│	│	│	│	│	│	│	│	│	│	│	│		 │
├───────┴──┬────┴──┬────┴──┬────┴──┬────┴──┬────┴──┬────┴──┬────┴──┬────┴──┬────┴──┬────┴──┬────┴──┬────┴──┬─────────────┤
│Tab	   │Q	   │W	   │E	   │R	   │T	   │Y	   │U	   │I	   │O	   │P	   │{	   │}	   │|	   	 │
│	   │  Quit │ Reset │	   │	   │	   │	   │	   │	   │	   │	   │[	   │]	   │\	   	 │
│	   │	   │	   │	   │	   │	   │	   │	   │	   │	   │	   │	   │	   │	   	 │
├──────────┴──┬────┴──┬────┴──┬────┴──┬────┴──┬────┴──┬────┴──┬────┴──┬────┴──┬────┴──┬────┴──┬────┴──┬────┴─────────────┤
│Caps Lock    │A      │S      │D      │F      │G      │H      │J      │K      │L      │:      │"      │Enter	   	 │
│	      │    B  │  C#/Db│  D#/Eb│       │  F#/Gb│  G#/Ab│  A#/Bb│       │  C#/Db│; D#/Eb│'    F │		   	 │
│	      │       │       │       │       │       │       │       │       │       │       │       │		   	 │
├─────────────┴───┬───┴───┬───┴───┬───┴───┬───┴───┬───┴───┬───┴───┬───┴───┬───┴───┬───┴───┬───┴───┬───┴──────────────────┤
│Shift	      	  │Z      │X      │C      │V      │B      │N      │M      │<      │>      │?      │Shift      		 │
|     Turn on     │     C │     D │     E │     F │     G │     A │     B │,    C │.   D  │/    E │      		 │
│     Arpeggio 	  │       │       │       │       │       │       │       │       │       │       │      		 │
├───────────┬─────┴───┬───┴────┬──┴───────┴───────┴───────┴───────┴───────┴───┬───┴─────┬─┴───────┼─────────┬────────────┤
│Ctrl	    │Win      │Alt     │	  				      │Alt	│Win	  │Menu	    │Ctrl        │
│	    │	      │	       │	  				      │		│	  │	    │            │
│	    │	      │	       │	  				      │		│	  │	    │            │
└───────────┴─────────┴────────┴──────────────────────────────────────────────┴─────────┴─────────┴─────────┴────────────┘
'''

from winsound import Beep
from keyboard import is_pressed, read_key
from time import sleep

note_placements = {'a':39, 'z':40, 's':41, 'x':42, 'd':43, 'c':44, 'v':45, 'g':46, 'b':47, 'h':48, 'n':49, 'j':50, #The value of the notes based on
                   'm':51, ',':52, 'l':53, '.':54, ';':55, '/':56, "'":57}                                          #their placements on the keyboard.

transpose_control = 0 #Variable to transpose the note. (Moves the value of a note up or down [if A = 4 and the user transposes it down by 1, A = 3,])
duration_control = 100 #Variable for the duration of the note
tuning_number = 440 #Used in the find_frequency module (Used in the formula to find the frequency of each note)
arpeggio = False #Boolean for the arpeggiator
arpeggio_control = 4
arpeggio_list = [0, 4, 7, 12, 16, 19, 24, 28, 31, 36]

def play_note(note): #Function that plays the note
    frequency = find_frequency(note + transpose_control)
    print(frequency)
    if frequency != None:
        Beep(frequency, duration_control) #TODO: Add functionality for the duration to last as long as the holder is pressing the key  
        sleep(.0025)
    return
    
def play_arpeggio(note): #Function that plays the arpeggio
    arpeggio = arpeggiate(note + transpose_control) #Get the notes in a list from the function 'arpeggiate'
    for i in arpeggio: #Loop over the notes to play the arpeggio
        if i != None:
            Beep(i, duration_control)
            print(i)
    sleep(.0025)
    
def find_frequency(n): #Find the frequency for the note that was played
    global tuning_number
    frequency = (2 ** ((n - 49) / 12)) * tuning_number #The formula to find a note based on the tuning number
    if frequency == 0:
        frequency = 440
    if frequency >= 32767: #Winsound will only allow frequencies between 37 and 32767, so this will catch if a frequency is higher or lower
        print("Note to High")
        return
    elif frequency <=37:
        print("Note to Low")
        return
    return int(frequency)

def transpose(control): #Transposes the note up or down and by octaves or just one note based on the user input
    global transpose_control
    if control == '1':
        transpose_control -= 1
    elif control == '2':
        transpose_control += 1
    elif control == '3':
        transpose_control -= 12
    elif control == '4':
        transpose_control += 12
    sleep(0.25)

def tune(control): #Tunes the piano and then prints what the piano is tuned too
    global tuning_number
    if control == '5':
        tuning_number -= 1
    elif control == '6':
        tuning_number += 1
    print("The piano is now tuned to: A4 =", tuning_number)
    sleep(0.25)

def arpeggiate(root):                #Makes an arpeggio based on the root note.
    global arpeggio_control
    arpeggio = []
    arpeggio_frequency = []
    down_arpeggio = []
    if arpeggio_control > 0:
        for i in range(arpeggio_control):
            arpeggio.append(root + arpeggio_list[i])
    elif arpeggio_control < 0:
        for i in range(arpeggio_control * -1):
            arpeggio.append(root + (arpeggio_list[i] * -1))
    elif arpeggio_control == 0:
        return find_frequency(root)
    down_arpeggio = arpeggio[::-1]
    del down_arpeggio[0]
    arpeggio.extend(down_arpeggio)
    for i in arpeggio:
        arpeggio_frequency.append(find_frequency(i))
    return arpeggio_frequency

def change_duration(n):
    global duration_control
    if n =='7':
        duration_control -= 10
    elif n =='8':
        duration_control += 10
    print("Duration changed to:", duration_control)
    sleep(0.25)


while True:
    note = read_key()
    print(note)
    if (note == '1') or (note == '2') or (note == '3') or (note == '4'):
        transpose(note)
    elif note == '5' or note == '6':
        tune(note)
    elif note == '7' or note == '8':
        change_duration(note)
    elif note == 'shift':
        if arpeggio == True:
            arpeggio = False
            print("Arpeggio = False")
            sleep(.25)
        elif arpeggio == False:
            arpeggio = True
            print("Arpeggio = True")
            sleep(.25)
    elif note == '9' or note == '0':
        if note == '9':
            if arpeggio_control != -10: 
                arpeggio_control -= 1    
                print('The number of notes in an arpeggio is:', arpeggio_control)
                sleep(.33)
            else:
                print('Arpeggio thing is too low, increase it')

        elif note == '0':
            if arpeggio_control != 10:
                arpeggio_control += 1
                print('The number of notes in an arpeggio is:', arpeggio_control)
                sleep(.33)
            else:
                print('Arpeggio thing is too high, decrease it')
        else:
            break
    elif note in note_placements.keys():
        if arpeggio == True:
            play_arpeggio(note_placements[note])
        else:
            if note_placements[note] > 88 or note_placements[note] < 1:
                break
            else:
                play_note(note_placements[note])
    elif note == 'q':
        break
    elif note =='w':
        transpose_control = 0
        duration_control = 100
        tuning_number = 440
        arpeggio = False
        print("Everything has reset.")
            
