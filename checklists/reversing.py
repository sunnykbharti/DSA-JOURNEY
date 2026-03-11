def reverse(l):
    if len(l)<=1:
        return l
    else:
        return l[-1]+reverse(l[:len(l)-1])
t=[1,2,3,4,5]
print(reverse(t))