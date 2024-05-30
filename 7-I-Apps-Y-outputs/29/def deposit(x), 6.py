
def deposit(x):
    if x <= 100:
        return 0
    else:
        return 1 + deposit(x * 1.01)

def main():
    x = int(input())
    print(deposit(x))

