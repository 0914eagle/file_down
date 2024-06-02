
def find_major_scales(n, notes):
    notes_order = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    scales = []
    
    for i in range(12):
        scale_notes = [notes_order[i]]
        current_note = i
        for interval in [2, 2, 1, 2, 2, 2, 1]:
            current_note = (current_note + interval) % 12
            scale_notes.append(notes_order[current_note])
        
        if all(note in scale_notes for note in notes):
            scales.append(scale_notes[0])
    
    if scales:
        return ' '.join(scales)
    else:
        return 'none'

# Input processing
n = int(input())
notes = input().split()

result = find_major_scales(n, notes)
print(result)
