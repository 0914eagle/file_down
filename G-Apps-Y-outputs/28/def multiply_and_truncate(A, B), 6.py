
def multiply_and_truncate(A, B):
    result = int(A * B)
    print(result)

if __name__ == "__main__":
    A, B = map(float, input().split())
    multiply_and_truncate(A, B)
