
for _ in range(int(input())):
    n = int(input())
    people = [tuple(map(int, input().split())) for _ in range(n)]
    max_ppl = 0
    for a in range(10001):
        for b in range(10001):
            for c in range(10001):
                if a + b + c > 10000:
                    break
                ppl = sum(a <= A and b <= B and c <= C for A, B, C in people)
                max_ppl = max(max_ppl, ppl)
    print(f'Case #{_+1}: {max_ppl}')

