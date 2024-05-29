
from typing import List

def parse_music(music_string: str) -> List[int]:
    beats = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    return [beats[note] for note in notes]

input_string = 'o o| .| o| o| .| .| .| .| o o'
output = parse_music(input_string)
print(output)
