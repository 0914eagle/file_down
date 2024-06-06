
import string
import re

words = ["be", "our", "rum", "will", "dead", "hook", "ship", "blood", "sable", "avenge", "parrot", "captain"]

encrypted = input()

encrypted_set = set()
for char in encrypted:
    encrypted_set.add(char)

possible = True
for word in words:
    for char in word:
        if char not in encrypted_set:
            possible = False
            break
    if not possible:
        break

if possible:
    print("possible")
else:
    print("Impossible")

