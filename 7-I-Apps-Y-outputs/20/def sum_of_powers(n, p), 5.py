
def sum_of_powers(n, p):
    return sum([int(i) ** p for i in n])

def main():
    n = int(input())
    n_list = list(map(int, input().split()))
    p = 1
    while sum_of_powers(n_list, p) < 1000000000:
        p += 1
    print(sum_of_powers(n_list, p))

if __name__ == '__main__':
    main()

