import time
print("how many lines do you want")
x = int(input())
q = x
y = "*"
a = " "
while True :
    print("do you want a pyramid or a stair")
    z = input()
    if z == "stair":
        for i in range(1, x + 1):
            print(y * i)
            time.sleep(0.2)
        break 
    elif z == "pyramid":
        for i in range(1, x + 1):
            i = 2 * i -1
            q = q - 1
            print(a * q + y * i)
            time.sleep(0.2)
        break 
    else:
        print("please input 'pryramid' or 'stair'")
print("please restart the programme")