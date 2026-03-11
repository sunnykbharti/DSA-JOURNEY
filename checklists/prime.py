def prime(n):
    p=True
    l=0
    if n==2:
        p=True
    else: 
        for i in range(2,int(pow(n,1/2))+1):
            if n%i==0:
                l+=1
    if l>=1:
        p=False
    print(p)
    n=int(input("Enter a number : "))
    prime(n)
#n=int(input("Enter a number : "))
prime(6)