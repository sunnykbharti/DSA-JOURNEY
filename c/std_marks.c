#include<stdio.h>
void main()
{
    int stud[20];
    int i,perc;
    for(i=0;i<5;++i)
    {
        printf("Enter marks of Subject %d : ",i+1);
        scanf("%d",&stud[i]);
    }
    int sum;
    for(i=0;i<5;++i)
    {
        sum+=stud[i];
    }
    //printf("sum %d",sum);
    perc=sum/5;
    printf("Your percentage is %d \n",perc);
    if (perc>90 && perc<=100)
    {
        printf("Your Grade is A");
    }
    else if (perc>80 && perc<=90)
    {
        printf("Your Grade is B");
    }
    else if (perc>60 && perc<=80)
    {
        printf("Your Grade is C");
    }
    else
    {
        printf("Your Grade is F");
    }
}