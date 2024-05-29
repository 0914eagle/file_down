
def find_minimum_amount(N, K, disliked_digits):
    while not all(digit in disliked_digits for digit in str(N)):
        N += 1
    return N

if __name__ == "__main__":
    N, K = map(int, input().split())
    disliked_digits = set(map(int, input().split()))

    result = find_minimum_amount(N, K, disliked_digits)
    print(result)
