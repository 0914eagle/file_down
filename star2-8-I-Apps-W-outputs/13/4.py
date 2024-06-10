
def print7():
    print(7)
    
def printBiggerOrSmaller(arr):
    if arr[0] > arr[1]:
        print("Bigger")
    elif arr[0] == arr[1]:
        print("Equal")
    else:
        print("Smaller")
        
def printMedian(arr):
    arr.sort()
    print(arr[1])
    
def printSum(arr):
    print(sum(arr))
    
def printEvenSum(arr):
    print(sum(x for x in arr if x % 2 == 0))
    
def printString(arr):
    s = ""
    for num in arr:
        s += chr(ord('a') + (num % 26))
    print(s)
    
def printJump(arr):
    N = len(arr)
    i = 0
    
    while i < N:
        if i < 0 or i >= N:
            print("Out")
            return
        if i == N-1:
            print("Done")
            return
        i = arr[i]
        
    print("Cyclic")

def main():
    N, t = map(int, input().split())
    arr = list(map(int, input().split()))
    
    if t == 1:
        print7()
    elif t == 2:
        printBiggerOrSmaller(arr)
    elif t == 3:
        printMedian(arr)
    elif t == 4:
        printSum(arr)
    elif t == 5:
        printEvenSum(arr)
    elif t == 6:
        printString(arr)
    elif t == 7:
        printJump(arr)
        
if __name__ == "__main__":
    main()

