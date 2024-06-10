

n,k=[int(x) for x in input().split()]
w=[int(x) for x in input().split()]

def find_ways(idx,current_weight,count):
    global min_count,ways,n
    if idx==n:
        if current_weight==0:
            min_count=min(min_count,count)
            ways+=1
    else:
        find_ways(idx+1,current_weight,count) #send the current person back
        find_ways(idx+1,current_weight+w[idx],count+1) #send the current person across

min_count=float('inf')
ways=0
find_ways(0,0,0)
if min_count==float('inf'):
    print(-1)
    print(0)
else:
    print(min_count)
    print(ways%1000000007)

