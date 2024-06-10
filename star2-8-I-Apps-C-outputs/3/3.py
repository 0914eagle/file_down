
def max_damage(pillars):
    n = len(pillars)
    left_max = [0] * n
    left_max[0] = pillars[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], pillars[i])

    right_max = [0] * n
    right_max[n-1] = pillars[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], pillars[i])
    
    damage = 0
    destroy_pillar = -1
    for i in range(1, n-1):
        if left_max[i-1] + right_max[i+1] - pillars[i] > damage:
            damage = left_max[i-1] + right_max[i+1] - pillars[i]
            destroy_pillar = i
    
    return damage, destroy_pillar
    
if __name__ == '__main__':
    n = int(input())
    pillars = list(map(int, input().split()))
    damage, destroy_pillar = max_damage(pillars)
    print(damage, destroy_pillar)

