st=input("expression : ")
exp=st.split(" ")
stack=[]
eqn=""
for i in exp:
    if i[0] in "0123456789":
        stack.append(int(i))
    else:
        print(stack)
        b=stack.pop()
        a=stack.pop()
        stack.append(eval(str(a)+i+str(b)))
print(stack)