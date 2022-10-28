
def prob1():
    myList = [1, 2, 3, 7, 4, 7]
    for i in range(len(myList)):
        if myList[i] == myList[i-1]:
            return True
        else:
            return False

def prob2():
    myList = [0, 4, 0, 3, 6]
    list2 = []
    for i in range(len(myList)):
        if myList[i] == 0:
            break
        list2.append(myList[i])
    h = sum(list2)
    print(h)



def prob3():
    myList = [1, 2, 8, 3, 6]
    list2 = []
    for i in range(len(myList)):
        if myList[i] == 2:
            while myList[i] != 3:
                i = i + 1
        else:
            list2.append(myList[i])
        
                
        

    h = sum(list2)
    print(h)


    
'''list2.append(myList[i])
        elif myList[i] != 3:
            list2.append(myList[i])
        else:
            sum(myList)'''
        







def main():
    prob3()
    










if __name__ == "__main__":
    main()
