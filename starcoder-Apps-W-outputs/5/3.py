
def dfs(house,house_dict,visited):
    visited.append(house)
    if house in house_dict:
        for neighbor in house_dict[house]:
            if neighbor not in visited:
                dfs(neighbor,house_dict,visited)
house, cables = map(int, input().split())
house_dict = {}
for _ in range(cables):
    house1, house2 = map(int, input().split())
    if house1 not in house_dict:
        house_dict[house1] = [house2]
    else:
        house_dict[house1].append(house2)
    if house2 not in house_dict:
        house_dict[house2] = [house1]
    else:
        house_dict[house2].append(house1)

visited = []
dfs(1,house_dict,visited)

if house == len(visited):
    print("Connected")
else:
    for house in range(1, house+1):
        if house not in visited:
            print(house)
