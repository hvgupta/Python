restart = True


def bubble_sort(sequence):
    n = len(sequence)
    for x in range(0, n-1):
        for a in range(0, n-x-1):
            if numbers[a] < numbers[a+1]:
                numbers[a], numbers[a+1] = numbers[a+1], numbers[a]


def binary_search (sequence, x):
    sequence.sort()
    max_ = len(sequence) - 1
    min_ = 0
    while min_ <= max_:
        mid = int((max_ + min_)//2)
        if x > sequence[mid]:
            min_ = mid + 1
        elif x < sequence[mid]:
            max_ = mid - 1
        else:
            return print(f"{looking_for} is located at {mid + 1} of {sequence}")

    print("x is not found in sequence")
    return "unsuccessful"


while restart is True:
    numbers = input("input your list seperated with a space\n").split()
    looking_for = input("which number are you looking for\n")
    bubble_sort(numbers)
    binary_search(numbers, looking_for)
    res_ = input("Would you like to enter another list? (Y/N)\n")

    if res_.upper() == "Y":
        continue
    elif res_.upper() == "N":
        break
    else:
        print("Sorry, I don't understand what you entered. Please type Y for yes, and N for no")