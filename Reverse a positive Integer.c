#include <stdio.h>
#include <stdlib.h>
#include<math.h>

int main()
{
    int n,r,i,rev=0;
    scanf("%d",&n);
    while(n>0){
        r=n%10;
        rev=r*10+rev;
        n=n/10;
    }
    printf("%d",rev);
    return 0;
}
