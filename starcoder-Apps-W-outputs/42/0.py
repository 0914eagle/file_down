
#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define P pair<int,int>
const int N = 2e3 + 10;
P p[N];
int vis[N], op[N];
int main(){
	int n, x, y, z;
	cin >> n;
	for(int i = 1; i <= n; i++){
		scanf("%d %d %d", &x, &y, &z);
		p[i] = P(y, z);
	}
	int cnt = 0;
	while(1){
		memset(vis, 0, sizeof(vis));
		int flag = 1;
		for(int i = 1; i <= n; i++){
			if(vis[i]) continue;
			for(int j = i + 1; j <= n; j++){
				if(vis[j]) continue;
				int minx = min(p[i].first, p[j].first);
				int maxx = max(p[i].first, p[j].first);
				int miny = min(p[i].second, p[j].second);
				int maxy = max(p[i].second, p[j].second);
				int ok = 0;
				for(int k = 1; k <= n; k++){
					if(vis[k]) continue;
					if(minx <= p[k].first && p[k].first <= maxx && miny <= p[k].second && p[k].second <= maxy)
						ok = 1;
				}
				if(!ok){
					vis[i] = vis[j] = 1;
					op[++cnt] = i;
					op[++cnt] = j;
					flag = 0;
					break;
				}
			}
			if(!flag) break;
		}
		if(flag) break;
	}
	for(int i = 1; i <= n; i++){
		printf("%d%c", op[i], " \n"[i == n]);
	}
	return 0;
}
