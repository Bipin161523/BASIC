#include<stdio.h>
struct test
{
    int a;
    float b;
    char c[100];

} ;

int main(){
    struct test s;
    printf("enter name:");
    gets(s.c);
    printf("enter roll number:");
    scanf("%d",&s.a);
    printf("enter marks:");
    scanf("%f",&s.b);
    printf("%s\n",s.c);
    printf("%d\n",s.a);
    printf("%f\n",s.b);

}

