#Learning RETURN 

#without return
def maths(a,b,c, d):
    print(a+d)
    print(c+b)
    print(a+d+c+b)
    print(a-b-c)

maths(2,3,4,5)



#with return

def maths(a,b,c, d):
    print(a+d)
    print(c+b)
    return(print(a+d+c+b))
    print(a-b-c)

maths(2,3,4,5)