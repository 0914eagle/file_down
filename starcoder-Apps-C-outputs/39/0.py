
def minimum_fuel_cost(station, capacity):
    fuel_cost = 0
    start = capacity
    for station_id, station_data in enumerate(station):
        distance, cost = station_data
        travelled_distance = min(start, distance)
        start -= travelled_distance
        if start == 0:
            fuel_cost += cost
            start = capacity
            if station_id == len(station) - 1:
                break
        else:
            if station_id == len(station) - 1:
                return "cancel road trip"
            elif station[station_id + 1][0] > distance:
                return "cancel road trip"
    return fuel_cost

n, g = [int(x) for x in input().split()]
stations = []
for _ in range(n):
    stations.append([int(x) for x in input().split()])
stations.sort(key=lambda x: x[0])

print(minimum_fuel_cost(stations, g))

