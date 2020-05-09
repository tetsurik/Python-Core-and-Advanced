s = {10, 20, 30, "XYZ", 10}

print(type(s))

s.update([88,99])
print(s)
print(type(s))

s.remove(30)
print(s)

f = frozenset(s)
print(f)

#Assignment
s1 = {'Japan', 'America', 'China'}
print(s1)
s1.update(['Malaysia'])
print(s1)
s1.remove('Japan')
print(s1)
s1.update(['Taiwan'])
print(s1)