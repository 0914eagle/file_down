
from typing import List

def parse_music(music_string: str) -> List[int]:
    beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    notes = music_string.split()
    return [beats[note] for note in notes]

# Test the function with the example
print(parse_music('o o| .| o| o| .| .| .| .| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
