a = [[2, 3], [4, 6], [6, 1]]
b = sorted(a,key=lambda x:x[0])
a.sort(key=lambda x:x[1])
print(a)
print(b)