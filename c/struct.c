#include<stdio.h>
struct stud
{
    int roll;
    char name[20];
    int marks;
};
void main()
{
    struct stud s[5];
    for(int i=0;i<5;i++)
    {
        printf("Enter roll, name, marks");
        scanf("%d %s %d",&s[i].roll,s[i].name,&s[i].marks);
    }
    printf("details : roll=%d,name=%s,marks=%d",s[0].roll,s[0].name,s[0].marks);
}
