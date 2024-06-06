
def sub_array(arr,k,m):
    n=len(arr)
    arr.sort()
    res=0
    for i in range(n-k+1):
        j=i+k-1
        res+=arr[j]-arr[j-m]
    return res
