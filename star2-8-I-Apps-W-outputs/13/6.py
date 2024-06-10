
import sys
read = sys.stdin.readline

def main():
    n, t = map(int, read().split())
    arr = list(map(int, read().split()))
    
    if t == 1:
        print(7)
        
    elif t == 2:
        if arr[0] > arr[1]:
            print("Bigger")
        elif arr[0] == arr[1]:
            print("Equal")
        else:
            print("Smaller")
            
    elif t == 3:
        temp = sorted(arr[:3])
        print(temp[1])
        
    elif t == 4:
        print(sum(arr))
        
    elif t == 5:
        print(sum([x for x in arr if x % 2 == 0]))
        
    elif t == 6:
        print("".join([chr(x%26+ord("a")) for x in arr]))
        
    elif t == 7:
        i = 0
        while True:
            if i < 0 or i >= n:
                print("Out")
                break
            elif i == n-1:
                print("Done")
                break
            else:
                i = arr[i]
main()

