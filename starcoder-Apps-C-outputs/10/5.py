
def input_int_list():
    return list(map(int, input().split()))


def get_subordinate(subordinates, id):
    if id in subordinates:
        return subordinates[id]
    return set()


def get_boss(b, id):
    if id in b:
        return b[id]
    return -1


def main():
    m, q = input_int_list()

    # people who earn more than the current person and are taller
    b = dict()
    # people who earn less than the current person and are taller
    subordinates = dict()

    for _ in range(m):
        id, salary, height = input_int_list()
        b[id] = -1
        subordinates[id] = set()
        for k in subordinates:
            if subordinates[k] is None:
                subordinates[k] = set()
            if salary > subordinates[k][0] and height > subordinates[k][1]:
                subordinates[id].add((salary, height))
        for k in b:
            if b[k] is None:
                b[k] = -1
            if salary < b[k][0] and height > b[k][1]:
                subordinates[id] = set()
                b[id] = k
                subordinates[k].add((salary, height))
    for _ in range(q):
        id = int(input())
        print('{} {}'.format(get_boss(b, id), len(get_subordinate(subordinates, id))))


main()
