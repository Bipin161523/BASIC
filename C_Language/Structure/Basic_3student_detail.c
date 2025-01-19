#include<stdio.h>
struct student{
    int rollno;
    float marks;
    char name[50];
};
     int main(){
        struct student p1[3];
        printf("enter three stdunts details\n:");
        for(int i=0;i<=2;i++){
            printf("enter %d student roll no:\n",i);
            scanf("%d",&p1[i].rollno);
            printf("enter %d students marks:\n",i);
             scanf("%f",&p1[i].marks);
            printf("enter %d students name:\n",i);
            scanf("%s",p1[i].name);
        }
        for(int i=0;i<=2;i++){
            printf("studen %d roll no is: %d\n", i,p1[i].rollno);
             printf("studen %d marks is: %f\n",i,p1[i].marks);
                printf("studen %d name: %s\n",i,p1[i].name);
        }

     }