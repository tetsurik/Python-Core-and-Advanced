lst = [10, 20, 'Tetsu', -10, 30.5]
print(lst)
print(lst[3])
print(lst[3:5])
print(lst*4)
print(len(lst))

lst.append(40)
lst.remove('Tetsu')
del(lst[1])
print(lst)

#lst.clear()
#print(lst)

print(max(lst))
print(min(lst))

lst.insert(3, 99)
print(lst)

lst.sort(reverse = True)
print(lst)

#Assignment
lst1 = ['Japan', 'America', 'China']
print(lst1)
lst1.append('Malaysia')
print(lst1)
del(lst1[2])
print(lst1)
lst1.insert(2, 'Taiwan')
print(lst1)
