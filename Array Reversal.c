#include <stdio.h>
#include <stdlib.h>
void reversearry(int a[],int len){
    int i,j;
    int array[len];
    for(j=len-1,i=0;j>=0;j--,i++){
        array[i]=a[j];
    }
    for(i=0;i<len;i++){
        printf("%d ",array[i]);
    }
}

int main()
{
    int n,i;
    scanf("%d",&n);
    int *arr;
    arr=(int*)malloc(n*sizeof(int));
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    reversearry(arr,n);
    return 0;
}
