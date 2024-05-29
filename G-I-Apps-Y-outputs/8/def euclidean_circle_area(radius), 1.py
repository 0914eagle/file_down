
import math

def euclidean_circle_area(radius):
    return math.pi * radius**2

def taxi_circle_area(radius):
    return 2 * radius**2

def main():
    radius = int(input())
    euclidean_area = euclidean_circle_area(radius)
    taxi_area = taxi_circle_area(radius)

    print("{:.6f}".format(euclidean_area))
    print("{:.6f}".format(taxi_area))

if __name__ == "__main__":
    main()
```
