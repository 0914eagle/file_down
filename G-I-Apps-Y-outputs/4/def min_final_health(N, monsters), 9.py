
import sys

def min_final_health(N, monsters):
    return min(monsters)

if __name__ == "__main__":
    input_lines = sys.stdin.read().strip().split("\n")
    N = int(input_lines[0])
    monsters = list(map(int, input_lines[1].split()))
    print(min_final_health(N, monsters))
``` 
