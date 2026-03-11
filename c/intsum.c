#include<stdio.h>
void main()
{
    int a,sum=0;
    printf("Enter a number : ");
    scanf("%d",&a);
    while(a>0)
    {
        sum+=a%10;
        a=a/10;
    }
    printf("sum=%d",sum);
}