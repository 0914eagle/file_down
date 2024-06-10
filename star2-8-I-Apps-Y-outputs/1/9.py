
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

def can_color(a, k):
    count = [0 for _ in range(k)]
    for el in a:
        if el > k:
            return False
        count[el - 1] += 1
    return all([el > 0 for el in count])

if can_color(a, k):
    print("YES")
    print(" ".join(map(str, a)))
else:
    print("NO")

