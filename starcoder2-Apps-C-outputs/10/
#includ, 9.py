
#include<bits/stdc++.h>
using namespace std;
const int maxn=205;
int n;
int d[maxn][maxn];
int dp[maxn][maxn];
int main(){
    cin>>n;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n-i;j++){
            cin>>d[i][i+j];
        }
    }
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n-i;j++){
            dp[i][i+j]=max(dp[i][i+j-1],dp[i+1][i+j])+d[i][i+j];
        }
    }
    cout<<dp[1][n]<<endl;
    return 0;
}
