import pickle
 
class calculator:
    def location_of_operator(operatorType, modifiedx):
        operator_index = []
        Index = 0
        for i in modifiedx:
            if i == operatorType:
                operator_index.append(Index)
            Index = Index + 1
        return operator_index

    def comparer(operator1:str,operator2:str, modifiedx:list, index:int):
        temp = ["*","/"]
        if( operator1 in modifiedx and operator2 in modifiedx and operator1 in temp and index<modifiedx.index(operator2)                                                                                                                                                   
            or operator1 in modifiedx and not operator2 in modifiedx
                      
            or operator1 in modifiedx and operator2 in modifiedx and not operator1 in temp and not temp in modifiedx and index<modifiedx.index(operator2)
            or operator1 in modifiedx and not operator2 in modifiedx and not operator1 in temp and not temp in modifiedx):
            allow = True
        else:
            allow = False
        return allow
    
    def bracket_solving(forward_brackets:list, backward_brackets:list, modifiedx:list):
        try:
            temp = modifiedx[forward_brackets[len(forward_brackets)-1]+1:backward_brackets[0]]
        except:
            temp = modifiedx
        return temp
    
    def appender(newx:list, modifiedx:list, lenght:int, forward_brackets:list):
        try:
            modifiedx.insert(forward_brackets[len(forward_brackets)-1], newx[0])
            del modifiedx[forward_brackets[len(forward_brackets)-1]+1:forward_brackets[len(forward_brackets)-1]+3+lenght]
        except:
            modifiedx = newx
        return modifiedx

    def CalculatorBody(modifiedx:list, opeator_locator:list, operationType:str):
        counter = 0
        for a in opeator_locator:
            allow = False
            if operationType == "^" and calculator.comparer("^","", modifiedx, a) == True:
                ans = float(modifiedx[a-1-counter] ** modifiedx[a+1-counter])
                allow = True
            elif operationType == "*" and calculator.comparer("*","/", modifiedx, a) == True:
                ans = float(modifiedx[a-1-counter] * modifiedx[a+1-counter])
                allow = True
            elif operationType == "/" and calculator.comparer("/","*", modifiedx, a) == True:
                ans = float(modifiedx[a-1-counter] / modifiedx[a+1-counter])
                allow = True
            elif operationType == "+" and calculator.comparer("+","-", modifiedx, a) == True:
                ans = float(modifiedx[a-1-counter] + modifiedx[a+1-counter])
                allow = True
            elif operationType == "-" and calculator.comparer("-","+", modifiedx, a) == True:
                ans = float(modifiedx[a-1-counter] - modifiedx[a+1-counter])
                allow = True
            if allow == True:
                try :
                    modifiedx[a-counter] = ans
                    del modifiedx[a-1-counter]
                    del modifiedx[a-counter]
                    counter +=2
                    if modifiedx[a-counter] == "(" and modifiedx[a + 2-counter] == ")":
                        del modifiedx[a]
                        del modifiedx[a-2]
                        counter +=2
                except:
                    pass
        counter = 0

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

    for i in calculator.location_of_operator("-", modifiedx):
        if i - 1 in calculator.location_of_operator("^", modifiedx) or i - 1 in calculator.location_of_operator("*", modifiedx) or i - 1 in calculator.location_of_operator("/", modifiedx):
            modifiedx.insert(i,0)
            modifiedx.insert(i,"(")
            modifiedx.insert(i+5,")")
    
    counter = 0
    location_of_fbracket=calculator.location_of_operator("(", modifiedx)
    location_of_bbracket=calculator.location_of_operator(")", modifiedx)

    for a in location_of_fbracket:
        if a - 1 + counter in location_of_bbracket and a + 2 + counter in location_of_bbracket or a - 1 + counter in location_of_bbracket and not a + 2 + counter in location_of_bbracket and a - 2 + counter in location_of_fbracket:
            modifiedx.insert(a-counter,"*")
            del modifiedx[a-1-counter-counter]
            del modifiedx[a-counter]
            counter =- 1    
        elif a - 1 + counter in location_of_bbracket and not a + 2 + counter in location_of_bbracket and not a - 2 + counter in location_of_bbracket or isinstance(modifiedx[a-1 + counter],float) == True:
            modifiedx.insert(a-counter,"*")
            counter =+ 1 

    counter = 0

    while len(modifiedx) != 1:

        newx = calculator.bracket_solving(calculator.location_of_operator("(", modifiedx), calculator.location_of_operator(")", modifiedx), modifiedx)
        lenght = len(newx)

        while len(newx) != 1:

            calculator.CalculatorBody(newx,calculator.location_of_operator("^", newx),"^")

            calculator.CalculatorBody(newx,calculator.location_of_operator("*", newx),"*")

            calculator.CalculatorBody(newx,calculator.location_of_operator("/", newx),"/")      
            
            calculator.CalculatorBody(newx,calculator.location_of_operator("+", newx),"+")

            calculator.CalculatorBody(newx,calculator.location_of_operator("-", newx),"-")

        modifiedx = calculator.appender(newx,modifiedx,lenght,calculator.location_of_operator("(", modifiedx))

    pickle.dump(modifiedx,open("Ans","wb"))
    print(modifiedx[0])