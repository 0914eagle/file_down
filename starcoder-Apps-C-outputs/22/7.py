
#include<bits/stdc++.h>
using namespace std;
#define ll long long

ll n,m,h,cnt,a[100005],b[100005],c[100005],d[100005],vis[100005];
vector<ll>g[100005];
void dfs(ll u)
{
    if(vis[u])
        return;
    vis[u]=1;
    d[u]=c[u]=1;
    for(int i=0;i<g[u].size();i++)
    {
        ll v=g[u][i];
        dfs(v);
        c[u]+=c[v];
        d[u]+=d[v];
    }
}

int main()
{
    scanf("%lld %lld %lld",&n,&m,&h);
    for(int i=1;i<=n;i++)
        scanf("%lld",&a[i]);
    for(int i=1;i<=m;i++)
    {
        ll x,y;
        scanf("%lld %lld",&x,&y);
        g[x].push_back(y);
        g[y].push_back(x);
    }
    dfs(1);
    for(int i=1;i<=n;i++)
    {
        b[i]=c[i]+n-d[i];
        cnt+=b[i];
    }
    ll ans=1e9,idx;
    for(int i=1;i<=n;i++)
    {
        if(cnt-b[i]<ans)
        {
            ans=cnt-b[i];
            idx=i;
        }
    }
    printf("%lld\n%lld\n",ans,idx);
}
