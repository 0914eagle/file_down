
def identify_major_scales(n, notes):
    notes_list = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    scales = {
        'C': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
        'C#': ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C'],
        'D': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
        'D#': ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D'],
        'E': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
        'F': ['F', 'G', 'A', 'A#', 'C', 'D', 'E'],
        'F#': ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F'],
        'G': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
        'G#': ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G'],
        'A': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
        'A#': ['A#', 'C', 'D', 'D#', 'F', 'G', 'A'],
        'B': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']
    }
    
    scales_found = set()
    
    for start_note, scale in scales.items():
        possible_scale = []
        for i in range(len(notes)):
            note_index = notes_list.index(notes[i])
            if notes_list[(note_index - notes_list.index(start_note)) % 12] not in scale:
                break
            possible_scale.append(notes_list[(note_index - notes_list.index(start_note)) % 12])
        else:
            scales_found.add(start_note)
    
    if scales_found:
        return ' '.join(sorted(scales_found))
    else:
        return 'none'

# Input parsing
n = int(input())
notes = input().split()

# Call the function and print the result
print(identify_major_scales(n, notes))
