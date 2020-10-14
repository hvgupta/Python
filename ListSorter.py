x = input("Input the numbers of the first list with spaces between the numbers\n").split()
a = []
h = len(x) 
y = 0
for i in range(0,h):
    a.append(int(x[y]))
    y = y + 1
z = input("Input the numbers of the second list with spaces between the numbers\n").split()
y = 0
b =[]
f = len(z) 
for i in range(0,f):
    b.append(int(z[y]))
    y = y + 1
c = []
for m in a:
    c.append(m)
for o in b:
    c.append(o)
c.sort()
print(c)