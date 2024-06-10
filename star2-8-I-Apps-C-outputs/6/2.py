
import sys

def maximum_blue_lemonade(children):
    
    pass

def main():
    num_children = int(sys.stdin.readline().strip())
    children = []
    for _ in range(num_children):
        offer, want, rate = sys.stdin.readline().strip().split()
        children.append({'offer': offer, 'want': want, 'rate': float(rate)})
    max_blue_lemonade = maximum_blue_lemonade(children)
    print(max_blue_lemonade)

if __name__ == '__main__':
    main()

