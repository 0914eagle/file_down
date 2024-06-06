
'''
Consider the middle element of the circle. There will be an odd number of elements on each side of it (not necessarily all of the same value).

When the middle element is chosen, it will be deleted. The element to its right will be deleted when its right neighbor is chosen,
and so on. After the last element on each side is deleted, the remaining element is the circular value.

Now, if we take any neighbor of the middle element, and consider the number of elements on its right and left sides,
it will have at least one element on each side. This means we can choose that element instead of the middle element to obtain a larger circular value.

Thus, the maximum circular value is the value of the middle element.

'''
n=int(input())
a=list(map(int,input().split()))
print(max(a))
