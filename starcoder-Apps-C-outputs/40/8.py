
#include<iostream>
#include<cstring>
using namespace std;
int n, num, dp[200001], a[200001];
int main()
{
    cin >> n;
    memset(dp, 0, sizeof(dp));
    for (int i = 1; i <= n; i++)
        cin >> a[i];
    for (int i = 1; i <= n; i++)
    {
        num = 1;
        for (int j = 1; j <= i - 1; j++)
            if (a[i] < a[j])
                num = max(num, dp[j] + 1);
        dp[i] = num;
    }
    int ans = 0;
    for (int i = 1; i <= n; i++)
        ans = max(ans, dp[i]);
    cout << ans << endl;
    return 0;
}
