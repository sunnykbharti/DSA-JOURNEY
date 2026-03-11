def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print("sorted array is : ",arr)
bubble([6,5,1,3,4,0,-1,-5])