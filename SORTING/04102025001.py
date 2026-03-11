def mergeInPlace(A,B):
    l1=len(A)
    l2=len(B)
    for i in range(l1):
        min=A[i]
        for j in range(l2):
            if min>B[j]:
                swap(A[i],B[j])
                #A[i],B[j]=B[j],A[i]
                min=A[i]        
    B.sort()
    print(A,B)
print(mergeInPlace([2,4,6,9,13,15],[1,3,5,10]))