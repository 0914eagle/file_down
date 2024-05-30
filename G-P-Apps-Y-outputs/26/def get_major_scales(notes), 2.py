
def get_major_scales(notes):
    scales = {
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
    for scale, scale_notes in scales.items():
        if all(note in scale_notes for note in notes):
            possible_scales.append(scale)

    return possible_scales

n = int(input())
notes = input().split()
result = get_major_scales(notes)

if len(result) == 0:
    print('none')
else:
    print(' '.join(sorted(result)))
```
