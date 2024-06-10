

def get_robot_image(w, h):
    return [[int(x) for x in input().split()] for _ in range(h)]

def get_floor_image(w, h):
    return [[int(x) for x in input().split()] for _ in range(h)]

def find_candidate_locations(robot_image, floor_image):
    w_robot, h_robot = len(robot_image[0]), len(robot_image)
    w_floor, h_floor = len(floor_image[0]), len(floor_image)
    if w_robot > w_floor or h_robot > h_floor:
        return []
    best_matches = []
    best_score = 0
    for y in range(h_floor - h_robot + 1):
        for x in range(w_floor - w_robot + 1):
            score = 0
            for dy in range(h_robot):
                for dx in range(w_robot):
                    if robot_image[dy][dx] == floor_image[y+dy][x+dx]:
                        score += 1
            if score > best_score:
                best_matches = [(x, y)]
                best_score = score
            elif score == best_score:
                best_matches.append((x, y))
    return best_matches

w_robot, h_robot = [int(x) for x in input().split()]
robot_image = get_robot_image(w_robot, h_robot)
w_floor, h_floor = [int(x) for x in input().split()]
floor_image = get_floor_image(w_floor, h_floor)
candidate_locations = find_candidate_locations(robot_image, floor_image)
for x, y in candidate_locations:
    print(x, y)

