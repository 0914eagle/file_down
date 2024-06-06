
# -*- coding: utf-8 -*-


n,m,k=map(int,raw_input().split())

if n==1:
    print k*m
    for i in range(k):
        for j in range(1,m+1):
            print "(1,",j,")",
        print "\n"

if m==1:
    print k*n
    for i in range(k):
        for j in range(1,n+1):
            print "(1,",j,")",
        print "\n"

if n==2:
    print 4*k
    for i in range(k):
        print "(1,1) (2,1)\n(1,1) (2,2)"

if m==2:
    print 4*k
    for i in range(k):
        print "(1,1) (1,2)\n(2,1) (2,2)"

if n==3 and m==3:
    print 9*k
    for i in range(k):
        print "(1,1) (2,1) (3,1)\n(1,1) (1,2) (1,3)\n(1,1) (2,1) (3,1)"

if n==4 and m==4:
    print 16*k
    for i in range(k):
        print "(1,1) (2,1) (3,1) (4,1)\n(1,1) (1,2) (1,3) (1,4)\n(1,1) (2,1) (3,1) (4,1)\n(1,1) (1,2) (1,3) (1,4)"
