class Cat:
#how it is constructed/constructer method/defines how the cat is intially created
    def __init__(self, name, age):
        #Instance varibles
        self.fur = "fluffy"
        self.age = age
        self.color = "black"
        self.name = name

    def getAge(self):
        return self.age
    #getter/returns age

    def getName(self):
        return self.name
        





def main():

    c = Cat("Mittens", 20)
    d = Cat("Deric", 3)

    '''print("Hi cat, what is your name?")

    print(c.getName())
    #call the cat name

    print("Hi cat, what is your name?")

    print(d.getName())'''

    print("cat's ages:")
    print(c.getName() + ": " + str(c.getAge()))
    print(d.getName() + ": " + str(c.getAge()))



if __name__ == "__main__":
    main()
