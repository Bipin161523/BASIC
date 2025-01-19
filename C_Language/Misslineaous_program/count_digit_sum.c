#include<stdio.h>
int main(){
    int N;
    printf("enter a number:");
    scanf("%d",&N);
    
     while(N>10){
      int sum=0;
      while(N>0){
        sum+=N%10;
        N=N/10;
      }
      N=sum;
    }
    printf("%d",N);
    

}
