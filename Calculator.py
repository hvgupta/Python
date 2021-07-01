#im not really sure how the functions work yet, but the next 53 lines of code saves the places of operators 
from datetime import datetime
def location_of_plus():
    global plusindex
    plusindex = []
    Index = 0
    for i in modifiedx:
        if i == "+":
            plusindex.append(Index)
        Index = Index + 1
    del i


def operation_locator(optype):
    global operator_index
    operator_index = []
    Index = 0
    for idx in modifiedx:
        if idx == optype:
            operator_index.append(Index)
        Index = Index + 1
    return operator_index


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

def Truemaker():
    global repeatedpower
    global repeatedmultiply
    global repeateddivide
    global repeatedadd
    global repeatedminus
    repeatedpower = True 
    repeatedmultiply = True
    repeateddivide = True
    repeatedadd = True
    repeatedminus = True 

#this is the main part of the calculator
x = input("Your input can include operations too like '( x + y ) ( x * y ) - ( z / a ) + ( x ^ 2 )'\n")
modifiedx = []
oldx = []
start1 = datetime.now()
for i in x.split(' '):
    try:
        j = float(i)
        modifiedx.append(j)
        oldx.append(j)
    except:
        modifiedx += list(i)
        oldx += list(i)
del i

Truemaker()
powerindex = []
multiplyindex = []
divideindex = []
plusindex = []
minusindex  = []

while len(modifiedx) != 1:
    while len(modifiedx) != 1:

        location_of_bracket()

        if len(operation_locator("^")) == 0 and '^' in modifiedx and len(backwardbracketindex) == 0 and repeatedpower == True or '^' in modifiedx and repeatedpower == True and modifiedx.index(')') > modifiedx.index('^') or oldx != modifiedx and '^' in modifiedx and repeatedpower == True and modifiedx.index(')') > modifiedx.index('^'):
            operation_locator('^')
            location_of_bracket()
            repeatedpower = False

        elif len(operator_index) != 0 and '^' in modifiedx and modifiedx[powerindex[0]-1] != ")":
            counter = 0
            for a in powerindex:
                if modifiedx[a-counter-1] == ")":
                    Truemaker()
                    break
                ans = float(modifiedx[(a-counter)-1] ** modifiedx[(a-counter)+1])
                modifiedx[a-counter] = ans
                del modifiedx[(a-counter)-1]
                del modifiedx[a-counter]
                if modifiedx[(a-counter)-2] == "(" and modifiedx[a-counter] == ")":
                    del modifiedx[a-counter]
                    del modifiedx[(a-counter)-2]
                    counter = counter + 2
                counter = counter + 2
        

        elif len(operation_locator("*")) == 0 and '*' in modifiedx and len(backwardbracketindex) == 0 and repeatedmultiply == True or '*' in modifiedx and repeatedmultiply == True and modifiedx.index(')') > modifiedx.index('*') or oldx != modifiedx and '*' in modifiedx and repeatedmultiply == True and modifiedx.index(')') > modifiedx.index('*'):
            operation_locator("*")
            location_of_bracket()
            repeatedmultiply = False

        elif len(operator_index) != 0 and '*' in modifiedx:
            counter = 0
            for b in multiplyindex:
                if modifiedx[b-counter-1] == ")":
                    Truemaker()
                    break
                ans = float(modifiedx[(b-counter)-1] * modifiedx[(b-counter)+1])
                modifiedx[b-counter] = ans
                del modifiedx[(b-counter)-1]
                del modifiedx[b-counter]
                if modifiedx[(b-counter)-2] == "(" and modifiedx[b-counter] == ")":
                    del modifiedx[b-counter]
                    del modifiedx[(b-counter)-2]
                    counter = counter + 2
                counter = counter + 2
        
        elif len(operation_locator("/")) == 0 and '/' in modifiedx and len(backwardbracketindex) == 0 and repeateddivide == True or '/' in modifiedx and repeateddivide == True and modifiedx.index(')') > modifiedx.index('/') or oldx != modifiedx and '/' in modifiedx and repeateddivide == True and modifiedx.index(')') > modifiedx.index('/'):
            operation_locator('/')
            location_of_bracket()
            repeateddivide = False

        elif len(operator_index) != 0 and '/' in modifiedx:
            counter = 0
            for c in divideindex:
                if modifiedx[c-counter-1] == ")":
                    Truemaker()
                    break
                ans = float(modifiedx[(c-counter)-1] / modifiedx[(c-counter)+1])
                modifiedx[c-counter] = ans
                del modifiedx[(c-counter)-1]
                del modifiedx[c-counter]
                if modifiedx[(c-counter)-2] == "(" and modifiedx[c-counter] == ")":
                    del modifiedx[c-counter]
                    del modifiedx[(c-counter)-2]
                    counter = counter + 2
                counter = counter + 2

        elif len(operation_locator("+")) == 0 and '+' in modifiedx and len(backwardbracketindex) == 0 and repeatedadd == True or '+' in modifiedx and repeatedadd == True and modifiedx.index(')') > modifiedx.index('+') or oldx != modifiedx and '+' in modifiedx and repeatedadd == True and modifiedx.index(')') > modifiedx.index('+'):
            operation_locator("+")
            location_of_bracket()
            repeatedadd = False

        elif len(operator_index) != 0 and '+' in modifiedx:
            counter = 0
            for d in plusindex:
                if modifiedx[d-counter-1] == ")":
                    Truemaker()
                    break
                ans = float(modifiedx[(d-counter)-1] + modifiedx[(d-counter)+1])
                modifiedx[d-counter] = ans
                del modifiedx[(d-counter)-1]
                del modifiedx[d-counter]
                if modifiedx[(d-counter)-2] == "(" and modifiedx[d-counter] == ")":
                    del modifiedx[d-counter]
                    del modifiedx[(d-counter)-2]
                    counter = counter + 2
                counter = counter + 2
        
        elif len(operation_locator("-")) == 0 and '-' in modifiedx and len(backwardbracketindex) == 0 and repeatedminus == True or '-' in modifiedx and repeatedminus == True and modifiedx.index(')') > modifiedx.index('-') or oldx != modifiedx and '-' in modifiedx and repeatedminus == True and modifiedx.index(')') > modifiedx.index('-'):
            operation_locator("-")
            location_of_bracket()
            repeatedminus = False

        elif len(operator_index) != 0 and '-' in modifiedx:
            counter = 0
            for e in minusindex:
                if modifiedx[e-counter-1] == ")":
                    Truemaker()
                    break
                ans = float(modifiedx[(e-counter)-1] - modifiedx[(e-counter)+1])
                modifiedx[e-counter] = ans
                del modifiedx[(e-counter)-1]
                del modifiedx[e-counter]
                if modifiedx[(e-counter)-2] == "(" and modifiedx[e-counter] == ")":
                    del modifiedx[e-counter]
                    del modifiedx[(e-counter)-2]
                    counter = counter + 2
                counter = counter + 2


modifiedx = str(modifiedx)
modifiedx = modifiedx.replace("[","")
modifiedx = modifiedx.replace("]","")
print(modifiedx)
end1 = datetime.now()
print(end1 - start1)