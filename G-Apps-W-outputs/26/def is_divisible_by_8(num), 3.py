
def is_divisible_by_8(num):
    for i in range(0, len(num)):
        for j in range(i+1, len(num)):
            for k in range(j+1, len(num)):
                current_num = int(num[i] + num[j] + num[k])
                if current_num % 8 == 0:
                    return str(current_num)
    return "NO"

n = input().strip()

result = is_divisible_by_8(n)

if result != "NO":
    print("YES")
    print(result)
else:
    print("NO")
