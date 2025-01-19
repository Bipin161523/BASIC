#include<stdio.h>
int fact(int a){
    if(a==0)
    return 1;
    else
    return (a*fact(a-1));
    
}
int main(){
    int x,facto;
    printf("enter number:");
    scanf("%d",&x);
    facto=fact(x);
    printf("factorial of the number is : %d",facto);
}