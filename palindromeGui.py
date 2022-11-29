from graphics import *
from button import *

def main():

    win = GraphWin("Palindrome", 800, 600)
    win.setBackground("beige")

    Q = button(win, Point(650, 500), Point(750, 575), "tomato", "Quit")

    P = button(win, Point(350, 350), Point(450, 425), "cyan", "Check")

    E = Entry(Point(400, 300), 30)
    E.draw(win)

    T = Text(Point(400, 250), "Write something below that you think is a palindrome.")
    T.draw(win)

    pal = ""
    yes = Text(Point(400, 150), "")
    yes.draw(win)
    
    
    



    while True:
        m = win.getMouse()

        if Q.isClicked(m):
            break

        if P.isClicked(m):
            


            pal = E.getText()
            cap = pal.casefold()
            #test pal for palindrome
            #have a gui output
            
            print(cap)
            rev = cap [::-1]
            print(rev)
            if rev == cap:

                yes.setText(pal + " is a palindrome.")
                
                

            else:
                yes.setText(pal + " is not a palindrome.")
                

            



    win.close()
        
    

if __name__ == "__main__":
    main()
