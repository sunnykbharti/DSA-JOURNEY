def partition(arr,start,end):
    index=-1
    for j in range(start,end):
        if arr[j]<=arr[end]:
            index+=1
            arr[j],arr[index]=arr[index],arr[j]
    index=index+1
    arr[end],arr[index]=arr[index],arr[end]
    return index

def quicksort(arr,start,end):
    if start<end:
        pivindex=partition(arr,start,end)
        quicksort(arr,start,pivindex-1)
        quicksort(arr,pivindex+1,end)
    print(arr)
quicksort([6,2,3,4,1,5],0,5)