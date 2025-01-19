#include<stdio.h>
#include<string.h>
struct address{
    int no;
    char name[50];
    float pin;
};
int main(){
    struct address s1;
    s1.no =90;
    strcpy(s1.name,"bipin");
    s1.pin=2.4;
    printf("%d\n%s\n%.2f\n",s1.no,s1.name,s1.pin);
}

