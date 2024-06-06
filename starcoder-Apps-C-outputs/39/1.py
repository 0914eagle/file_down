
from queue import PriorityQueue

n, g = [int(n) for n in input().split()]

class Station(object):
    def __init__(self, distance, cost):
        self.distance = distance
        self.cost = cost
    
    def __lt__(self, other):
        return self.cost < other.cost

stations = PriorityQueue()

for _ in range(n):
    d, c = [int(n) for n in input().split()]
    stations.put(Station(d, c))

cost = 0
tank = 0
while not stations.empty():
    station = stations.get()

    fuel = tank * (station.distance - stations.get().distance)
    if fuel < 0:
        cost += abs(fuel) * station.cost
        tank = 0
    else:
        tank = g

    if stations.empty():
        break

if tank == 0:
    print('cancel road trip')
else:
    print(cost)

