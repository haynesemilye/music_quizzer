import math

from note import Note

def calc_major_chord(root_note):
    print("Root note: " + root_note)
    note_array = [n.value for n in Note]
    root_note_index = note_array.index(root_note)
    print("Root note index: ")
    print(root_note_index)

    first_third_note_index = root_note_index + 2
    if first_third_note_index > (len(note_array)):
        first_third_note_index = math.abs(note_array.size() - first_third_note_index)
        print(note_array[first_third_note_index])

    #second_third_note = note_array[root_note_index + 4]