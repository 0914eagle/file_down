
import sys
import bisect

def solve(s, c, k, d):
    d.sort() #sort the color values

    machines = 0 #number of machines
    wash = [] #the color values of socks in a machine
    
    for color in d: #for each sock
        if not wash: #if there is no sock in the machine
            wash.append(color) #add the sock to the machine
            machines += 1 #start a new machine
        elif abs(color - wash[0]) <= k: #if the sock can be added to the machine
            wash.append(color) #add the sock to the machine
        else: #if the sock can't be added to the machine
            wash = [] #start a new machine
            wash.append(color) #add the sock to the machine
            machines += 1 #start a new machine
            
        if len(wash) == c: #if the machine is full
            wash = [] #start a new machine
            machines += 1 #start a new machine
            
    return machines
    
if __name__ == "__main__":
    s, c, k = map(int, input().split())
    d = list(map(int, input().split()))
    
    answer = solve(s, c, k, d)
    
    print(answer)
    

