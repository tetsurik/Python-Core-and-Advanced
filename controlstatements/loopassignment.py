x = int(input("Enter a number: "))
i = 1
for i in range(i, x):
    if (i - 1) % 10 == 0: continue
    print(i)