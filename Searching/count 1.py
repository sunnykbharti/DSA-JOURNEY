def count(arr):
    low=0
    high=len(arr)-1
    while low<high:
        mid=(low+high)//2
        if mid==0:
            high=mid-1
        elif mid==len(arr)-1 or arr[mid+1]==1:
            return mid+1
        else:
            low=mid+1
        # if arr[high-1]==1:
        #     return high
        #     break
    return 0
arr=input()
print(count(arr))