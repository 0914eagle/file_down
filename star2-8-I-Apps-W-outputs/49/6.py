
def main():
    n, k = list(map(int, input().split()))
    h = list(map(int, input().split()))
    correct = [0] * n
    for i in range(n):
        correct[(i+1) % n] = h[i]
    valid = 0
    for i in range(k**n):
        binary = bin(i)[2:].rjust(n, "0")
        answer = [int(c) for c in binary]
        if answer.count(1) == n:
            continue
        total = 0
        for j in range(n):
            if answer[j] == correct[j]:
                total += 1
        if total > answer.count(1):
            valid += 1
    print(valid % 998244353)

main()

