#im not really sure how the functions work yet, but the next 53 lines of code saves the places of operators 
def location_of_plus():
    global plusindex
    plusindex = []
    Index = 0
    for i in modifiedx:
        if i == "+":
            plusindex.append(Index)
        Index = Index + 1
    del i

def location_of_minus():
    global minusindex
    minusindex = []
    Index = 0
    for i in modifiedx:
        if i == "-":
            minusindex.append(Index)
        Index = Index + 1
    del i 

def location_of_multiply():
    global multiplyindex
    multiplyindex = []
    Index = 0
    for i in modifiedx:
        if i == "*":
            multiplyindex.append(Index)
        Index = Index + 1
    del i

def location_of_divide():
    global divideindex
    divideindex = []
    Index = 0
    for i in modifiedx:
        if i == "/":
            divideindex.append(Index)
        Index = Index + 1
    del i

def location_of_bracket():
    global forwardbracketindex
    global backwardbracketindex
    forwardbracketindex = []
    backwardbracketindex = []
    Index = 0
    for i in modifiedx:
        if i == "(":
            forwardbracketindex.append(Index)
        elif i == ")":
            backwardbracketindex.append(Index)
        Index = Index + 1
    del i 

def location_of_power():
    global powerindex
    powerindex = []
    Index = 0
    for i in modifiedx:
        if i == "^":
            powerindex.append(Index)
        Index = Index + 1
    del i 

#this is the main part of the calculator
x = input("Your input can include operations too like '( x + y ) ( x * y ) - ( z / a ) + ( x ^ 2 )'\n")
modifiedx = []
for i in x.split(' '):
    try:
        j = int(i)
        modifiedx.append(j)
    except:
        modifiedx += list(i)
del i

while len(modifiedx) != 1:
    while len(modifiedx) != 1:

        newx = []
        location_of_bracket()
        location_of_divide()
        location_of_minus()
        location_of_multiply()
        location_of_plus()
        location_of_power()


        if len(powerindex) != 0 and modifiedx[powerindex[0]-1] != ")":
            for g in powerindex:
                n = powerindex[0]
                ans = modifiedx[n-1] ** modifiedx[n+1]
                modifiedx[n] = ans
                del modifiedx[n-1]
                del modifiedx[n]
                if modifiedx[n-2] == "(" and modifiedx[n] == ")":
                    del modifiedx[n]
                    del modifiedx[n-2]
                location_of_power()
                del g


        elif len(multiplyindex) != 0 and modifiedx[multiplyindex[0]-1] != ")":
            location_of_multiply()
            location_of_bracket()
            for g in multiplyindex:
                n = multiplyindex[0]
                ans = modifiedx[n-1] * modifiedx[n+1]
                modifiedx[n] = ans
                del modifiedx[n-1]
                del modifiedx[n]
                if modifiedx[n-2] == "(" and modifiedx[n] == ")":
                    del modifiedx[n]
                    del modifiedx[n-2]
                location_of_multiply()
                del g

        elif len(divideindex) != 0 and modifiedx[divideindex[0]-1] != ")":
            location_of_divide()
            for g in divideindex:
                n = divideindex[0]
                ans = modifiedx[n-1] / modifiedx[n+1]
                modifiedx[n] = ans
                del modifiedx[n-1]
                del modifiedx[n]
                if modifiedx[n-2] == "(" and modifiedx[n] == ")":
                    del modifiedx[n]
                    del modifiedx[n-2]
                location_of_divide()
                del g

        elif len(plusindex) != 0 and modifiedx[plusindex[0]-1] != ")":
            location_of_plus()
            for g in plusindex:
                n = plusindex[0]
                ans = modifiedx[n-1] + modifiedx[n+1]
                modifiedx[n] = ans
                del modifiedx[n-1]
                del modifiedx[n]
                if modifiedx[n-2] == "(" and modifiedx[n] == ")":
                    del modifiedx[n]
                    del modifiedx[n-2]
                location_of_plus()
                del g

        elif len(minusindex) != 0 and modifiedx[minusindex[0]-1] != ")":
            location_of_minus()
            for g in minusindex:
                n = minusindex[0]
                ans = modifiedx[n-1] + modifiedx[n+1]
                modifiedx[n] = ans
                del modifiedx[n-1]
                del modifiedx[n]
                if modifiedx[n-2] == "(" and modifiedx[n] == ")":
                    del modifiedx[n]
                    del modifiedx[n-2]
                location_of_minus()
                del g
modifiedx = str(modifiedx)
modifiedx = modifiedx.replace("[","")
modifiedx = modifiedx.replace("]","")
print(modifiedx)