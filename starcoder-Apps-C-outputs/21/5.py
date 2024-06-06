
def beautiful_sequence(a, b, c, d):
    # write your code here
    if a == 0 and b == 0 and c == 0:
        print("YES")
        print(*[3] * d)
    elif b == 0 and c == 0 and d == 0:
        print("YES")
        print(*[0] * a)
    elif a == 0 and c == 0 and d == 0:
        print("YES")
        print(*[1] * b)
    elif a == 0 and b == 0 and d == 0:
        print("YES")
        print(*[2] * c)
    else:
        print("NO")

if __name__ == "__main__":
    a, b, c, d = map(int, input().split())
    beautiful_sequence(a, b, c, d)
