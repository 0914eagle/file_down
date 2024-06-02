
def main():
    n = int(input())
    stock = 0
    cost = 0
    for i in range(n):
        event = input().split()
        if event[0] == 'buy':
            stock += int(event[1])
            cost += int(event[1]) * int(event[2])
        elif event[0] == 'sell':
            stock -= int(event[1])
            cost -= int(event[1]) * int(event[2])
        elif event[0] == 'split':
            cost *= int(event[1])
        elif event[0] == 'merge':
            cost //= int(event[1])
        elif event[0] == 'die':
            cost //= stock
            stock = 0
            print(cost * int(event[1]) * 0.7)

main()

