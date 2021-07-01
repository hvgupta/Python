import pickle
from datetime import datetime
start1 = datetime.now()
 
class calculator:
    def location_of_operator(operatorType):
        operator_index = []
        Index = 0
        for i in modifiedx:
            if i == operatorType:
                operator_index.append(Index)
            Index = Index + 1
        return operator_index

    def comparer(operator1:str,operator2:str, modifiedx:list, counter:int):
        if (operator1 in modifiedx and operator2 in modifiedx and not modifiedx[modifiedx.index(operator1) - 1] == ")" and not modifiedx[modifiedx.index(operator1) + 1] == "(" and modifiedx.index(operator1)< modifiedx.index(operator2) and counter == 0 
        or operator1 in modifiedx and not modifiedx[modifiedx.index(operator1) - 1] == ")" and not modifiedx[modifiedx.index(operator1) + 1] == "(" and not modifiedx[modifiedx.index(operator1) - 1] == ")" and not modifiedx[modifiedx.index(operator1) + 1] == "(" and counter==0 
        or operator1 in modifiedx and operator2 in modifiedx and modifiedx.index(operator1)< modifiedx.index(operator2) and not modifiedx[modifiedx.index(operator1) - 1] == ")" and not modifiedx[modifiedx.index(operator1) + 1] == "(" and counter == 0 
        or operator1 in modifiedx and counter == 0 and not operator2 in modifiedx and not modifiedx[modifiedx.index(operator1) - 1] == ")" and not modifiedx[modifiedx.index(operator1) + 1] == "("):
            allow = True
        else:
            allow = False
        return allow

    def CalculatorBody(modifiedx:list, opeator_locator:list, operationType:str, counter:int):
        for a in opeator_locator:
            if operationType == "^":
                ans = float(modifiedx[a-1] ** modifiedx[a+1])
            elif operationType == "*":
                ans = float(modifiedx[a-1] * modifiedx[a+1])
            elif operationType == "/":
                ans = float(modifiedx[a-1] / modifiedx[a+1])
            elif operationType == "+":
                ans = float(modifiedx[a-1] + modifiedx[a+1])
            elif operationType == "-":
                ans = float(modifiedx[a-1] - modifiedx[a+1])
            counter = 1
            break
        counter = 0
        modifiedx[a] = ans
        del modifiedx[a-1]
        del modifiedx[a]
        if modifiedx[a-2] == "(" and modifiedx[a] == ")":
            del modifiedx[a]
            del modifiedx[a-2]

x = "placeholder"

while x.lower() != "off":
    modifiedx=[]
    try:
        Ans = pickle.load(open("Ans","rb"))[0]
        x = input("You have an answer stored in this Calculator, to use it use 'ans' or 'Ans or if you want to turn off the calculator then type 'off' \n")
        x = x.replace("ans",str(Ans))
    except:
        x = input("Your input can include operations too like '( x + y ) ( x * y ) - ( z / a ) + ( x ^ 2 )'\n")

    if x.lower() == "off":
        break
    num=''
    temp = []
    count = -1
    for i in [i for i in x]:
        if i.isnumeric() == True:
            num += i
            temp.append(num)
            count += 1
        else:
            if count >= 0:
                modifiedx.append(float(temp[count]))        
            modifiedx.append(i)
            num = ''
        if not num == "":
            modifiedx.append(float(temp[count]))
        break

    counter = 0
    location_of_fbracket=calculator.location_of_operator("(")
    location_of_bbracket=calculator.location_of_operator(")")

    for a in location_of_fbracket:
        if a - 1 in location_of_bbracket and a + 2 in location_of_bbracket:
            modifiedx.insert(a-counter,"*")
            del modifiedx[a-1-counter]
            del modifiedx[a-counter]
            counter =+ 1 
        elif a - 1 in location_of_bbracket and not a + 2 in location_of_bbracket and a - 2 in location_of_fbracket:
            modifiedx.insert(a-counter,"*")
            del modifiedx[a-1-counter]
            del modifiedx[a-counter]
            counter =+ 1
        elif a - 1 in location_of_bbracket and not a + 2 in location_of_bbracket and not a - 2 in location_of_bbracket:
            modifiedx.insert(a-counter,"*")
            counter =- 1

    counter = 0

    while len(modifiedx) != 1:

        if calculator.comparer("^", "", modifiedx, counter) == True:
            calculator.CalculatorBody(modifiedx,calculator.location_of_operator("^"),"^",counter)

        if calculator.comparer("*","/", modifiedx, counter) == True:
            calculator.CalculatorBody(modifiedx,calculator.location_of_operator("*"),"*",counter)

        if calculator.comparer("/","*", modifiedx, counter) == True:
            calculator.CalculatorBody(modifiedx,calculator.location_of_operator("/"),"/",counter)      
        
        if calculator.comparer("+","-", modifiedx, counter) == True:
            calculator.CalculatorBody(modifiedx,calculator.location_of_operator("+"),"+",counter)

        if calculator.comparer("-","+", modifiedx, counter) == True:
            calculator.CalculatorBody(modifiedx,calculator.location_of_operator("-"),"-",counter)

    pickle.dump(modifiedx,open("Ans","wb"))
    end1 = datetime.now()
    print(modifiedx[0])
    print(end1-start1)