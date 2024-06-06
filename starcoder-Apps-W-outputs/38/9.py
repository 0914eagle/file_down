

#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
string a,b;
int la,lb;
int main()
{
    cin>>a>>b;
    la=a.size();lb=b.size();
    if(la==lb)
    {
        int cnt=0;
        for(int i=0;i<la;i++)
        {
            if(a[i]!=b[i]) cnt++;
            if(cnt>2) break;
        }
        if(cnt==0||cnt==2) printf("YES");
        else printf("NO");
    }
    else printf("NO");
}
