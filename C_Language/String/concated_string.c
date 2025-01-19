#include<stdio.h>
#include<string.h>
void concate(char a[],char b[]){
    int c=0;
    while(a[c]!='\0'){
        c++;
    }
    
    int j=0;
    while(b[j]!='\0'){
        a[c]=b[j];
        c++;
        j++;
    }
    a[c]='\0';

    printf("concated string is %s",a);
}
int main(){
    char a[100],b[50];
    printf("enter first string:");
    scanf("%s",&a);
    printf("enter second string:");
    scanf("%s",&b);
    concate(a,b);
}