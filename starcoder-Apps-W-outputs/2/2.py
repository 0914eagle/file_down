
n, h, m, k = [int(x) for x in input().split()]

freight_trains = []

for _ in range(n):
    h_i, m_i = [int(x) for x in input().split()]
    freight_trains.append((h_i, m_i))

freight_trains.sort()

passenger_trams = []

for h_i, m_i in freight_trains:
    if m_i - k >= 0:
        passenger_trams.append((h_i, m_i - k))
    if m_i + k < m:
        passenger_trams.append((h_i, m_i + k))

passenger_trams.sort()

max_tram = 0

for h_i, m_i in passenger_trams:
    max_tram = max(max_tram, m_i)

    for i in range(n):
        if (h_i, m_i) == freight_trains[i]:
            freight_trains[i] = (-1, -1)
            break

min_tram = -1

for h_i, m_i in passenger_trams:
    min_tram = min(min_tram, m_i)

    for i in range(n):
        if (h_i, m_i) == freight_trains[i]:
            freight_trains[i] = (-1, -1)
            break

if max_tram > min_tram:
    print(n)
else:
    print(n - 1)

for i in range(n):
    if freight_trains[i] != (-1, -1):
        print(i + 1)
