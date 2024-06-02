
def find_major_scales(n, notes):
    notes_order = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    scales = []
    
    for i in range(12):
        scale_notes = []
        current_note = notes_order[i]
        scale_notes.append(current_note)
        next_index = i
        for step in [2, 2, 1, 2, 2, 2, 1]:
            next_index = (next_index + step) % 12
            scale_notes.append(notes_order[next_index])
        
        if all(note in scale_notes for note in notes):
            scales.append(current_note)
    
    if scales:
        return ' '.join(scales)
    else:
        return 'none'

# Input
n = int(input())
notes = input().split()

# Output
print(find_major_scales(n, notes))
