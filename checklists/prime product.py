def prime(num):
    p=True
    l=0
    if num==2:
        p=True
    else: 
        for i in range(2,int(pow(num,1/2))):
            if num%i==0:
                l+=1
    if l>=1:
        p=False
    return p
def prime_product(n):
    if n<0:
        return False
    for i in range(2,n//2+1):
        print(prime(i),i)
        for j in range(2,n//2+1):
            print(prime(j),j)
            if prime(i)==prime(j)==True and i*j==n:
                print(prime(i),prime(j))
                return True
                break
    return False
print(prime_product(12))