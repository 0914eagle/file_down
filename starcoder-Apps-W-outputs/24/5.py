
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <cmath>
#include <sstream>
#define pii pair<int,int>
#define fi first
#define se second
using namespace std;
typedef long long LL;

inline int read(){
	int x=0,f=1;char ch=getchar();
	while(!isdigit(ch)){if(ch=='-')f=-1;ch=getchar();}
	while(isdigit(ch)){x=x*10+ch-'0';ch=getchar();}
	return x*f;
}
const int maxn = 200005;
int n,a[20],b[maxn],vis[maxn];
LL s;

int main(){
	n = read();
	for(int i=1;i<=1<<n;i++)b[i]=read();
	sort(b+1,b+1<<n+1);
	s = 0;
	for(int i=1;i<=n;i++)a[i]=1,s+=1;
	int tmp = 0,now = 0;
	for(int i=1;i<=1<<n;i++){
		vis[i] = s;
		tmp = s;
		s -= now;
		now = tmp;
	}
	for(int i=1;i<=n;i++)if(b[i]!=a[i])return puts("impossible"),0;
	for(int i=1;i<=1<<n;i++){
		if(vis[i]!=b[i]){
			puts("impossible");
			return 0;
		}
	}
	for(int i=1;i<=n;i++)cout<<a[i]<<endl;
}
