

def game(N, E, D, e, d):
    if N == 1:
        return -1
    
    exploding_kittens = [e[i] - i for i in range(E)]
    defuses = [d[i] - i for i in range(D)]
    
    curr = 0
    curr_round = 1
    
    while len(exploding_kittens) > 0:
        if exploding_kittens[0] == 0:
            if len(defuses) > 0 and defuses[0] == 0:
                exploding_kittens.pop(0)
                defuses.pop(0)
            else:
                curr += 1
                curr %= N
                curr_round += 1
        else:
            exploding_kittens[0] -= 1
        
        if len(exploding_kittens) > 0 and exploding_kittens[0] == 0:
            if len(defuses) > 0 and defuses[0] == 0:
                exploding_kittens.pop(0)
                defuses.pop(0)
            else:
                curr += 1
                curr %= N
                curr_round += 1
        
    return curr

N, E, D = map(int, input().split())
e = list(map(int, input().split()))
d = list(map(int, input().split()))

print(game(N, E, D, e, d))


