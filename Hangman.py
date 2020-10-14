import random

def find_word():
    words = open('Hangman_word_list.txt', 'r')
    lines = words.readlines()
    a = len(lines)
    count = random.randint(0, a)
    w = lines[count-1].rstrip('\n')
    words.close()

    return w


def count_letters(word_):
    list_of_letters = []
    for x in word_:
        if x not in list_of_letters:
            list_of_letters.append(x)

    return list_of_letters


word = find_word()
print(word)
tries = len(count_letters(word))
list_of_letter = count_letters(word)

while tries > 0:
    if len(list_of_letter) == 0:
        print("Hooray!, you have guessed the word")
    enter = input(">\n")
    if list_of_letter.count(enter) > 0:
        list_of_letter.remove(enter)
        print(f"Correct!\ntries:{tries}\n")
    else:
        tries -= 1
        print(f"Incorrect!\ntries:{tries}\n")
else:
    print(f"You have used up all of your tries!\nthe word was {word}")