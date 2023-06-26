from tkinter import*
from tkinter import messagebox


def Map2():    
    fen = Tk()
    fen.title('DBZ')
    
    fond = Canvas(fen, width = 1160, height = 700, bg = 'black')

    image = PhotoImage(file = 'Map 2.gif')
    image_fond = fond.create_image(580,350, image=image)
    
    image2 = PhotoImage(file = 'Goku2.gif')
    image_goku = fond.create_image(posx2,posy2, image=image2)

    def Clavier(event):
        global posx2,posy2
        touche = event.keysym
        if touche == 'Right':
            if posx2+30 < 1160:
                posx2 += 20
        if touche == 'Left':
            if posx2-30 > 10:
                posx2 -= 20
            if posx2-30 < 10:
                fen.destroy()
                Map1()
        if touche == 'Up':
            if posy2-20 > 100:
                posy2 -= 20
        if touche == 'Down':
            if posy2+20 < 600:
                posy2 += 20

        if touche == 'Return':
            print('x =',posx2)
            print('y =',posy2)
            print('x-40 =',posx2-40)
            print('y-54 =',posy2-54)
            print('x+40 =',posx2+40)
            print('y+54 =',posy2+54)
            
        fond.coords(image_goku,posx2,posy2)

    fond.focus_set()
    fond.bind('<Key>',Clavier)
    fond.pack()
    fen.mainloop()
