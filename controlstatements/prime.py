primeFlag=True

n = int(input("Enter number: "))

i = n - 1

while i > 1:
    if n % i == 0:
        primeFlag = False
        break
    i-=1

if primeFlag == True: print(n, " is prime")
else: print(n, " is not prime")
