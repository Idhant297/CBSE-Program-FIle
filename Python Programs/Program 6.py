x=int(input("Enter the number whose factorial you want to calculate- "))
fac=1
for i in range(x,1,-1):
    fac=fac*i
print("Factorial of",x,"is",fac)