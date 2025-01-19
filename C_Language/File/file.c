#include<stdio.h>

int main(){
    FILE *file = fopen("example.txt","w");
    if (file == NULL) {
        printf("File opned successfully\n");
        return 1;
    }
    
    fprintf(file, "amit gupta*\n");
    printf("data return to file successfully");
    fclose(file);
    return 0;
}