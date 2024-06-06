
def get_input():
    n, m = list(map(int, input().split()))
    ship_list = []
    for i in range(m):
        x1, x2, y = list(map(int, input().split()))
        ship_list.append([x1, x2, y])
    return n, ship_list

def check(n, ship_list):
    # 각각의 밴드별로 탐색하면서 좌표가 있는지 확인
    band_list = []
    min_y = 0
    max_y = 0
    for i in range(n):
        band_list.append([])
        for j in range(3):
            if (j == 1):
                min_y = i + 1
            elif (j == 2):
                max_y = i + 1
            for ship in ship_list:
                if (min_y <= ship[2] and ship[2] <= max_y):
                    band_list[i].append(ship)
    
    # 좌표가 없다면 해당 방향 탐색
    # 좌표가 있다면 해당 좌표는 불가능
    # 모든 좌표를 탐색한 후
    # 좌표가 없다면 해당 방향 탐색
    # 좌표가 있다면 해당 좌표는 불가능
    # 모든 좌표를 탐색한 후
    # 좌표가 없다면 해당 방향 탐색
    # 좌표가 있다면 해당 좌표는 불가능
    # 모든 좌표를 탐색한 후
    # 좌표가 없다면 불가능
    # 좌표가 있다면 가능
    for i in range(n):
        if (not band_list[i]):
            return False
    
    return True

def solution(n, ship_list):
    answer = ''
    for i in range(n):
        if (i == 0):
            answer += '-'
        else:
            answer += '+'
    
    if (check(n, ship_list)):
        print(answer)
    else:
        print('impossible')

if __name__ == '__main__':
    n, ship_list = get_input()
    solution(n, ship_list)
