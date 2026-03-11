sublist=[]
def subs(word):
    sub=""
    for i in word:
        if i not in sub:
            sub+=i
        else :
            new=a.replace(sub,'')
            subs(new)
    if sub not in sublist: 
        sublist.append(sub)
    return sublist
    
a=input("String : ")
subs(a)
for i in sublist:
    print(f'longest substring without repition is/are of length {len(i)} and the substring is {i}')
