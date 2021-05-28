import pickle

def location_of_operator(operatorType):
    operator_index = []
    Index = 0
    for i in modifiedx:
        if i == operatorType:
            operator_index.append(Index)
        Index = Index + 1
    return operator_index

def comparer(operator1:str,operator2:str, modifiedx:list, counter:int):
    if (operator1 in modifiedx and operator2 in modifiedx and ')' in modifiedx and not modifiedx.index(operator1) > modifiedx.index(operator2) and modifiedx.index(operator1)< modifiedx.index(operator2) and counter == 0 
    or operator1 in modifiedx and ')' in modifiedx and not modifiedx.index(operator1) > modifiedx.index(")") and counter==0 
    or operator1 in modifiedx and operator2 in modifiedx and modifiedx.index(operator1)< modifiedx.index(operator2) and counter == 0 
    or  operator1 in modifiedx and counter == 0 and not operator2 in modifiedx):
        allow = True
    else:
        allow = False
    return allow

modifiedx=[]
try:
    Ans = pickle.load(open("Ans","rb"))[0]
    x = input("Your input can include operations too like '( x + y ) ( x * y ) - ( z / a ) + ( x ^ 2 )'\nYou have an answer stored in this calculator, to use it use 'ans' or 'Ans \n")
except:
    x = input("Your input can include operations too like '( x + y ) ( x * y ) - ( z / a ) + ( x ^ 2 )'\n")

for i in x.split(' '):
    try:
        j = float(i)
        modifiedx.append(j)
    except:
        if i == "Ans" or i == "ans":
            modifiedx.append("Ans")
            modifiedx.insert(modifiedx.index("Ans"), Ans)
            modifiedx.remove(modifiedx[modifiedx.index("Ans")])
        else:
            modifiedx += list(i)

counter = 0

while len(modifiedx) != 1:
    while len(modifiedx) != 1:

        if '^' in modifiedx and ')' in modifiedx and not modifiedx.index("^") > modifiedx.index(")") and counter == 0 or '^' in modifiedx and counter == 0:
            power_location= location_of_operator("^")
            for a in power_location:
                if modifiedx[a-counter-1] == ")" or modifiedx[a-counter+1] == "(":
                    break
                ans = float(modifiedx[(a-counter)-1] ** modifiedx[(a-counter)+1])
                counter = 1
                break
    
        allow = comparer("*","/", modifiedx, counter)

        if allow == True:
            multiply_location=location_of_operator("*")            
            a = multiply_location[0]
            if modifiedx[a-counter-1] == ")" or modifiedx[a-counter+1] == "(":
                break
            ans = float(modifiedx[(a-counter)-1] * modifiedx[(a-counter)+1])
            counter = 1
            break

        allow = comparer("/","*", modifiedx, counter)
        
        if allow == True:
            divisor_location=location_of_operator("/")
            a = divisor_location[0]
            if modifiedx[a-counter-1] == ")" or modifiedx[a-counter+1] == "(":
                break
            ans = float(modifiedx[(a-counter)-1] / modifiedx[(a-counter)+1])
            counter = 1 
            break          
        
        allow = comparer("+","-", modifiedx, counter)

        if allow == True:
            addition_location=location_of_operator("+")
            a = addition_location[0]
            if modifiedx[a-counter-1] == ")" or modifiedx[a-counter+1] == "(":
                break
            ans = float(modifiedx[(a-counter)-1] + modifiedx[(a-counter)+1])
            counter = 1
            break

        allow = comparer("-","+", modifiedx, counter)

        if allow == True:
            minus_location=location_of_operator("-")
            a = minus_location[0]
            if modifiedx[a-counter-1] == ")" or modifiedx[a-counter+1] == "(":
                break
            ans = float(modifiedx[(a-counter)-1] - modifiedx[(a-counter)+1])
            counter = 1  
            break  
   
        counter = 0 
        modifiedx[a-counter] = ans
        del modifiedx[a-1]
        del modifiedx[a]
        if modifiedx[a-2] == "(" and modifiedx[a] == ")":
            del modifiedx[a]
            del modifiedx[a-2]  

pickle.dump(modifiedx,open("Ans","wb"))
modifiedx = str(modifiedx)
modifiedx = modifiedx.replace("[","")
modifiedx = modifiedx.replace("]","")
print(modifiedx)