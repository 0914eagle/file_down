
n, m = map(int, input().split())
words = [input().split() for _ in range(n)]

def is_ordered(words):
    for i in range(1, len(words)):
        if words[i] < words[i-1]:
            return False
    return True

if is_ordered(words):
    print("Yes")
    print(0)
else:
    print("No")

