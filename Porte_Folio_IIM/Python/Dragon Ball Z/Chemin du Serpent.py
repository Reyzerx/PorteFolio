from tkinter import*#3.6
from tkinter import messagebox#3.6


def Chemin_Du_Serpent():
    global posx,posy
    posx = 30
    posy = 555
    posx2 = 30
    posy2 = 115


    def Map1():

        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image1 = PhotoImage(file = 'Map Route Serpent.gif')
        image_fond = fond.create_image(580,350, image=image1)

        image2 = PhotoImage(file = 'Goku2.gif')
        image_goku = fond.create_image(posx,posy, image=image2)

        def Clavier(event):
            global posx,posy
            touche = event.keysym

            #Collision a droite
            if touche == 'Right':
                if posx+40 < 10170:
                    posx += 20
                if posx+40 == 1170:
                    fen.destroy()
                    Map2()

            #Collision a gauche
            if touche == 'Left':
                if posx-40 > -100:
                    posx -= 20

            #Collision en haut
            if touche == 'Up':
                #Haut milieu
                if posy+54 > 69 and 230 < posx-40 < 670:
                    posy -= 20
                #Haut gauche
                if posy+54 > 489 and -30 < posx-40 <= 230:
                    posy -= 20
                #Haut bout droite
                if posy+54 > 489 and 670 <= posx-40 < 750:
                    posy -= 20
                #Haut droite
                if posy+54 > 69 and 750 <= posx-40 < 1110:
                    posy -= 20
                

            #Collision en bas
            if touche == 'Down':
                if posy+54 < 7000:
                    posy += 20


            if touche == 'c':
                    messagebox.showinfo('Commandes','Flèche du haut : Monter           Flèche de Gauche : Aller a Gauche\nFlèche du bas : Descendre        Flèche de droite : Aller a Droite')

                    
            if touche == 'Return':
                print('x =',posx)
                print('y =',posy)
                print('x-40 =',posx-40)
                print('y-54 =',posy-54)
                print('x+40 =',posx+40)
                print('y+54 =',posy+54)

                    
            fond.coords(image_goku,posx,posy)

        fond.focus_set()
        fond.bind('<Key>',Clavier)
        fond.pack()
        fen.mainloop()

    def Map2():

        posx2 = 30
        posy2 = posy

        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image1 = PhotoImage(file = 'Map Route Serpent2.gif')
        image_fond = fond.create_image(580,350, image=image1)

        image2 = PhotoImage(file = 'Goku2.gif')
        image_goku = fond.create_image(posx2,posy2, image=image2)

        fond.pack()
        fen.mainloop()
        
    Map1()    
Chemin_Du_Serpent()
