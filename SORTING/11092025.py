class Student:
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
name=input("Enter name:")
m1=int(input("Enter marks1:")) 
m2=int(input("Enter marks2:"))
m3=int(input("Enter marks3:"))
s1=Student(name,m1,m2,m3)  
print("Average marks:",s1.avg())