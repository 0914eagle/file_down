
def maxbeauty(arr, m, k):
    n = len(arr)
    beauty = []
    arr.sort()
    for i in range(n-m+1):
        beauty.append(sum(arr[i:i+m]))
    beauty.sort()
    return beauty[-k]

if __name__ == "__main__":
    n,m,k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(maxbeauty(arr, m, k))
