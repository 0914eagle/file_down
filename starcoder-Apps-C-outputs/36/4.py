

def unlock(rooms, switches, lock_to_room):
    start = 0
    end = 0
    room_to_switch = {}
    for lock in lock_to_room:
        if len(lock_to_room[lock]) == 1:
            switch = lock_to_room[lock].pop()
            end ^= switches[switch]
            room_to_switch[lock] = switch
    while start != end:
        switch = room_to_switch[start]
        start ^= switches[switch]
        for room in lock_to_room[switch]:
            room_to_switch[room] = switch
            start ^= switches[switch]

    return start == end


n, m = [int(x) for x in input().strip().split()]
rooms = [int(x) for x in input().strip().split()]

switches = []
lock_to_room = {}
for i in range(1, m+1):
    t = [int(x) for x in input().strip().split()]
    switches.append(2 ** (t[0] - 1))
    for r in t[1:]:
        if r in lock_to_room:
            lock_to_room[r].add(i)
        else:
            lock_to_room[r] = set([i])

print("YES" if unlock(rooms, switches, lock_to_room) else "NO")

