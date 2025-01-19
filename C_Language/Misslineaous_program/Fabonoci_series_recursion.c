#include <stdio.h>

// Function to calculate the nth Fibonacci number using recursion
int fibonacci(int n) {
    if (n == 0) {
        return 0; // Base case: 0th Fibonacci number
    } else if (n == 1) {
        return 1; // Base case: 1st Fibonacci number
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2); // Recursive call
    }
}

int main() {
    int n;

    printf("Enter the number of terms: ");
    scanf("%d", &n);

    printf("Fibonacci Series: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", fibonacci(i)); // Call the recursive function
    }
    printf("\n");

    return 0;
}
