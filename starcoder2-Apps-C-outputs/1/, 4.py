
# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-19 11:14:43
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-19 11:15:14
# @Email: 

r, c = map(int, raw_input().split())
start = []
target = []
for i in xrange(r):
    start.append(raw_input())
    target.append(raw_input())

def hammer(board, i, j):
    board[i] = board[i][:j] + 'O' + board[i][j+1:]
    for k in xrange(c):
        if board[k][j] == 'O':
            board[k] = board[k][:j] + 'X' + board[k][j+1:]
    for k in xrange(r):
        if board[i][k] == 'O':
            board[i] = board[i][:k] + 'X' + board[i][k+1:]
    return board

def check(start, target):
    if start == target:
        return True
    for i in xrange(r):
        for j in xrange(c):
            if start[i][j] == 'O':
                if check(hammer(start, i, j), target):
                    return True
    return False

print 1 if check(start, target) else 0
