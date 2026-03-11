def invert(fnf,L):
    count=0
    i=0
    for j in range(len(L)):
        if fnf.index(L[i]) < fnf.index(L[j]):
            L[i],L[j]=L[j],L[i]
            count+=1
        i+=1
    return count
a=invert([4,2,5,1,3],[1,2,5,4,3])
print(a)