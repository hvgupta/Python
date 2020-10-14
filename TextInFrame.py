print("what do you want in  a frame")
x = input()
x = x + " "
f = "*" 
k = 0
g = []
w = []
a = x.replace(" ", "\n")
for i in a :
    if i == "\n":
        k += 1
        b = a.find("\n")
        u = a[0:b+1]
        o = "\n" + u
        w.append(o)
        g.append(b)
        a = a.replace(u, "")
n = max(g) + 2
r = " "
print(f * n)
for j in w:
    d = str(j)
    d = d.strip("\n")
    h = d + "\n"
    e = h.find("\n")
    p = n - (e + 2)     
    print("*" + d + r * p + "*")
print(f * n)