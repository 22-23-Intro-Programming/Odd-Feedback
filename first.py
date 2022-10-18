def add3(x):
    #anything here is add3 method definition
    result = x + 3
    return result



def main():
    #print("Hello world")
    '''print(1234)

    hello = "Hello Class"
    numStudents = 13
    print(hello + " there are " + str(numStudents) + " of you today ")'''

    '''x = input("What is your favorite number?")
    #print(x)
    x = int(x)
    if x > 10:
        print(x / 2)
    else:
        print(x + 1)'''

    res = add3(12)
    print(res)
    print(add3(100))

    myString = "Mr. Considine"
    firstChar = myString[0]
    seveth = myString[6]
    #print(firstChar)

    for char in myString:
        print(char)

    print(8 % 3)



if __name__ == "__main__":
    main()

