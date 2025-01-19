#include<stdio.h>
#include<string.h>
struct college{
    int clgno;
    float nirf;
    char name[50];
    

}add;

    struct class{
        int classno;
        float number;
        char name[50];
        struct college add;
    };
int main(){
    struct class p1;
    p1.classno=100;
    p1.number = 1.1;
    strcpy(p1.name,"bipin");
    p1.add.clgno=100;
    strcpy(p1.add.name,"niet");
    p1.add.nirf=101;
   
    printf("%d\n%f\n%s\n%d\n%f\n%s\n",p1.classno,p1.number,p1.name,p1.add.clgno,p1.add.nirf,p1.add.name);
}