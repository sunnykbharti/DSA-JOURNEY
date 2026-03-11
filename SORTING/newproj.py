import random as r
def captcha():
    fnf=""
    a="qwertyuiopasdfghjklzxcvbnm"
    b="1234567890"
    for i in range(0,5):
        c=r.randint(1,2)
        if c==1:
            d=r.randint(0,25)
            fnf+=a[d]
        else:
            e=r.randint(0,9)
            fnf+=b[e]
    print(fnf)
    gen()



def gen():
    print("Welcome to captcha generator")
    z=input("Kindly enter to generate captcha")
    captcha()
gen()
