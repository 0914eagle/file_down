
#include<bits/stdc++.h>
using namespace std;
#define int long long
const int N=110;
int w[N],n;
int x[N];
bool check()
{
    int ret=0;
    for(int i=1;i<=n;i++)ret+=x[i]*w[i];
    if(ret!=w[0])return 0;
    return 1;
}
int cnt=1;
signed main()
{
    scanf("%lld",&n);
    for(int i=0;i<(1<<n);i++)scanf("%lld",&w[i]);
    for(int i=1;i<=n;i++)w[0]+=w[cnt++];
    int flag=0;
    for(int i=1;i<=n;i++)
    {
        for(int j=0;j<(1<<n);j++)
        {
            x[i]=1;
            if(check())
            {
                flag=1;
                break;
            }
            x[i]=-1;
            if(check())
            {
                flag=1;
                break;
            }
            x[i]=0;
        }
        if(flag)break;
    }
    if(!flag)puts("impossible");
    else
    {
        for(int i=1;i<=n;i++)printf("%lld\n",x[i]);
    }
    return 0;
}
