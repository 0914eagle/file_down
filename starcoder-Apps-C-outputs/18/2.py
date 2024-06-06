
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N=5e3+5;
const int M=25e3+5;
const int mod=1e9+7;
int n,m,k,a[N],b[N],s[N];
vector<int>v[M];
int main()
{
	int i,j;
	scanf("%d%d",&n,&m);
	for(i=1;i<=n;++i)
	{
		scanf("%d",&a[i]);
		b[i]=a[i];
	}
	sort(b+1,b+n+1);
	for(i=1;i<=n;++i)
		for(j=i;j<=n;++j)
			s[i]+=a[j];
	int ans=0;
	for(i=1;i<=n;++i)
	{
		for(j=1;j<=n;++j)
		{
			if(s[i]==b[j]&&s[i]<=m)
			{
				v[s[i]].push_back(a[i]);
				v[s[i]].push_back(b[j]);
			}
		}
	}
	for(i=0;i<=m;++i)
		if(v[i].size())
		{
			ans++;
			printf("%d\n",i);
		}
	return 0;
}
