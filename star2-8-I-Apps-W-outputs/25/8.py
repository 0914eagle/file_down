
def main():
    n, m, k = map(int, input().split())
    buildings = [0] * m
    for _ in range(n):
        i = int(input())
        buildings[i - 1] += 1
    
    buildings.sort(reverse=True)
    
    total_noise = sum(buildings)
    for i in range(k):
        total_noise -= buildings[i]
    
    print(total_noise)
    
main()

