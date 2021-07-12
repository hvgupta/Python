import pickle
 
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
        or operator1 in modifiedx and counter == 0 and not operator2 in modifiedx and not modifiedx[modifiedx.index(operator1) - 1] == ")" and not modifiedx[modifiedx.index(operator1) + 1] == "(" 
        or operator1 == "^"):   
            allow = True
        else:
            allow = False
        return allow

    def CalculatorBody(modifiedx:list, opeator_locator:list, operationType:str, counter:int):
        for a in opeator_locator:
            if operationType == "^" and calculator.comparer("^","", modifiedx, counter) == True:
                ans = float(modifiedx[a-1-counter] ** modifiedx[a+1-counter])
            elif operationType == "*" and calculator.comparer("*","/", modifiedx, counter) == True:
                ans = float(modifiedx[a-1-counter] * modifiedx[a+1-counter])
            elif operationType == "/" and calculator.comparer("/","*", modifiedx, counter) == True:
                ans = float(modifiedx[a-1-counter] / modifiedx[a+1-counter])
            elif operationType == "+" and calculator.comparer("+","-", modifiedx, counter) == True:
                ans = float(modifiedx[a-1-counter] + modifiedx[a+1-counter])
            elif operationType == "-" and calculator.comparer("-","+", modifiedx, counter) == True:
                ans = float(modifiedx[a-1-counter] - modifiedx[a+1-counter])
            modifiedx[a-counter] = ans
            del modifiedx[a-1-counter]
            del modifiedx[a-counter]
            counter +=2
            if modifiedx[a-counter] == "(" and modifiedx[a + 2-counter] == ")":
                del modifiedx[a]
                del modifiedx[a-2]
                counter +=2
        counter = 0

x = "placeholder"

while x.lower() != "off":
    modifiedx=[]
    try:
        Ans = pickle.load(open("Ans","rb"))[0]
        x = input("You have an answer stored in this Calculator, to use it use 'ans' or 'Ans or if you want to turn off the calculator then type 'off' \n")
        x = x.replace("ans",str(Ans))
    except:
        x = input("Your input can include operations too like '(x+y)(x*y)-(z/a)+(x^2)'\n")

    if x.lower() == "off":
        break
    num=''
    temp = []
    counter = -1
    for i in [i for i in x]:
        if i.isnumeric() == True or i == ".":
            num += i
            temp.append(num)
            counter += 1
        else:
            if counter >= 0:
                modifiedx.append(float(temp[counter]))
                counter = -1
                temp =[]        
            modifiedx.append(i)
            num = ''
    if not len(temp) == 0:
        modifiedx.append(float(temp[counter]))
        temp = []

    for i in calculator.location_of_operator("-"):
        if i - 1 in calculator.location_of_operator("^") or i - 1 in calculator.location_of_operator("*") or i - 1 in calculator.location_of_operator("/"):
            modifiedx.insert(i,0)
            modifiedx.insert(i,"(")
            modifiedx.insert(i+5,")")
    
    counter = 0
    location_of_fbracket=calculator.location_of_operator("(")
    location_of_bbracket=calculator.location_of_operator(")")

    for a in location_of_fbracket:
        if a - 1 in location_of_bbracket and a + 2 in location_of_bbracket or a - 1 in location_of_bbracket and not a + 2 in location_of_bbracket and a - 2 in location_of_fbracket:
            modifiedx.insert(a-counter,"*")
            del modifiedx[a-1-counter-counter]
            del modifiedx[a-counter]
            counter =+ 1
        elif a - 1 in location_of_bbracket and not a + 2 in location_of_bbracket and not a - 2 in location_of_bbracket:
            modifiedx.insert(a-counter,"*")
            counter =- 1

    counter = 0

    while len(modifiedx) != 1:

        calculator.CalculatorBody(modifiedx,calculator.location_of_operator("^"),"^",counter)

        calculator.CalculatorBody(modifiedx,calculator.location_of_operator("*"),"*",counter)

        calculator.CalculatorBody(modifiedx,calculator.location_of_operator("/"),"/",counter)      
        
        calculator.CalculatorBody(modifiedx,calculator.location_of_operator("+"),"+",counter)

        calculator.CalculatorBody(modifiedx,calculator.location_of_operator("-"),"-",counter)

    pickle.dump(modifiedx,open("Ans","wb"))
    print(modifiedx[0])