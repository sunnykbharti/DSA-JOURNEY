n,m=10,3
a=sum([i for i in range(1,n+1) if i%m!=0])
b=sum([j for j in range(1,n+1) if j%m==0])
print(a-b)