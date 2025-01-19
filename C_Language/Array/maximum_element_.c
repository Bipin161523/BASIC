#include<stdio.h>
int main(){
    int size;
    printf("enter size of the array:");
    scanf("%d",&size);
    int arr[size];
    printf("enter array elements:");
    for(int i=0;i<size;i++){
        scanf("%d",&arr[i]);
    }
    int max=arr[0];
    for(int i=0;i<size;i++){
        if(max<arr[i])
        max=arr[i];
    }
    printf("maximum element is %d ",max);
}
