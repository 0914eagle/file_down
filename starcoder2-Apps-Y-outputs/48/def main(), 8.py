
def main():
    # read input
    events = []
    while True:
        line = input()
        if line == 'die':
            break
        events.append(line)
    # process events
    shares = 0
    cost = 0
    for event in events:
        if event.startswith('buy'):
            x, y = event.split()[1:]
            x = int(x)
            y = int(y)
            shares += x
            cost += x * y
        elif event.startswith('sell'):
            x, y = event.split()[1:]
            x = int(x)
            y = int(y)
            shares -= x
            cost -= x * y
        elif event.startswith('split'):
            x = int(event.split()[1])
            shares *= x
            cost /= x
        elif event.startswith('merge'):
            x = int(event.split()[1])
            shares //= x
            cost *= x
    # compute final sale
    y = int(input())
    profit = shares * y - cost
    tax = profit * 0.3
    print(shares * (y - tax))

if __name__ == '__main__':
    main()

