from winsound import Beep
from keyboard import is_pressed, read_key
from time import sleep

note_placements = {'a':39, 'z':40, 's':41, 'x':42, 'd':43, 'c':44, 'v':45, 'g':46, 'b':47, 'h':48, 'n':49, 'j':50,
                   'm':51, ',':52, 'l':53, '.':54, ';':55, '/':56, "'":57}

transpose_control = 0
tuning_number = 440
arpeggio = False

def play_note(note):
    frequency = find_frequency(note + transpose_control)
    print(frequency)
    Beep(frequency, 100) #Add functionality for the duration to last as long as the holder is pressing the key  
    sleep(.04)
    
def play_arpeggio(note):
    arpeggio = arpeggiate(note)
    for i in arpeggio:
        Beep(i, 100)
    sleep(.0025)
    
def find_frequency(n):
    global tuning_number
    frequency = (2 ** ((n - 49) / 12)) * tuning_number
    if frequency == 0:
        frequency = 440
    return int(frequency)

def transpose(control):
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

def tune(control):
    global tuning_number
    if control == '5':
        tuning_number -= 1
    elif control == '6':
        tuning_number += 1
    print("The piano is now tuned to: A4 =", tuning_number)
    sleep(0.25)

def arpeggiate(root):                #Example if the note was C
    arpeggio = [root]                #C
    arpeggio.append(root + 2)        #E
    arpeggio.append(arpeggio[1] + 2) #G
    arpeggio.append(arpeggio[2] + 3) #High C
    arpeggio.append(arpeggio[3] - 3) #G
    arpeggio.append(arpeggio[4] - 2) #E
    arpeggio.append(arpeggio[5] - 2) #C
    arpeggio_frequency = []
    for i in arpeggio:
        arpeggio_frequency.append(find_frequency(i))
    return arpeggio_frequency


    

while True:
    note = read_key()
    print(note)
    if (note == '1') or (note == '2') or (note == '3') or (note == '4'):
        transpose(note)
    elif note == '5' or note == '6':
        tune(note)
    elif note == 'left shift':
        if arpeggio == True:
            arpeggio = False
            print("Arpeggio = False")
            sleep(.25)
        elif arpeggio == False:
            arpeggio = True
            print("Arpeggio = True")
            sleep(.25)
    elif note in note_placements.keys():
        if arpeggio == True:
            play_arpeggio(note_placements[note])
        else:
            play_note(note_placements[note])
    elif note == 'q':
        break
            
