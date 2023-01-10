from graphics import *

class fish:
    


    def __init__(self,win, posX, posY):
#
        self.win = win
#converts corinants to graphcis corodinants 
        self.posX = ((posX * 20) + 100)-10
        self.posY = ((posY * 20) + 100)-10
        self.posX2 = posX
        self.posY2 = posY
        

        





        
#creat and draw the fish object
    
        self.f = Image(Point(self.posX,self.posY),"fish.png")
        self.f.draw(win)
                  

    
        
        
    def getPosX(self):
        return self.posX2
    def getPosY(self):
        return self.posY2

#move function doesnt work :(
    #def move(self,x,y):
        #fish.move(20*x,20*y)
        
        






#I = Image(Point(300,300),"veitchii.png")
