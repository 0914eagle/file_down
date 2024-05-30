
def find_girl_name(N, boys, A, B):
    odd_nums = [i for i in range(A, B+1) if i % 2 != 0]
    max_distance = -1
    chosen_num = -1
    for num in odd_nums:
        min_distance = min([abs(num - boy) for boy in boys])
        if min_distance > max_distance:
            max_distance = min_distance
            chosen_num = num
    return chosen_num

# Input
N = int(input())
boys = list(map(int, input().split()))
A, B = map(int, input().split())

# Output
print(find_girl_name(N, boys, A, B))
```
