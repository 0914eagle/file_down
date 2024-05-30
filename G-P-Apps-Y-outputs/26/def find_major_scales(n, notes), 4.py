
def find_major_scales(n, notes):
    major_scales = {
        "A": ["A", "B", "C#", "D", "E", "F#", "G#"],
        "A#": ["A#", "C", "D", "D#", "F", "G", "A"],
        "B": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
        "C": ["C", "D", "E", "F", "G", "A", "B"],
        "C#": ["C#", "D#", "F", "F#", "G#", "A#", "C"],
        "D": ["D", "E", "F#", "G", "A", "B", "C#"],
        "D#": ["D#", "F", "G", "G#", "A#", "C", "D"],
        "E": ["E", "F#", "G#", "A", "B", "C#", "D#"],
        "F": ["F", "G", "A", "A#", "C", "D", "E"],
        "F#": ["F#", "G#", "A#", "B", "C#", "D#", "F"],
        "G": ["G", "A", "B", "C", "D", "E", "F#"],
        "G#": ["G#", "A#", "C", "C#", "D#", "F", "G"]
    }
    
    scales = []
    
    for scale, notes_list in major_scales.items():
        valid_scale = True
        for i in range(n):
            if notes[i] not in notes_list:
                valid_scale = False
                break
        if valid_scale:
            scales.append(scale)
    
    if not scales:
        print("none")
    else:
        print(" ".join(sorted(scales)))

# Input
n = int(input())
notes = input().strip().split()

# Call the function
find_major_scales(n, notes)
```
