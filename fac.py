n=int(input("Enter a number:"))
def fac(n):
    if n<2:
        return 1
    else:
        return n*fac(n-1)
res=fac(n)
print("Factorial of",n,"is:",res)