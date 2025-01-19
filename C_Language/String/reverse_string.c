#include<stdio.h>
#include<string.h>
int main(){
    char arr[100];
    puts("input the name");
    gets(arr);
    int size=0,i;
    while(arr[i]!='\0'){
        size++;
        i++;
    }
    for(int i=0,j=size-1;i<=j;i++,j--){
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }
    puts("the revrse name is");
    puts(arr);

}