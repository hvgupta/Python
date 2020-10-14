a = []
print("Type in the word you want to check")
y = str(input())
y = y.replace(" ", "")
for i in y:
    a.append(i)
a.reverse()
a = str(a)
a = a.replace("[", "")
a = a.replace("]", "")
a = a.replace(",", "")
a = a.replace(" ", "")
a = a.replace("'", "")
if a == y:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")