
# python 3.6
def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = nums[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None

def split(a, n):
    i = 1
    while i <= n:
        if a[i] == '(':
            i += 1
        else:
            break
    a = a[i:]
    i = n
    while i >= 0:
        if a[i] == ')':
            i -= 1
        else:
            break
    a = a[:i+1]
    return a


def is_valid(a):
    if len(a) % 2 != 0:
        return False
    count = 0
    for i in a:
        if i == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return True


n = int(input())
ans = 0
a = []
for i in range(n):
    a.append(split(input(), n))

b = a.copy()
a.sort()

for i in range(n):
    index = binary_search(a, b[i])
    if index is not None:
        if a[index] == b[i]:
            count = 1
            while index < n-1 and a[index] == b[i]:
                index += 1
                count += 1
            index -= count
            while index >= 0 and a[index] == b[i]:
                index -= 1
                count += 1
            ans += count*(count-1)//2


print(ans)
