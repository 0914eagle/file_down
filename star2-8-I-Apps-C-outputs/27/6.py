
def count_consecutive(num_list):
    count = 0
    max_count = 0
    for i in range(1, len(num_list)):
        if num_list[i] == num_list[i-1]:
            count += 1
        else:
            count = 0
        max_count = max(max_count, count)
    return max_count + 1

n = int(input())
num_list = list(map(int, input().split()))
print(count_consecutive(num_list))

