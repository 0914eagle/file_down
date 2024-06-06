
while True:
    try:
        length, distance, num = map(int, input().split())
        birds = [int(input()) for i in range(num)]
        birds.sort()
        max_num = 0
        j = 0
        for i in range(num):
            while j < num and birds[j] - birds[i] < distance:
                j += 1
            max_num = max(max_num, j - i - 1)
        print(max_num)
    except:
        break
