
def find_major_scales(n, notes):
    notes_order = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    scales = []
    
    for i in range(12):
        scale_notes = []
        current_note = notes_order[i]
        scale_notes.append(current_note)
        
        tone = (i + 2) % 12
        semitone = (i + 1) % 12
        
        for _ in range(6):
            current_note = notes_order[(current_note == 'B' or current_note == 'E') * semitone + (current_note != 'B' and current_note != 'E') * tone]
            scale_notes.append(current_note)
        
        if all(note in scale_notes for note in notes):
            scales.append(scale_notes[0])
    
    if not scales:
        return "none"
    
    return ' '.join(scales)

# Input
n = int(input())
notes = input().split()

# Output
print(find_major_scales(n, notes))
