
def min_explosions(N, A, B, monsters):
    monsters.sort(reverse=True)
    count = 0
    for i in range(N):
        if monsters[i] > 0:
            if monsters[i] <= A:
                monsters[i] = 0
            else:
                explosions_needed = (monsters[i] - A) // (A - B)
                if (monsters[i] - A) % (A - B) != 0:
                    explosions_needed += 1
                count += explosions_needed
                monsters[i] -= explosions_needed * (A - B)
                if monsters[i] < 0:
                    monsters[i] = 0
            for j in range(i+1, N):
                if monsters[j] > 0:
                    monsters[j] -= B
                    if monsters[j] < 0:
                        monsters[j] = 0
    return count

# Read input
N, A, B = map(int, input().split())
monsters = [int(input()) for _ in range(N)]

# Call the function and print the result
print(min_explosions(N, A, B, monsters))
```
