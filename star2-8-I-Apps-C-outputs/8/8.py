
def min_moves_to_sort(railway_cars):
    
    sorted_cars = sorted(railway_cars)
    moves = 0
    for car in sorted_cars:
        if car not in railway_cars:
            moves += 1
        else:
            railway_cars.remove(car)
    return moves

if __name__ == "__main__":
    num_cars = int(input())
    railway_cars = list(map(int, input().split()))
    print(min_moves_to_sort(railway_cars))

