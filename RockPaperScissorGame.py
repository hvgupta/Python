import random
x = input("This is a rock paper scissors game, for rock type 'r', for paper type 'p' and for scissor type 's'\n")
z = 0
while True:
    while True:
        AI = ["r", "p", "s"]
        y = random.choice(AI)
        if x == "r" and y == "s":
            print("you won, the bot chose scissor")
            z = z + 1
            x = input("please choose from r, p and s again\n")
        elif x == "s" and y == "p":
            print("you won, the bot chose paper")
            z =z +1
            x = input("please choose from r, p and s again\n")
        elif x == "p" and y == "r":
            print("you won, the bot chose rock")
            z = z + 1
            x = input("please choose from r, p and s again\n")
        elif x == "r" and y == "r":
            print("it is a tie")
            x = input("please choose from r, p and s again\n")
        elif x == "s" and y == "s":
            print("it is a tie")
            x = input("please choose from r, p and s again\n")
        elif x == "p" and y == "p":
            print("it is a tie")
            x = input("please choose from r, p and s again\n")
        elif x == "r" and y == "p":
            print("you lost, the bot chose paper")
            break
        elif x == "p" and y == "s":
            print("you lost, the bot chose scissor")
            break
        elif x == "s" and y == "r":
            print("you lost, the bot chose rock")
            break
        else:
            print("please choose from r, p or s")
            x = input("please choose from r, p and s again\n")
    a = f"you won {z} times"
    print(a)
    aga = input("Do you want to try again (y/n)\n")
    if aga == "y":
        print("restarting the game")
        x = input("please choose between r, p and s \n")
    else:
        break