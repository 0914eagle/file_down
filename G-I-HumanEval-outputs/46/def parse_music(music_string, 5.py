
from typing import List

def parse_music(music_string: str) -> List[int]:
    beats_mapping = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    notes = music_string.split()
    beats_list = [beats_mapping[elem] for elem in notes]

    return beats_list
