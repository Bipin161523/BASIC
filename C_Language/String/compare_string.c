#include<stdio.h>
 int stringcmp(char *p,char* q);
int main(){
    int c;
    char str1[20];
    puts("enter first string");
    gets(str1);
    char str2[20];
    puts("enter 2nd string");
    gets(str2);
    c = stringcmp(str1,str2);
    if(c==0)
        puts("string are same");
    else if(c>0)
       puts("string a is big");
    else
       puts("string b is big");
    
}
    int stringcmp(char *p,char* q){
        while(*p==*q){
            if(*p=='\0')
            return 0;
            p++;
            q++;
        }
        return
        (*p-*q);
    }



        
        
    
