
def find_major_scales(n, song):
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    
    def get_scale_notes(root_note):
        scale_notes = []
        idx = notes.index(root_note)
        scale_notes.append(notes[idx])
        interval = [2, 2, 1, 2, 2, 2, 1]
        for i in interval:
            idx = (idx + i) % 12
            scale_notes.append(notes[idx])
        return scale_notes
    
    possible_scales = []
    
    for note in notes:
        scale_notes = get_scale_notes(note)
        valid_scale = True
        for n in song:
            if n not in scale_notes:
                valid_scale = False
                break
        if valid_scale:
            possible_scales.append(note)
    
    if possible_scales:
        return ' '.join(possible_scales)
    else:
        return 'none'

# Input processing
n = int(input())
song = input().split()

# Call the function and output the result
print(find_major_scales(n, song))
```
