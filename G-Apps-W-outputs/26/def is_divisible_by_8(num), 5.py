
def is_divisible_by_8(num):
    if int(num) % 8 == 0:
        return True
    return False

def remove_digits(n):
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            for k in range(j + 1, len(n)):
                num = n[:i] + n[j] + n[k]
                if is_divisible_by_8(num):
                    return num
    return "NO"

n = input().strip()

result = remove_digits(n)

if result == "NO":
    print("NO")
else:
    print("YES")
    print(result)
