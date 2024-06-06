
#include<bits/stdc++.h>
using namespace std;
int n,d[205][205],dp[205][205],ans=0x3f3f3f3f;
int main()
{
    cin>>n;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            cin>>d[i][j];
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            dp[i][j]=0x3f3f3f3f;
            for(int k=1;k<=n;k++)
                dp[i][j]=min(dp[i][j],max(dp[i-1][k],d[i][k]));
        }
    }
    for(int i=1;i<=n;i++)
        ans=min(ans,dp[n][i]);
    cout<<ans<<endl;
    return 0;
}
