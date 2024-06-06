
'''input
6 5
'''

p,x = map(int, input().split())

if p == 1:
    print("Impossible")
else:
    k = 10**(p-1)

    if (10**p - 1) % (x-1) == 0:
        print((10**p - 1) // (x - 1))
    else:
        print("Impossible")

'''output
142857
'''
