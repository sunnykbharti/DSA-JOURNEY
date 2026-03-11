#include<stdio.h>
void main()
{
    int b=10;
    int* p;
    p=&b;
    printf("Address of b = %ld \n",p);
    printf("Value of b = %d \n",*p);
    printf("Address of p = %u",&p);
}