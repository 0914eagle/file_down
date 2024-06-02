
def find_major_scales(n, notes):
    notes_order = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    scales = []
    
    for i in range(12):
        scale_notes = [notes_order[i]]
        current_index = i
        intervals = [2, 2, 1, 2, 2, 2, 1]
        
        for interval in intervals:
            current_index = (current_index + interval) % 12
            scale_notes.append(notes_order[current_index])
        
        scale_notes.append(scale_notes[0])  # Repeat the first note at the end
        if all(note in scale_notes for note in notes):
            scales.append(scale_notes[0])
    
    if scales:
        return ' '.join(sorted(scales))
    else:
        return 'none'

# Input reading
n = int(input())
notes = input().split()

# Call the function and print the output
print(find_major_scales(n, notes))
