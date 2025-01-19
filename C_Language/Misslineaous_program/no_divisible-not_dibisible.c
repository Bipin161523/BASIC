#include<stdio.h>
int main(){
    int N,n,sum1=0,sum2=0;
    printf("enter a number:");
    scanf("%d",&N);
    printf("enter divi no:");
    scanf("%d",&n);
    for(int i=1;i<=N;i++){
        if(i%n==0)
        sum1+=i;
        else
        if(i%n!=0)
        sum2+=i;
    }
    printf("%d",sum2-sum1);
}