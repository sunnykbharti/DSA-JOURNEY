def DishPrepareOrder(nums):
    order={}
    for i in nums:
        if i not in order:
            order[i]=1
        else:
            order[i]+=1
    
    print(order)

nums=[1004,1003,1004,1003,1004,1005,1003,1004,1003,1002,1005,1002,1002,1001,1002,1002,1002]
DishPrepareOrder(nums)