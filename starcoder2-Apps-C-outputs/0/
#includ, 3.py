
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n,x,y;
    cin>>n;
    vector<int> v[n];
    for(int i=0;i<n;i++)
    {
        int k;
        cin>>k;
        for(int j=0;j<k;j++)
        {
            cin>>x>>y;
            v[i].push_back(y);
        }
    }
    for(int i=0;i<n;i++)
    {
        sort(v[i].begin(),v[i].end());
    }
    int max=v[0][0];
    for(int i=0;i<n;i++)
    {
        if(v[i][0]>max)
        {
            max=v[i][0];
        }
    }
    int a[max+1]={0};
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<v[i].size();j++)
        {
            a[v[i][j]]++;
        }
    }
    int sum=0;
    for(int i=1;i<=max;i++)
    {
        sum+=a[i];
        if(a[i]>0)
        {
            cout<<sum<<" ";
        }
    }
    return 0;
}
