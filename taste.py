def get_taste(input):
    taste =''
    if (input=="sugar"):
        taste ="Sweet"
    else:
        taste ="Salty"
    return taste




returned_taste = get_taste("salt")
print (returned_taste)

test = [1,2,3,4,5]
print(test[1])

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
hello_message = "Hello, " + full_name.title() + "!"
print(hello_message)
