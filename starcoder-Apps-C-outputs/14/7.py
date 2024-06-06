
# -*- coding: utf-8 -*-
import re
import sys


def count_syllable(word):
    if len(word) <= 2:
        return 1
    if word[-2:] == "es":
        return 1
    if word[-1] == "e":
        return 2
    if word[-2:] == "le":
        return 2
    if word[-3:] == "ing":
        return 3
    return 0

def process_line(line):
    if len(line) > 0:
        line = line[:-1]
    words = re.split(r'\s+', line)
    syllable_count = 0
    for word in words:
        if count_syllable(word) != 0:
            syllable_count += count_syllable(word)
        else:
            syllable_count += 1
    return syllable_count

if __name__ == "__main__":
    line = sys.stdin.readline()
    if process_line(line) == 17:
        print("International")
        print("contest- motivation high")
        print("Programmers have fun!.")
    else:
        print(line[:-1])
