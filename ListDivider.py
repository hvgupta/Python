a = []
b = []
c = []
h = 1
x = input("Please input the numbers with space between them\n").split()
o = len(x) 
y = 0
a = []
for i in range(0,o):
    a.append(int(x[y]))
    y = y + 1
for i in a:
    if h % 2 == 0:
        b.append(i)
        h = h + 1
    elif h % 2 != 0:
        c.append(i)
        h = h + 1
a = str(a)
b = str(b)
c = str(c)
a = a.replace("[", "")
b = b.replace("[", "")
c = c.replace("[", "")
a = a.replace("]", "")
b = b.replace("]", "")
c = c.replace("]", "")
print("the entire list consists", a)
print("the numbers on odd positions are", c)
print("the numbers on even positions are", b)