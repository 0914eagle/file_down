
#include<stdio.h>
int main()
{
    int n,i,j,k,a[1000],b[1000],c[1000],d[1000],e[1000];
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
        e[0]=1;
        for(j=1;j<k;j++)
        {
            if(b[j]==d[e[0]-1])
            {
                c[e[0]-1]+=a[j];
            }
            else
            {
                e[0]++;
                c[e[0]-1]=a[j];
                d[e[0]-1]=b[j];
            }
        }
        for(j=0;j<e[0];j++)
        {
            printf("%d ",c[j]);
        }
        printf("\n");
    }
    return 0;
}
