
mod = 998244353

def count_monotonic_renumerations(n, a):
    a_count = {}
    for num in a:
        if num in a_count:
            a_count[num] += 1
        else:
            a_count[num] = 1

    unique_counts = sorted(list(set(a_count.values())))

    count_dict = {}
    for count in unique_counts:
        count_dict[count] = 1

    for i in range(1, len(unique_counts)):
        if unique_counts[i] == unique_counts[i-1]:
            count_dict[unique_counts[i]] = count_dict[unique_counts[i-1]]
        else:
            count_dict[unique_counts[i]] = count_dict[unique_counts[i-1]] + count_dict[unique_counts[i]]

    total_count = 1
    for count in a_count.values():
        total_count = (total_count * count_dict[count]) % mod

    return total_count

# Input reading and function call
n = int(input())
a = list(map(int, input().split()))
print(count_monotonic_renumerations(n, a))
```
