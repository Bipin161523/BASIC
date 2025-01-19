#include<stdio.h>
#include<stdlib.h>
void main(){
    int n,*p;
    printf("enter thr value of n\n");
    scanf("%d",&n);
    p = (int*)malloc(n*sizeof(int));
    if(p==NULL){
        printf("\n unable located");
    }
    else{
        printf("base address=%p",p);
    }
}