
def fruit_distribution(s,n):
    fruits = s.split()
    apples = int(fruits[0]) if fruits[0].isdigit() else 0
    oranges = int(fruits[-1]) if fruits[-1].isdigit() else 0
    mango = n - apples - oranges
    return mango
