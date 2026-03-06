
def factorial(n):
    if n == 0:
        return 1
    else:
        fact=n*factorial(n-1)
    return fact

n=int(input ("Enter a number: "))
factorial_n=factorial(n)
print("The factorial of", n, "is", factorial_n)