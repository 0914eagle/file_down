
'''
input:
    ex eoii jpxbmx cvz uxju sjzzcn jzz
output:
    we will avenge our dead parrot arr
'''

import sys

words = ["be", "our", "rum", "will", "dead", "hook", "ship", "blood", "sable", "avenge", "parrot", "captain"]

def main():
    input = sys.stdin.readline().split()
    input_list = ''.join(input)

    for word in words:
        if word not in input_list:
            print("Impossible")
            return
    
    words_len = []
    for word in words:
        words_len.append(len(word))

    input_len = []
    for s in input:
        input_len.append(len(s))
    
    if len(set(words_len)) != len(set(input_len)):
        print("Impossible")
        return
    
    replace_map = {}
    for s, word in zip(input, words):
        for i in range(len(s)):
            replace_map[s[i]] = word[i]

    output = []
    for s in input:
        output.append(s.translate(str.maketrans(replace_map)))
    
    print(" ".join(output))

if __name__ == "__main__":
    main()
