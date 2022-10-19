    
def palindrome():
    stop = 4
    while stop != "stop":
        word = input(" Please enter a potential palindrome ")
        if word == "stop":
            break
        else:
            reverse = word [::-1]
            if reverse == word:
                print(" yes, " + word + " is a palindrome ")
            else:
                print(" No, " + word + " is not a palindrome ")


def greeting():
    name = input("What is your name?")
    print(" How nice to meet you " + str(name) + "!  Have a Fantastic Day!")


def isMultiple():
    num2 = input(" number 1 ")
    num1 = input(" number 2 ")
    if int(num2) % int(num1) == 0:
                       print(str(num1) + " is a multiple of " + str(num2))
    else:
        print(str(num1) + " is not a multiple of " + str(num2))



    
def main():
    program = input("Which program do you want to run? greeting, factor or Palindrome")
    if program == "greeting":
        res = greeting()
    if program == "factor":
        res = isMultiple()
    if program == "palindrome":
        res = palindrome()
    








if __name__ == "__main__":
    main()


