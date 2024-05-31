
def find_possible_names(n, k, notes):
    names = []
    
    for i in range(n):
        if i < k-1:
            names.append(chr(ord('A') + i))
        else:
            if notes[i-k+1] == "YES":
                names.append(names[-k+1])
            else:
                names.append(chr(ord('A') + i))
    
    return ' '.join([name + "bcdefghijklmno" for name in names])

# Input
n, k = map(int, input().split())
notes = input().split()

# Output
print(find_possible_names(n, k, notes))
