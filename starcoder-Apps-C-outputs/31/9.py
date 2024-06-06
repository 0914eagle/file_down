
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
#define MAXN 1000+10
using namespace std;
struct item
{
    double p;
    int e;
};
item a[MAXN];
int cmp(item x,item y)
{
    return x.p>y.p;
}
int main()
{
    int n;
    double p;
    cin>>n>>p;
    for(int i=0;i<n;i++)
    {
        cin>>a[i].e>>a[i].p;
    }
    sort(a,a+n,cmp);
    double sum=1;
    int ans=0;
    for(int i=0;i<n;i++)
    {
        if(sum<p)
        {
            sum*=(1-a[i].p);
            ans+=a[i].e;
        }
        else break;
    }
    cout<<ans<<endl;
    return 0;
}
