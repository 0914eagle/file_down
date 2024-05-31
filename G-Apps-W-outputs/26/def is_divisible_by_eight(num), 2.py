
def is_divisible_by_eight(num):
    if int(num) % 8 == 0:
        return True
    return False

def find_divisible_by_eight(num):
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            for k in range(j+1, len(num)):
                temp_num = num[:i] + num[j] + num[j+1:k] + num[i] + num[k:]
                if temp_num[0] != '0' and is_divisible_by_eight(temp_num):
                    return temp_num
    return None

n = input().strip()

result = find_divisible_by_eight(n)

if result:
    print("YES")
    print(result)
else:
    print("NO")
