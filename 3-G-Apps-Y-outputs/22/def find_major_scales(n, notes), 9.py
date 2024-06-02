
def find_major_scales(n, notes):
    notes_order = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    scales = []
    
    for i in range(12):
        scale_notes = [notes_order[(i+j)%12] for j in [0, 2, 4, 5, 7, 9, 11, 12]]
        if all(note in scale_notes for note in notes):
            scales.append(notes_order[i])
    
    return scales if scales else ['none']

# Input
n = int(input())
notes = input().split()

# Output
result = find_major_scales(n, notes)
print(' '.join(result))
