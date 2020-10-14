a = []
x = input("please input numbers with space between them \n").split()
h = len(x) 
y = 0
for i in range(0,h):
    a.append(int(x[y]))
    y = y + 1    
a.sort()
z = len(a) - 1
w = str(a)
w = w.replace("[", "")
w = w.replace("]", "")
w = w.replace(",", "")
print(w)
print("The smallest number among the input is" , a[0] , "and the largest is" , a[z])