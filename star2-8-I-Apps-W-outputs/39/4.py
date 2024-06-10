
def solve(n, s, arrival):
    arrival.sort(key=lambda x: x[1]) # sort by time of arrival
    
    time = 0
    for floor, t in arrival:
        time += (abs(floor - s) + time - t) # time to go down + time to wait for passenger
        s = floor # update current floor
    
    return time

