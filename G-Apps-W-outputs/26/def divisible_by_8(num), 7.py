
def divisible_by_8(num):
    for i in range(0, len(num)):
        for j in range(i+1, len(num)):
            for k in range(j+1, len(num)):
                temp_num = int(num[i] + num[j] + num[k])
                if temp_num % 8 == 0:
                    return temp_num
    return -1

n = input().strip()

result = divisible_by_8(n)

if result != -1:
    print("YES")
    print(result)
else:
    print("NO")
