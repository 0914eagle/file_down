
from math import factorial

def main():
n = int(input())
approximation = 0
for i in range(n + 1):
approximation += 1 / factorial(i)
print(approximation)

if __name__ == '__main__':
main()

