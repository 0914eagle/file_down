
def next_permutation(num):
    num_list = list(str(num))
    i = len(num_list) - 1
    while i > 0:
        if num_list[i - 1] < num_list[i]:
            break
        i -= 1
    if i == 0:
        return 0
    j = len(num_list) - 1
    while num_list[j] <= num_list[i - 1]:
        j -= 1
    num_list[i - 1], num_list[j] = num_list[j], num_list[i - 1]
    num_list[i:] = num_list[len(num_list) - 1:i - 1:-1]
    return int(''.join(num_list))

num = int(input())
print(next_permutation(num))

