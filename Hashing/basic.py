import random as r
a=[]
for _ in range(10):
    b=r.randint(1,1000)
    if b not in a and len(str(b))==3:
        a.append(b)
    else:
        a.append(999)
hash=[None]*10
print(a)
for i in a:
    hf=i%10
    print(hf)
    if hash[hf]==None:
        hash[hf]=i
    else:
        if type(hash[hf]) is not list:
            hash[hf]=[hash[hf],i]
        else:
            hash[hf].append(i)
print(hash)