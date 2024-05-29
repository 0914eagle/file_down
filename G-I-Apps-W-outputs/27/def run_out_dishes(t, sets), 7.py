
def run_out_dishes(t, sets):
    for s in sets:
        m, k = s[0]
        portions = s[1]
        observations = s[2:]

        remaining_portions = portions[:]
        choices = [True] * k

        for i in range(m - 1):
            dish, disappointed = observations[i]
            if dish == 0:
                continue

            if disappointed:
                choices[dish - 1] = False

            remaining_portions[dish - 1] -= 1
            if remaining_portions[dish - 1] == 0:
                choices[dish - 1] = False

        output = 'Y' if choices[0] else 'N'
        for c in choices[1:]:
            output += 'Y' if c else 'N'
        print(output)

t = int(input())
sets = []
for _ in range(t):
    input()
    m, k = map(int, input().split())
    portions = list(map(int, input().split()))
    observations = [tuple(map(int, input().split())) for _ in range(m - 1)]
    sets.append((m, k, portions, observations))

run_out_dishes(t, sets)
```
