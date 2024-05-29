
def check_coinciding_tracks(n, L, kefa_barriers, sasha_barriers):
    def shift_list(lst, shift):
        return lst[-shift:] + lst[:-shift]

    for i in range(1, L):
        shifted_kefa = shift_list(kefa_barriers, i)
        if shifted_kefa == sasha_barriers:
            return "YES"

    return "NO"

# Read input
n, L = map(int, input().split())
kefa_barriers = list(map(int, input().split()))
sasha_barriers = list(map(int, input().split()))

# Check if tracks coincide and print the result
print(check_coinciding_tracks(n, L, kefa_barriers, sasha_barriers))
```
