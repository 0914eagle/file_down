
#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e4 + 5;
int n, v[maxn], f[maxn], ans;
vector<int> g[maxn];
void dfs(int u, int fa) {
    f[u] = v[u];
    for (int i = 0; i < g[u].size(); i++) {
        int v = g[u][i];
        if (v == fa) continue;
        dfs(v, u);
        f[u] = max(f[u], f[v] + 1);
    }
}
void dfs2(int u, int fa) {
    if (f[u] == 1) ans++;
    for (int i = 0; i < g[u].size(); i++) {
        int v = g[u][i];
        if (v == fa) continue;
        dfs2(v, u);
    }
}
int main() {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) scanf("%d", &v[i]);
    for (int i = 1; i < n; i++) {
        int u, v;
        scanf("%d%d", &u, &v);
        g[u].push_back(v);
        g[v].push_back(u);
    }
    dfs(1, 0);
    dfs2(1, 0);
    printf("%d\n", ans);
    return 0;
}
