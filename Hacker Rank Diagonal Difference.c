#include <stdio.h>
#include<stdlib.h>
int main()
{
    int n;
    scanf("%d",&n);
    int i,j,k,a[n][n],sum1=0,sum2=0;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            scanf("%d",&a[i][j]);
        }
    }
    
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(i==j){
                sum1+=a[i][j];
                break;
            }
        }
    }
    j=n-1;
    for(i=0;i<n;i++){
            sum2+=a[i][j];
            j--;
        }
    printf("%d",abs(sum1-sum2));

    return 0;
}
