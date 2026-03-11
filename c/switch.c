#include<stdio.h>
void main()
{
    int a,b;
    char o;
    printf("Enter the expression  : ");
    scanf("%ld %c %ld",&a,&o,&b);

    switch(o)
    {
        case '+':
        printf("Sum is %d",a+b);
        break;

        case '-':
        printf("difference is %d",a-b);
        break;
    }
}