
import math

def main():
    X, A, B = input().split()
    X, A, B = int(X), int(A), int(B)
    digits = input()
    #print(X, A, B)
    if X == 1:
        print(len(digits)*(B-A+1))
    else:
        digits_set = set(digits)
        length = len(digits)
        #print(digits_set)
        count = 0
        for i in range(A, B+1):
            if all(x in digits_set for x in str(i)):
                count += 1
        print(count)


main()
