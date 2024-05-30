
def find_major_scales(n, notes):
    notes_list = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    major_scales = {
        'A': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
        'A#': ['A#', 'C', 'D', 'D#', 'F', 'G', 'A'],
        'B': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'],
        'C': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
        'C#': ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C'],
        'D': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
        'D#': ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D'],
        'E': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
        'F': ['F', 'G', 'A', 'A#', 'C', 'D', 'E'],
        'F#': ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F'],
        'G': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
        'G#': ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']
    }
    
    possible_scales = set()
    
    for scale, notes_in_scale in major_scales.items():
        valid_scale = True
        for i in range(n):
            note = notes[i % n]
            if note not in notes_in_scale:
                valid_scale = False
                break
        if valid_scale:
            possible_scales.add(scale)
    
    if not possible_scales:
        return "none"
    else:
        return ' '.join(sorted(possible_scales))

# Input reading and function call
n = int(input())
notes = input().split()
result = find_major_scales(n, notes)
print(result)
```
