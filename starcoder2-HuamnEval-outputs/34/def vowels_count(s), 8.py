
 def vowels_count(s):
    vowels = "aeiou"
    count = 0
    for letter in s.lower():
        if letter in vowels:
            count += 1
    return count
 