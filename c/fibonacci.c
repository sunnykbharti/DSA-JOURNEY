#include<stdio.h>
void main()
{
    int a,b,c,n;
    a=0;
    b=1;
    printf("Enter n ");
    scanf("%d",&n);
    printf("%d \n",a);
    printf("%d \n",b);
    for(int i=2;i<=n;i++)
    {
        c=a+b;
        a=b;
        b=c;
        printf("%d \n",c);
    }
}
