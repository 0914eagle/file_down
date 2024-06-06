
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,m,i,j,e,u,v,c,ans=0;
    cin>>n>>m;
    vector<int>a(n+1),g[n+1];
    for(i=0;i<n;i++)
    cin>>a[i];
    while(m--)
    {
        cin>>u>>v;
        g[v].push_back(u);
    }
    for(i=n-1;i>=0;i--)
    {
        if(a[i]==1)
        {
            c=0;
            for(j=0;j<g[i].size();j++)
            {
                if(a[g[i][j]]==1)
                c++;
            }
            if(c==g[i].size())
            ans++;
        }
    }
    cout<<ans<<endl;
    return 0;
}
