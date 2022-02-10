def calci(x,y,c):
    if c==1:
        return x+y
    if c==2:
        return x-y
    if c==3:
        return x*y
    if c==4:
        return x/y
    if c==5:
        return x%y
    else:
        return x+y,x-y,x*y,x/y,x%y 
print("Enter two numbers ")
a=int(input())
b=int(input())
print("Enter your choice\n1 for +\n2 for -\n3 for *\n4 for /\n5 for %\n6 for all")
c=int(input())
d=calci(a,b,c)
print("\nAnswer:",d)