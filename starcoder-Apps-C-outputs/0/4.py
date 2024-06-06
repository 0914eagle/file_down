
import math

def main():
    x,y = map(float, input().split())
    v,w = map(float, input().split())
    dis = math.sqrt(x**2 + y**2)
    print(max(dis/v, (math.pi - math.acos(x/dis))/w))


if __name__ == '__main__':
    main()
