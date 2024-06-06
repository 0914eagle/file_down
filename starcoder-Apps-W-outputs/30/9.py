
#include<bits/stdc++.h>
using namespace std;
int main()
{
	char s[101];
	scanf("%s",s);
	int n=strlen(s);
	int i,flag=0;
	for(i=0;i<n;i++)
	{
		if(s[i]!='a'&&s[i]!='e'&&s[i]!='i'&&s[i]!='o'&&s[i]!='u'&&s[i]!='n')
		{
			if(s[i+1]!='a'&&s[i+1]!='e'&&s[i+1]!='i'&&s[i+1]!='o'&&s[i+1]!='u')
			{
				flag=1;
				break;
			}
		}
	}
	if(flag==1)
		printf("NO");
	else
		printf("YES");
	return 0;
}
