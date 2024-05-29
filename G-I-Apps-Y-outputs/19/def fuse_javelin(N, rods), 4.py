
def fuse_javelin(N, rods):
    total_length = sum(rods)
    return total_length - (N - 1)

# Input
N = int(input())
rods = [int(input()) for _ in range(N)]

# Output
print(fuse_javelin(N, rods))
