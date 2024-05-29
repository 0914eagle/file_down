
from typing import List

def parse_music(music_string: str) -> List[int]:
    durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    notes = music_string.split()
    result = [durations[notes[i]] for i in range(len(notes))]
    
    return result

# Test the function
print(parse_music('o o| .| o| o| .| .| .| .| o o'))
