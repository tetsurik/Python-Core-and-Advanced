maths, physics, chemistry = [float(x) for x in (input("Enter your math, physics, and chemistry grades seperated by a space: ").split())]

if maths < 35 or physics < 35 or chemistry < 35: print("You have failed")
else:
    average = (maths + physics + chemistry) / 3
    if average <= 59: print("You got a C with an average of ", average)
    elif average <= 69: print("You got a B with an average of ", average)
    else: print("You got an A with an average of ", average)