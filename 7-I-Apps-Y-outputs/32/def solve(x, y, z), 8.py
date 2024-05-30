
def solve(x, y, z):
    # Write your code here
    return (x-2*z)//y

if __name__ == '__main__':
    x, y, z = map(int, input().split())
    print(solve(x, y, z))

