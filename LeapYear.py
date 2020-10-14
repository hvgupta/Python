x = []
y = 1
ThisYear = int(input("From which year do you want to start: "))
n = int(input("How many 'Leap years' do you want: "))
NewYear = ThisYear
while True:
    NewYear = NewYear + 1
    if y <= n:
        if NewYear % 4 == 0:
            x.append(NewYear)
            y = y + 1
        elif NewYear % 100 == 0 and NewYear % 400 == 0:
            x.append(NewYear)
            y = y + 1
    elif y > n:
        break
for i in x:
    print(i)
print(len(x))