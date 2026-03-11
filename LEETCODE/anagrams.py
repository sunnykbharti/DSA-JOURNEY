def dic(s):
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
    return d
def anagram(a,b):
    if dic(a)==dic(b):
        return True
    else:
        return False
print(anagram("sunny","nnuys"))