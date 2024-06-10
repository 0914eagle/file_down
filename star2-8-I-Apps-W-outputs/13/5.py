
import sys

if __name__ == '__main__':
    n, t = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    if t == 1:
        print(7)
        
    elif t == 2:
        if a[0] > a[1]:
            print('Bigger')
        elif a[0] == a[1]:
            print('Equal')
        else:
            print('Smaller')
            
    elif t == 3:
        b = [a[0], a[1], a[2]]
        b.sort()
        print(b[1])
        
    elif t == 4:
        print(sum(a))
        
    elif t == 5:
        print(sum([x for x in a if x % 2 == 0]))
        
    elif t == 6:
        s = ''
        for x in a:
            s += chr(ord('a') + x % 26)
        print(s)
        
    elif t == 7:
        i = 0
        while 0 <= i < n:
            if i == n - 1:
                print('Done')
                break
            i = a[i]
        else:
            print('Out')
        if i == n - 1:
            print('Done')
        else:
            print('Cyclic')
            

