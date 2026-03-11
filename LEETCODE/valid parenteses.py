def isValid(s: str) -> bool:
    stack=[]
    fnf=False
    op,cl=0,0
    c="}])"
    e="{}","()","[]"
    for i in s:
        if i in "{[(":
            stack.append(i)
            op+=1
        else:
            cl+=1
            if len(stack)>0 :
                a=stack.pop()
                if a+i in e:
                    print(stack)
                    fnf=True
    print(op,cl)
    if stack != [] or op!=cl:
        fnf=False
    return fnf

print(isValid("({{{{}}}))"))