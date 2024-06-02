
def find_major_scales(n, notes):
    notes_order = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    scales = []
    
    for i in range(12):
        scale_notes = []
        current_note = notes_order[i]
        scale_notes.append(current_note)
        
        tone_steps = [2, 2, 1, 2, 2, 2, 1]
        for step in tone_steps:
            current_index = notes_order.index(current_note)
            next_index = (current_index + step) % 12
            current_note = notes_order[next_index]
            scale_notes.append(current_note)
        
        if all(note in scale_notes for note in notes):
            scales.append(scale_notes[0])
    
    if scales:
        return ' '.join(scales)
    else:
        return 'none'

# Input
n = int(input())
notes = input().split()

# Output
print(find_major_scales(n, notes))
