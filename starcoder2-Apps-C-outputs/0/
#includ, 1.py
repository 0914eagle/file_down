
#include <stdio.h>
int main()
{
    int n,i,j,k,a[1000],b[1000],c[1000],d[1000];
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&k);
        for(j=0;j<k;j++)
        {
            scanf("%d%d",&a[j],&b[j]);
        }
        c[0]=a[0];
        d[0]=b[0];
        for(j=1;j<k;j++)
        {
            for(int m=0;m<j;m++)
            {
                if(b[j]==d[m])
                {
                    c[m]+=a[j];
                    break;
                }
                else if(m==j-1)
                {
                    c[j]=a[j];
                    d[j]=b[j];
                }
            }
        }
        for(j=0;j<k;j++)
        {
            if(d[j]!=0)
            {
                printf("%d ",c[j]);
            }
        }
        printf("\n");
    }
    return 0;
}
