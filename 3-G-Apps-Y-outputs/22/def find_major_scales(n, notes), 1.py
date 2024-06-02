
def find_major_scales(n, notes):
    notes_order = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    scales = []
    
    for i in range(12):
        scale = []
        current_note = notes_order[i]
        scale.append(current_note)
        
        tone = (i + 2) % 12
        semitone = (i + 1) % 12
        
        for j in range(6):
            if notes_order[tone] in notes:
                scale.append(notes_order[tone])
            else:
                break
            if j == 2:
                if notes_order[semitone] in notes:
                    scale.append(notes_order[semitone])
                else:
                    break
            tone = (tone + 2) % 12
            semitone = (semitone + 1) % 12
        
        if len(scale) == 8:
            scales.append(scale[0])
    
    if not scales:
        print("none")
    else:
        print(" ".join(scales))

# Input
n = int(input())
notes = input().split()

# Function call
find_major_scales(n, notes)
