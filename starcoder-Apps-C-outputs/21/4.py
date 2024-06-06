
#https://github.com/nayefahmad/Coursera-Python-Programming/blob/master/week%203%20files/week%203%20problem%20set/Trans%20and%20Number%20Sequence.ipynb

a, b, c, d = map(int, input().split())

if (a > 0 and b == 0 and c == 0 and d == 0) or (a == 0 and b > 0 and c == 0 and d == 0) or (a == 0 and b == 0 and c > 0 and d == 0) or (a == 0 and b == 0 and c == 0 and d > 0):
    print("NO")
else:
    print("YES")
    print(0, end = " ")
    a -= 1
    
    while a > 0:
        print(1, end = " ")
        a -= 1
    
    while b > 0:
        print(0, end = " ")
        b -= 1
    
    while c > 0:
        print(2, end = " ")
        c -= 1
    
    while d > 0:
        print(3, end = " ")
        d -= 1
