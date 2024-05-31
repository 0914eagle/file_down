
def is_divisible_by_8(number):
    return int(number) % 8 == 0

def solve_divisible_by_8(n):
    n = str(n)
    n_len = len(n)

    if n_len <= 2:
        if is_divisible_by_8(n):
            print("YES")
            print(n)
        else:
            print("NO")
    else:
        for i in range(n_len):
            for j in range(i + 1, n_len):
                for k in range(j + 1, n_len):
                    num = int(n[:i] + n[i+1:j] + n[j+1:k] + n[k+1:])
                    if is_divisible_by_8(num):
                        print("YES")
                        print(num)
                        return
        print("NO")

# Input
n = input()
solve_divisible_by_8(n)
