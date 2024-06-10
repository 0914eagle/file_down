
def tapeart(n, c):
    tape = {}
    for i in range(n):
        if c[i] not in tape:
            tape[c[i]] = [i+1, i+1]
        else:
            tape[c[i]][1] = i+1
    
    tape_list = list(tape.values())
    tape_list = sorted(tape_list, key=lambda x: x[0])
    
    for i in range(len(tape_list)-1):
        if tape_list[i][1] > tape_list[i+1][0]:
            return "IMPOSSIBLE"
    
    return len(tape_list)
n = int(input())
c = list(map(int, input().split()))
print(tapeart(n, c))

