

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int a1,b1,a2,b2;
    scanf("%d %d %d %d",&a1,&b1,&a2,&b2);
    if(b1-a1>b2-a2)
    {
        printf("Gunnar\n");
    }
    else if(b1-a1<b2-a2)
    {
        printf("Emma\n");
    }
    else
    {
        printf("Tie\n");
    }
    return 0;
}


