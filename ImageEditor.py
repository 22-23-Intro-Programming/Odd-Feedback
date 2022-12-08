from button import *
from graphics import *


def darken(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            r,g,b = pix[0], pix[1], pix[2]
            r = r - 50
            g = g - 50
            b = b - 50
            if r <= 0:
                r = 0
            if g <= 0:
                g = 0
            if b <= 0:
                b = 0
            newColor = color_rgb(r, g, b)

            img.setPixel(i,j,newColor)



    return True


def lighten(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            r,g,b = pix[0], pix[1], pix[2]
            
            r = r + 50
            g = g + 50
            b = b + 50
            if r >= 255:
                r = 255
            if g >= 255:
                g = 255
            if b >= 255:
                b = 255
            newColor = color_rgb(r, g, b)

            img.setPixel(i,j,newColor)

    return True

def grayScale(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            r,g,b = pix[0], pix[1], pix[2]
            add = r + g + b
            avg = add//3
            
            grayColor = color_rgb(avg, avg, avg)

            img.setPixel(i,j,grayColor)

    return True
    
def contrast(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            r,g,b = pix[0], pix[1], pix[2]

            add = r + g + b
            avg = add//3

            if avg <= 128:
                r = r - 50

                g = g - 50

                b = b - 50
                if r <= 0:
                    r = 0
                if g <= 0:
                    g = 0
                if b <= 0:
                    b = 0

            

            else:
                r = r + 50

                g = g + 50

                b = b + 50

                if r >= 255:
                    r = 255
                if g >= 255:
                    g = 255
                if b >= 255:
                    b = 255


            conColor = color_rgb(r, g, b)

            img.setPixel(i,j,conColor)



            
            
def blur(img):
    x = img.getWidth()
    y = img.getHeight()
    r = []
    g = []
    b = []
    

    for i in range(x):
        for j in range(y):
            
            pix = img.getPixel(i,j)
            r,g,b = pix[0], pix[1], pix[2]

            for k in range(3):
                    for o in range(3):
                        x1 = i + k
                        y1 = j + o
                        pix1 = img.getPixel(x1,y1)
                        r1,g1,b1 = pix1[0],pix1[1],pix1[2]
                        r.append(str(r1))
                        g.append(str(g1))
                        b.append(str(b1))
                        
                        for w in range(9):
                            total = 0

                            capr = r[w] + total
                            avgr = total/9
                        for t in range(9):
                            total = 0

                            capg = g[t] + total
                            avgg = total/9
                        for h in range(9):
                            total = 0

                            capb = b[h] + total
                            avgb = total/9

                            





            blurColor = color_rgb(avgr,avgg,avgb)
            img.setPixel(i,j,blurColor)
                            
                            
                        

                        
                        
                

            

            






            '''blurcolor = color_rgb(r,g,b)
            if i == 0:
                i = 5
                

            if j == 0:
                j = 5

            else:
                for k in range(5):
                    for o in range(5):
               
    
                        img.setPixel(i+k,j+o,blurcolor)
                        img.setPixel(i - k ,j - 0,blurcolor)'''
            
                
    






    return True
    
            
                





def main():

    win = GraphWin("Image editor", 800, 600)
    win.setBackground("white")
    l = [0,0,0]
    I = Image(Point(300,300),"veitchii.png")
    I.draw(win)
    Qbutton = button(win, Point(600, 500), Point(750, 600), "tomato", "Quit")
    B = button(win, Point(600,100), Point(700,175),"cyan", "Darken")
    A = button(win, Point(600,200), Point(700,275),"cyan", "Lighten")
    C = button(win, Point(600,300), Point(700,375),"cyan", "Gray Scale")
    D = button(win, Point(600,400), Point(700,475),"cyan", "Contrast")
    E = button(win, Point(700,400), Point(800,475),"cyan", "Blur")





    while True:
        m = win.getMouse()
        if B.isClicked(m):
            darken(I)
        if A.isClicked(m):
            lighten(I)
        if C.isClicked(m):
            grayScale(I)
        if D.isClicked(m):
            contrast(I)
        if E.isClicked(m):
            blur(I)


        if Qbutton.isClicked(m):
            break

    win.close()











if __name__ == "__main__":
    main()
