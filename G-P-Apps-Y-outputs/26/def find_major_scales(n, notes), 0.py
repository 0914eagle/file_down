
def find_major_scales(n, notes):
    major_scales = {
        'A': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
        'A#': ['A#', 'C', 'D', 'D#', 'F', 'G', 'A'],
        'B': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'],
        'C': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
        'C#': ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C'],
        'D': ['D', 'E', 'F#', 'G', 'A', 'A#', 'C#'],
        'D#': ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D'],
        'E': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
        'F': ['F', 'G', 'A', 'A#', 'C', 'D', 'E'],
        'F#': ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F'],
        'G': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
        'G#': ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']
    }

    possible_scales = []
    for scale, notes_list in major_scales.items():
        if all(note in notes_list for note in notes):
            possible_scales.append(scale)

    return ' '.join(sorted(possible_scales)) if possible_scales else 'none'

# Input handling
n = int(input())
notes = input().split()

# Output
print(find_major_scales(n, notes))
```
