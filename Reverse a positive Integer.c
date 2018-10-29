#include <stdio.h>
#include <stdlib.h>
#include<math.h>

int main()
{
    int n,r,i,flag=0;
    scanf("%d",&n);
    int a[10];
    while(n>0){
        r=n%10;
        a[flag]=r;
        flag++;
        n=n/10;
    }
    for(i=0;i<flag;i++){
            if(a[i]==0)continue;
        printf("%d",a[i]);
    }
    return 0;
}
