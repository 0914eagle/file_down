
# cook your dish here
n=int(input())
s=input()
i=s.find('P')
j=s.rfind('P')
c=s.count('*')
if c==0:
    print(0)
elif c==n:
    print(n-1)
elif i==j:
    print(1)
else:
    if c%2==1:
        print(c//2+2)
    else:
        print(c//2+1)---
title: '602A - Approximating a Constant Range'
date: 2020-02-03T09:37:00.000Z
submitTime: 2020-02-03T09:37:00.000Z
tags:
  - math
  - dp
  - *2200
categories:
  - AtCoder
isShow: true
description: 给定一个数组，找出一个最大的区间，使得区间内的数，取最大值和最小值之差小于等于 1。
---

# Approximating a Constant Range

## 题目描述

You are given a sequence $a$ of length $n$. Find the longest subsequence of consecutive elements of this sequence that has the difference of maximum and minimum elements not greater than $1$.

## 输入输出格式

### 输入格式：

The first line contains a single integer $n$ ($1 \le n \le 200\,000$) — the length of the sequence $a$.

The second line contains $n$ integers $a_1, a_2, \ldots, a_n$ ($1 \le a_i \le 10^9$) — elements of the sequence $a$.

### 输出格式：

Print a single integer — the length of the longest subsequence of consecutive elements with the difference of maximum and minimum elements not greater than $1$.

## 输入输出样例

### 输入样例 #1：

