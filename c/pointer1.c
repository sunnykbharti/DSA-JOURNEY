#include<stdio.h>
// void main() {
//     int arr[] = {0, 10, 20, 30, 40, 50};
//     int *p = arr;
//     printf("%d ", *p++);
//     printf("%d ", *++p);
// }

void main() {
    int a = 5, b = 10;
    int *p1 = &a, *p2 = &b;
    *p1 = *p1 + *p2;
    *p2 = *p1 - *p2;
    *p1 = *p1 - *p2;
    printf("a=%d b=%d", a, b);
    printf("%d",p1);
}