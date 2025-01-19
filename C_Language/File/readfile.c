#include<stdio.h>


int main(){
    FILE *file = fopen("amit.txt","r");
    if (file == NULL) {
        printf("File opned successfully\n");
        return 1;
    }
    
    char line[100];
    while(fgets(line,sizeof(line),file)){
        printf("%s",line);
    }
    fclose(file);
    return 0;
}