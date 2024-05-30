
def find_major_scales(n, notes):
    all_notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    scales = []
    
    for start_note in all_notes:
        scale = [start_note]
        current_note_index = all_notes.index(start_note)
        interval_pattern = [2, 2, 1, 2, 2, 2, 1]
        valid_scale = True
        
        for i in range(1, n):
            current_note_index = (current_note_index + interval_pattern[i % len(interval_pattern)]) % 12
            scale.append(all_notes[current_note_index])
        
        if set(notes).issubset(set(scale)):
            scales.append(" ".join(scale))
    
    if not scales:
        return "none"
    
    return " ".join(sorted(scales))

# Read input
n = int(input())
notes = input().split()

# Call the function and print the output
print(find_major_scales(n, notes))
```
