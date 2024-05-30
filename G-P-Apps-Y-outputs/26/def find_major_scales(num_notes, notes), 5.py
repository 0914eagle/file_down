
def find_major_scales(num_notes, notes):
    musical_notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    scales = []
    
    for root_note in musical_notes:
        scale = [root_note]
        current_note = root_note
        intervals = [2, 2, 1, 2, 2, 2, 1]
        
        for interval in intervals:
            current_index = musical_notes.index(current_note)
            next_index = (current_index + interval) % len(musical_notes)
            current_note = musical_notes[next_index]
            scale.append(current_note)
        
        if all(note in scale for note in notes):
            scales.append(root_note)
    
    return scales if scales else ['none']

# Input processing
input_str = input().strip()
num_notes, notes_str = map(str, input_str.split('\n'))
notes = notes_str.split()

# Call the function and print the output
result = find_major_scales(int(num_notes), notes)
print(' '.join(result))
```
