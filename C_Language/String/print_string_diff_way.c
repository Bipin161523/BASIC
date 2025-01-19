#include<stdio.h>
int main(){
    char str[]="hello world is best";
    
     printf("%c",str[3]);
       printf("%c",str[5]);
      printf("%d",str[4]);//asccii valu
    str[3]='b';
    str[6]=98;
     printf("%c",str[3]);
       printf("%c",str[6]);

}