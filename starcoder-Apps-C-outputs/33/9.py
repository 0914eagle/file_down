
def main():
    a,b,l,r=map(int,input().split())
    if r-l+1<=a:
        return a
    ans=0
    if a+b>l+r:
        ans+=b+l+r-a-b
    else:
        ans+=b
    ans+=a-1
    return ans
if __name__=='__main__':
    print(main())
