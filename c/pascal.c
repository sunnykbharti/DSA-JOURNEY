#include <stdio.h>

void main() {
    int rows = 5, coef = 1, space, i, j;

    // Outer loop for rows
    for (i = 0; i < rows; i++) {
        
        // Loop for spaces to print the pyramid shape
        for (space = 1; space <= rows - i; space++)
            printf(" ");

        // Loop to print values in each row
        for (j = 0; j <= i; j++) {
            if (j == 0 || i == 0)
                coef = 1;
            else
                // Formula to calculate value based on previous value
                coef = coef * (i - j + 1) / j;
            
            printf("%d ", coef);
        }
        printf("\n");
    }
}