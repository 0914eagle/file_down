
def catch_criminals(n, a, criminal_cities):
    total_criminals = 0

    for i in range(n):
        dist = abs(a - i + 1)
        if dist != 0 and criminal_cities[i] == 1:
            total_criminals += 1

    return total_criminals

# Input processing
n, a = map(int, input().split())
criminal_cities = list(map(int, input().split()))

result = catch_criminals(n, a, criminal_cities)
print(result)
