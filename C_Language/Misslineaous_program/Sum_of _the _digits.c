#include<stdio.h>
int count(int n){
    int rev=0,r;
    while(n!=0){
        r=(n%10);
        rev=rev+r;
        n=(n/10);
    }
    return rev;
}
int main(){
    int n,digit;
    printf("enter a number:");
    scanf("%d",&n);
    printf("sum of the digits =%d",count(n));
}