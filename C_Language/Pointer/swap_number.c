#include<stdio.h>
int swap(int *x, int *y){
    int temp=*x;
    *x=*y;
    *y=temp;
    printf("value of first and second number is %d and %d:",*x,*y);
}
int main(){
    int x,y;
    printf("enter first and second number:");
    scanf("%d%d",&x,&y);
    swap(&x,&y);
}
