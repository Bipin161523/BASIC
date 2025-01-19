#include<stdio.h>
int swap(int x, int y){
    x = x+y;
    y=x-y;
    x=x-y;
    printf("value of first and second number is %d and %d:",x,y);
}
int main(){
    int x,y;
    printf("enter first and second number:");
    scanf("%d%d",&x,&y);
    swap(x,y);

}