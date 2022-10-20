class Koala:
    def __init__(self, name, age, hungry):
        self.name = name
        self.age = age
        self.food = hungry

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getFood(self):
        return self.food


def main():
    l = Koala("Larry", 12, "very hungry")
    v = Koala("viola", 9, "Just Ate")


    print(l.getName() + ": " + str(l.getAge()) +" " + l.getFood())
    print(v.getName() + ": " + str(v.getAge()) +" " + v.getFood())
if __name__ == "__main__":
    main()
