
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import os
from heapq import *

def rebel():
    [s,b] = [int(x) for x in sys.stdin.readline().split()]
    attack = [int(x) for x in sys.stdin.readline().split()]
    #print "attack=",attack
    defense = []
    gold = []
    maxgold = 0
    for i in range(b):
        [d,g] = [int(x) for x in sys.stdin.readline().split()]
        defense.append(d)
        gold.append(g)
        maxgold = max(maxgold, g)
    #print "defense=",defense
    #print "gold=",gold
    #print "maxgold=",maxgold
    ans = []
    for i in attack:
        #print "maxgold=",maxgold
        ans.append(maxgold)
        for j in range(b):
            if i >= defense[j]:
                maxgold = max(maxgold, gold[j])
                #print "maxgold=",maxgold
    for i in ans:
        print i,
rebel()
