
def chicken_problem(N, M):
    if M % N == 0:
        return "Dr. Chaz will have {} piece[s] of chicken left over!".format(M - N)
    else:
        return "Dr. Chaz needs {} more piece[s] of chicken!".format(N - M)

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(chicken_problem(N, M))

