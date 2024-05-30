
def find_major_scales(n, notes):
    def get_scale(note):
        scale = []
        idx = notes.index(note)
        for interval in [2, 2, 1, 2, 2, 2, 1]:
            idx = (idx + interval) % len(notes)
            scale.append(notes[idx])
        return scale

    scales = []
    for note in notes:
        possible_scale = get_scale(note)
        if all(note in possible_scale for note in notes):
            scales.append(''.join(possible_scale))

    return sorted(scales) if scales else ['none']

# Input
n = int(input())
notes = input().split()

# Output
result = find_major_scales(n, notes)
print(' '.join(result))
```
