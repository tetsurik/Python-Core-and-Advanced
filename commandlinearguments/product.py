import sys

lst = sys.argv
for i in range(1,3): lst[i] = int(lst[i])
print("product of ", lst[1], " and ", lst[2], " is: ", lst[1] * lst[2])