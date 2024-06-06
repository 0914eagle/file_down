
# Read number of people
n = int(input())

# List of numbers for each person
nums = []

# Read numbers for each person
for i in range(n):
    m = int(input())
    nums.append([int(x) for x in input().split()])

# Check if each number is repeated
# If it is repeated, we know that two people are connected
def check_repeated(nums):
    for i in range(n):
        if len(nums[i]) != len(set(nums[i])):
            return True
    return False

# Check if each number is connected to all other numbers
# This shows that each person is connected to everyone else
def check_all(nums):
    for i in range(n):
        for j in range(n):
            if i != j and not set(nums[i]).intersection(set(nums[j])):
                return False
    return True

# Check if the numbers of each person are unique
# If the numbers are unique, then each person is unique
def check_unique(nums):
    num_set = set()
    for i in range(n):
        if not set(nums[i]).isdisjoint(num_set):
            return False
        num_set = num_set.union(set(nums[i]))
    return True

# Check if each person has a number that is shared with at least one other person
# If this is true, then we know that each person is connected to at least one other person
def check_connected(nums):
    for i in range(n):
        found = False
        for j in range(n):
            if i != j and set(nums[i]).intersection(set(nums[j])):
                found = True
                break
        if not found:
            return False
    return True

if not check_repeated(nums) or not check_all(nums) or not check_unique(nums) or not check_connected(nums):
    print("impossible")
else:
    print("possible")
