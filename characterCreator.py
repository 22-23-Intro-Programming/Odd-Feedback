from graphics import*
from button import*



    

    
def main():

    win = GraphWin("Character Creator", 800, 800)
    face = Oval(Point(100, 100), Point(500, 600))
    face.draw(win)
    


    Beyes = button(win, Point(525, 100), Point(625, 175), "blue", "Blue Eyes")
    Geyes = button(win, Point(650, 100), Point(750, 175), "green", "Green Eyes")


    bigNoseB = button(win, Point(525, 200), Point(625, 275), "purple", "Big Nose")
    smallNoseB = button(win, Point(650, 200), Point(750, 275), "yellow", "Small Nose")

    smileB = button(win, Point(525, 300), Point(625, 375), "orange", "Straight Mouth")
    frownB = button(win, Point(650, 300), Point(750, 375), "turquoise", "Suprised Mouth")

    line1 = Line(Point(200, 500), Point(400, 500))

    suprisedMouth = Circle(Point(300, 500), 60)

    
    


    Qbutton = button(win, Point(600, 625), Point(750, 725), "red", "Quit")

    Eye1 = Circle(Point(200,250), 50)
    Eye2 = Circle(Point(400,250), 50)

    Eye1.draw(win)
    Eye2.draw(win)

    Pupil1 = Circle(Point(200,250), 20)
    Pupil2 = Circle(Point(400,250), 20)

    
    bigNose = Polygon(Point(300, 250), Point(250, 400), Point(350, 400))
    smallNose = Polygon(Point(300, 325), Point(250, 400), Point(350, 400))


    
    #blue eyes
    Beye1 = Circle(Point(200,250), 40) 
    Beye2 = Circle(Point(400,250), 40)

    #green eyes
    Geye1 = Circle(Point(200,250), 40)
    Geye2 = Circle(Point(400,250), 40)

    eyes = [Beye1, Beye2, Geye1, Geye2, Pupil1, Pupil2]
    noses = [bigNose, smallNose]

    while True:
        m = win.getMouse()
        if Beyes.isClicked(m):
            #undraws all eyes in the list 
            for e in eyes:
                e.undraw()

        

            Beye1.draw(win)
            Beye2.draw(win)
            Beye1.setFill("blue")
            Beye2.setFill("blue")

            Pupil1.draw(win)
            Pupil2.draw(win)
    
            Pupil1.setFill("black")
            Pupil2.setFill("black")
            
            
        elif Geyes.isClicked(m):
            
            for e in eyes:
                e.undraw()


            

            Geye1.draw(win)
            Geye2.draw(win)
            Geye1.setFill("green")
            Geye2.setFill("green")

            Pupil1.draw(win)
            Pupil2.draw(win)
    
            Pupil1.setFill("black")
            Pupil2.setFill("black")



        elif bigNoseB.isClicked(m):
            smallNose.undraw()
            bigNose.undraw()

            bigNose.draw(win)

        elif smallNoseB.isClicked(m):
            smallNose.undraw()
            bigNose.undraw()
            

            smallNose.draw(win)


        elif smileB.isClicked(m):
            line1.undraw()
            suprisedMouth.undraw()

            line1.draw(win)



        elif frownB.isClicked(m):
            line1.undraw()
            suprisedMouth.undraw()

            suprisedMouth.draw(win)


        #more buttons
        elif Qbutton.isClicked(m):
            break
    win.close()

if __name__ == "__main__":
    main()
