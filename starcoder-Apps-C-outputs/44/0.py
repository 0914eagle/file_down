
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const int maxn=5e5+5;
ll x0,y0,ax,ay,bx,by,xs,ys,t,xx[maxn],yy[maxn];
int main(){
	cin>>x0>>y0>>ax>>ay>>bx>>by>>xs>>ys>>t;
	xx[0]=x0;yy[0]=y0;
	int i;
	for(i=1;t>=abs(xx[i-1]-xs)+abs(yy[i-1]-ys);i++){
		xx[i]=ax*xx[i-1]+bx;
		yy[i]=ay*yy[i-1]+by;
		t-=abs(xx[i]-xx[i-1])+abs(yy[i]-yy[i-1]);
	}
	i--;
	ll ans=0;
	for(int j=0;j<=i;j++)
		if(abs(xx[i]-xx[j])+abs(yy[i]-yy[j])<=t)
			ans++;
	cout<<ans<<endl;
	return 0;
}
