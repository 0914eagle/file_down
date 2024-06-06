
#include <bits/stdc++.h>
using namespace std;

int N;
long long ans = 1e18;
int a[405];
vector<int> G[405];
bool vis[405];

void dfs(int x)
{
	if (vis[x]) return ;
	vis[x] = 1;
	for (int i = 0; i < G[x].size(); i++)
	{
		dfs(G[x][i]);
		a[x] += a[G[x][i]];
	}
}

void dfs1(int x, long long tmp)
{
	if (vis[x]) return ;
	vis[x] = 1;
	if (x == N)
	{
		ans = min(ans, tmp);
		return ;
	}
	for (int i = 0; i < G[x].size(); i++)
	{
		dfs1(G[x][i], max(tmp, a[x]));
	}
}

int main()
{
	scanf("%d", &N);
	for (int i = 1; i <= N; i++)
		scanf("%d", &a[i]);
	for (int i = 1; i <= N; i++)
	{
		int n, k;
		scanf("%d", &n);
		for (int j = 0; j < n; j++)
		{
			scanf("%d", &k);
			G[i].push_back(k);
		}
	}
	dfs(1);
	memset(vis, 0, sizeof(vis));
	dfs1(1, 0);
	printf("%lld\n", ans);
	return 0;
}
