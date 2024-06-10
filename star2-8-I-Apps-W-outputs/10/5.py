
n = int(input())
angles = list(map(int, input().split()))
angles.sort(reverse=True)
vasya = angles[:n//2]
petya = angles[n//2:]
print(abs(sum(vasya) - sum(petya)))

