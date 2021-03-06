import random


from flask import Flask
from flask import render_template
from flask import request
from flask import session

from note import Note

import chord_calculator

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/quizzer', methods=['GET', 'POST'])
def quizzer():
    return render_template("quizzer_home.html")


@app.route('/scales', methods=['POST'])
def scales():
    return render_template("scale_practice.html")


@app.route('/chords', methods=['POST'])
def chords():

    session['chord_list'] = {
        'A major': [Note.A.value, Note.C_SHARP.value, Note.E.value],
        'B major': [Note.B.value, Note.D_SHARP.value, Note.F_SHARP.value],
        'C major': [Note.C.value, Note.E.value, Note.G.value],
        'D major': [Note.D.value, Note.F_SHARP.value, Note.A.value],
        'E major': [Note.E.value, Note.G_SHARP.value, Note.B.value],
        'F major': [Note.F.value, Note.A.value, Note.C.value],
        'G major': [Note.G.value, Note.B.value, Note.D.value]
    }

    chord_list = session.get('chord_list')

    session['current_chord'] = random.choice(list(chord_list.keys()))

    current_chord = session.get('current_chord')

    return render_template("chord_practice.html", current_chord=current_chord)


@app.route('/chord_check', methods=['POST'])
def check_chords():
    chord_list = session.get('chord_list')
    current_chord = session.get('current_chord')

    chord_calculator.calc_major_chord(chord_list.get(current_chord)[0])
    #print(chord_list.get(current_chord)[0])

    chords_entered = request.form.getlist('note')
    print(*chords_entered, sep='\n')
    print(*chord_list.get(current_chord), sep='\n')

    if set(chords_entered) == set(chord_list.get(current_chord)):
        return render_template("correct.html", practice="chords")
    else:
        return render_template("incorrect.html")


'''
def main():

    is_practice = True
    while is_practice:

        is_valid = False

        while not is_valid:

          quiz_type = input("Would you like to practice scales or chords? ")

          if quiz_type.lower() == 'chords':
              chord_practice()
              is_valid = True
          elif quiz_type.lower() == 'scales':
              scale_practice()
              is_valid = True
          else:
              print("Sorry, that's not a valid option. Please indicate if you would like to practice scales or chords")

        continue_practice = input("Would you like to practice something else? ")

        if continue_practice.lower() == 'no':
            is_practice = False

def chord_practice():

    chords = {
        'A major': 'A C# E',
        'B major': 'B D# F#',
        'C major': 'C E G',
        'D major': 'D F# A',
        'E major': 'E G# B',
        'F major': 'F A C',
        'G major': 'G B D'
    }

    while (True):
        current_chord = random.choice(list(chords.keys()))
        answer = input( "Please enter the notes in the " + current_chord + " chord: ")
        if answer.lower() == chords[current_chord].lower():
            print("Correct!")
        else:
            print("Sorry, that's incorrect")

        continue_practice = input("Would you like to continue chord practice? ")

        if continue_practice.lower() == 'no':
            return

def scale_practice():
    scales = {
        'A major': 'A B C# D E F# G# A',
        'B major': 'B C# D# E F# G# A# B',
        'C major': 'C D E F G A B C',
        'D major': 'D E F# G A B C# D',
        'E major': 'E F# G# A B C# D# E',
        'F major': 'F G A Bflat C D E F',
        'G major': 'G A B C D E F# G'
    }

    while (True):
        current_scale = random.choice(list(scales.keys()))
        answer = input("Please enter the notes in the " + current_scale + " chord: ")
        if answer.lower() == scales[current_scale].lower():
            print("Correct!")
        else:
            print("Sorry, that's incorrect")

        continue_practice = input("Would you like to continue scale practice? ")

        if continue_practice.lower() == 'no':
            return

#if __name__ == "__main__":
    main()
'''

if __name__ == "__main__":
    app.run()
