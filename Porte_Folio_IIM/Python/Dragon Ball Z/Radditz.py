#from Tkinter import*#2.7
#import tkMessageBox#2.7
from tkinter import*#3.6
from tkinter import messagebox#3.6


def Radditz():
    global posx,posy,posx2,posy2,posx3,posy3,posx4,posy4,ViesRadditz,ViesPiccolo,RechargeGrenadeLumiere,ViesRadditz2,ViesPiccolo2,RechargeGrenadeLumiere2,ViesGoku,RechargeKamehameha

    ##################
    ##################
    #Vaisseau Radditz#
    ##################
    ##################

    def Vaisseau_Radditz():

        def Passer():
            messagebox.showinfo('',"Après la victoire de Son Goku contre Piccolo, la Terre connu la paix pendant un certains temps, mais l'arrivée d'un étrange vaisseau sur Terre risque de remettre en cause cette paix")
            fen.destroy()
            Vaisseau_Radditz2()
            
        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image = PhotoImage(file = 'VaisseauRadditz.gif')
        image_fond = fond.create_image(580,350, image=image)

        Passer = Button(fen,text = 'Passer',command = Passer)
        Passer.place(x = 500,y = 800)

        fond.pack()
        fen.mainloop()

    def Vaisseau_Radditz2():

        def Passer():
            messagebox.showinfo('',"Un étrange homme sorti de ce vaisseau, il se nomme Radditz.\nCet homme vient de la planète Vegeta, les habitants de cette planète sont appelés 'Saiyans'")
            fen.destroy()
            Vaisseau_Radditz3()
                
        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image = PhotoImage(file = 'VaisseauRadditz2.gif')
        image_fond = fond.create_image(580,350, image=image)

        Passer = Button(fen,text = 'Passer',command = Passer)
        Passer.place(x = 500,y = 800)

        fond.pack()
        fen.mainloop()


    def Vaisseau_Radditz3():

        def Transition():
            messagebox.showinfo('','Pendant ce temps...')
            messagebox.showinfo('',"Pour afficher les commandes appuyez sur 'c'")

        def Passer():
            Transition()
            fen.destroy()
            Map1()
                
        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image = PhotoImage(file = 'VaisseauRadditz4.gif')
        image_fond = fond.create_image(580,350, image=image)

        image2 = PhotoImage(file = 'Radditz2.gif')
        image_radditz = fond.create_image(650,300, image=image2)

        image3 = PhotoImage(file = 'Bulledroite.gif')
        image_bulle = fond.create_image(830,220, image=image3)
        text = fond.create_text(840,210, text = "Les habitants de cette planète sont tous en\nvies ?! Mais qu'a fait Kakarotto pendant tout\nce temps !",fill = 'black')

        Passer = Button(fen,text = 'Passer',command = Passer)
        Passer.place(x = 500,y = 800)

        fond.pack()
        fen.mainloop()
    
    #########
    #########
    #Map 1###
    #########
    #########
    posx = 470
    posy = 320
    posx2 = 410
    posy2 = 320
    posx3 = 100
    posy3 = 320
    posx4 = 540
    posy4 = 320
    ViesRadditz = 50
    ViesPiccolo = 20
    RechargeGrenadeLumiere = 0
    ViesRadditz2 = 80
    ViesPiccolo2 = 20
    RechargeGrenadeLumiere2 = 0
    ViesGoku = 30
    RechargeKamehameha = 0

    def Map1():

        def Nuage():
            messagebox.showinfo('','*Je doit aller chercher Gohan chez Tortue Génial avec le Nuage Magique*')

        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image = PhotoImage(file = 'Mont Paozu.gif')
        image_fond = fond.create_image(580,350, image=image)

        image3 = PhotoImage(file = 'Nuage Magique2.gif')
        image_nuage = fond.create_image(370,580, image=image3)
        
        image2 = PhotoImage(file = 'Goku2.gif')
        image_goku = fond.create_image(posx,posy, image=image2)

        def Go():
            messagebox.showinfo('','Pendant ce temps...')
            fen.destroy()
            Map_Radditz_Piccolo()

        def Clavier(event):
            global posx,posy
            touche = event.keysym

            #Collision a droite
            if touche == 'Right':
                if posx+40 < 1170:
                    posx += 20
                if posx+40 == 1170:
                    Nuage()

            #Collision a gauche
            if touche == 'Left':
                #Maison
                if posx-40 > 610 and posy+54 <= 174:
                    posx -= 20
                #Nuage Magique
                if posx-40 > 390 and posy+54 > 574:
                    posx -= 20
                #Riviere
                if posx-40 > 270 and 174 < posy+54 <= 574:
                    posx -= 20
                #Boutton
                if posx-40 == 390 and posy+54 > 574:
                    Button(fen,text='Go !',command = Go).place(x = 350,y =567)

            #Collision en haut
            if touche == 'Up':
                #Arbre haut
                if posy-54 > 86:
                    posy -= 20
                if posx-40 >= 610 and 66 < posy-54 <= 86:
                    posy -= 20

            #Collision en bas
            if touche == 'Down':
                #Nuage Magique
                if posx-40 >= 270:
                    if posy+54 < 574:
                        posy += 20
                #Boutton
                if posy+54 == 574 and posx-40 < 390:
                    Button(fen,text='Go !',command = Go).place(x = 350,y =567)
                #Arbre bas
                if posx-40 >= 390 and posy+54 >= 574:
                    if posy+54 < 634:
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
        
    #####################
    #####################
    #Map Radditz Piccolo#
    #####################
    #####################

    def Map_Radditz_Piccolo():

        def Info_Kikoho():
            messagebox.showinfo('','Fait 1 point de degat\nKikoho est utilisable a tout les tours')

        def Info_Grenade_Lumiere():
            messagebox.showinfo('','Fait 2 points de degats\nGrenade Lumiere est utilisable 1 tour sur 2')

            
            
        def Passer():
            fond.delete(image_bulle)
            fond.delete(text)
            Dialogue1.destroy()
            image5 = PhotoImage(file = 'Bullegauche.gif')
            image_bulle2 = fond.create_image(250,400, image=image5)
            text2 = fond.create_text(240,385, text = 'Pour ça il faudra me battre !',fill = 'black')
            Dialogue2 = Button(fen,text = 'Combat',command = Combat)
            Dialogue2.place(x = 290,y = 405)
            fen.mainloop()

        def Combat():
            fen.destroy()
            Combat1()

        def Combat1():

            def Attaque():
                global ViesRadditz,ViesPiccolo,RechargeGrenadeLumiere
                ViesRadditz -= 1
                RechargeGrenadeLumiere == 0
                messagebox.showinfo('','Piccolo utilise Kikoho')
                messagebox.showinfo('','Radditz perd 1 point de vie')
                fond.delete(6,7)
                Vie_Radditz = fond.create_text(600,100,text = 'Vie Restante : 50/'+str(ViesRadditz),fill = 'black')
                messagebox.showinfo('','Radditz utilise Week-End')
                messagebox.showinfo('','Piccolo perd 15 points de vie')
                ViesPiccolo -= 15
                fond.delete(4,8)
                Vie_Piccolo = fond.create_text(260,490,text = 'Vie Restante : 20/'+str(ViesPiccolo),fill = 'black')

                if ViesPiccolo == -10:
                    messagebox.showinfo('','Piccolo est KO')
                    fen.destroy()
                    Map_Radditz_Piccolo2()

                fen.mainloop()

            def Attaque2():
                global ViesRadditz,ViesPiccolo,RechargeGrenadeLumiere
                if RechargeGrenadeLumiere == 0:
                    ViesRadditz -= 2
                    messagebox.showinfo('','Piccolo utilise Grenade Lumiere')
                    messagebox.showinfo('','Radditz perd 2 points de vie')
                    fond.delete(6,7)
                    Vie_Radditz = fond.create_text(600,100,text = 'Vie Restante : 50/'+str(ViesRadditz),fill = 'black')
                    messagebox.showinfo('','Radditz utilise Week-End')
                    messagebox.showinfo('','Piccolo perd 15 points de vie')
                    ViesPiccolo -= 15
                    fond.delete(4,8)
                    Vie_Piccolo = fond.create_text(260,490,text = 'Vie Restante : 20/'+str(ViesPiccolo),fill = 'black')
                    RechargeGrenadeLumiere += 1

                    if ViesPiccolo == -10:
                        messagebox.showinfo('','Piccolo est KO')
                        fen.destroy()
                        Map_Radditz_Piccolo2()
                else:
                    messagebox.showinfo('','Grenade Lumiere sera disponible au prochain tour')

                    fen.mainloop()
            
            fen = Tk()
            fen.title('DBZ')
            hauteur = fen.winfo_screenheight()
            largeur = fen.winfo_screenwidth() 
            fen.wm_state(newstate="zoomed")

            fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

            image = PhotoImage(file = 'Desert rocheux.gif')
            image_fond = fond.create_image(580,350, image=image)

            image4 = PhotoImage(file = 'Combat.gif')
            image_combat = fond.create_image(580,350, image=image4)
        
            image2 = PhotoImage(file = 'Piccolo2.gif')
            image_piccolo = fond.create_image(100,550, image=image2)
            Vie_Piccolo = fond.create_text(260,490, text = 'Vie Restante : 20/'+str(ViesPiccolo),fill = 'black')


            image3 = PhotoImage(file = 'Radditz2.gif')
            image_radditz = fond.create_image(1060,150, image=image3)
            Vie_Radditz = fond.create_text(600,100,text = 'Vie Restante : 50/'+str(ViesRadditz),fill = 'black')

            Kikoho1 = Button(fen,text = 'Kikoho',command = Attaque)
            Kikoho1.place(x = 400,y = 455)
            Kikohoinfo = Button(fen,text = 'Info',command = Info_Kikoho)
            Kikohoinfo.place(x = 400,y = 490)

            Grenade_Lumiere1 = Button(fen,text = 'Grenade Lumiere',command = Attaque2)
            Grenade_Lumiere1.place(x = 500,y = 455)
            Grenade_Lumiereinfo = Button(fen,text = 'Info',command = Info_Grenade_Lumiere)
            Grenade_Lumiereinfo.place(x = 500,y = 490)

            fond.pack()
            fen.mainloop()        


        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image = PhotoImage(file = 'Desert rocheux.gif')
        image_fond = fond.create_image(580,350, image=image)
        
        image2 = PhotoImage(file = 'Piccolo2.gif')
        image_piccolo = fond.create_image(400,500, image=image2)

        image3 = PhotoImage(file = 'Radditz2.gif')
        image_radditz = fond.create_image(800,500, image=image3)

        image4 = PhotoImage(file = 'Bulledroite.gif')
        image_bulle = fond.create_image(970,400, image=image4)
        text = fond.create_text(980,390, text = 'Je pensais tomber sur Kakarotto, Qui est tu ?\nDit moi ou il se cache !',fill = 'black')

        Dialogue1 = Button(fen,text = 'Passer',command = Passer)
        Dialogue1.place(x = 1030,y = 410)

        fond.pack()
        fen.mainloop()

    #####################
    ######DEUXIEME#######
    #Map Radditz Piccolo#
    #####################
    #####################

    def Map_Radditz_Piccolo2():

        def Passer():
            fen.destroy()
            Map_Tortue_Genial()

        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image = PhotoImage(file = 'Desert rocheux.gif')
        image_fond = fond.create_image(580,350, image=image)
        
        image2 = PhotoImage(file = 'Piccolo2allonger.gif')
        image_piccolo = fond.create_image(400,520, image=image2)

        image3 = PhotoImage(file = 'Radditz2.gif')
        image_radditz = fond.create_image(800,500, image=image3)

        image4 = PhotoImage(file = 'Bulledroite.gif')
        image_bulle = fond.create_image(970,400, image=image4)
        text = fond.create_text(980,390, text = 'Hum il ne valait pas grand chose..\n(Bip bip) Je détecte une puissante énergie,\nça ne peut être que lui',fill = 'black')

        Dialogue1 = Button(fen,text = 'Passer',command = Passer)
        Dialogue1.place(x = 1030,y = 410)

        fond.pack()
        fen.mainloop()

    #####################
    #####################
    #Map Tortue Genial###
    #####################
    #####################

    def Map_Tortue_Genial():

        def Passer():
            fen.destroy()
            Map_Tortue_Genial2()
            
        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image = PhotoImage(file = 'Maison Tortue Genial.gif')
        image_fond = fond.create_image(580,350, image=image)
        
        image2 = PhotoImage(file = 'Goku2.gif')
        image_goku = fond.create_image(320,600, image=image2)

        image3 = PhotoImage(file = 'Gohan enfant sage.gif')
        image_gohan = fond.create_image(580,600, image=image3)

        image4 = PhotoImage(file = 'Nuage Magique2.gif')
        image_nuage = fond.create_image(100,650, image=image4)

        image5 = PhotoImage(file = 'Bulledroite.gif')
        image_bulle = fond.create_image(750,530, image=image5)
        text = fond.create_text(750,515, text = 'Papa !',fill = 'black')

        Dialogue1 = Button(fen,text = 'Passer',command = Passer)
        Dialogue1.place(x = 820,y = 530)

        fond.pack()
        fen.mainloop()

    #####################
    ######DEUXIEME#######
    #Map Tortue Genial###
    #####################
    #####################
    def Map_Tortue_Genial2():

        def Passer():
            fond.delete(image_bulle)
            fond.delete(text)
            Dialogue1.destroy()
            image5 = PhotoImage(file = 'Bullegauche.gif')
            image_bulle2 = fond.create_image(150,530, image=image5)
            text2 = fond.create_text(145,515, text = 'Qui est-tu ? Rend moi mon fils !',fill = 'black')
            Dialogue2 = Button(fen,text = 'Passer',command = Passer2)
            Dialogue2.place(x = 200,y = 530)
            fen.mainloop()

        def Passer2():
            fen.destroy()
            Map_Tortue_Genial3()
            
            
        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image = PhotoImage(file = 'Maison Tortue Genial.gif')
        image_fond = fond.create_image(580,350, image=image)
        
        image2 = PhotoImage(file = 'Goku2.gif')
        image_goku = fond.create_image(320,600, image=image2)

        image3 = PhotoImage(file = 'Gohan enfant pleure.gif')
        image_gohan = fond.create_image(900,625, image=image3)

        image4 = PhotoImage(file = 'Nuage Magique2.gif')
        image_nuage = fond.create_image(100,650, image=image4)

        image6 = PhotoImage(file = 'Radditz2.gif')
        image_radditz = fond.create_image(850,600, image=image6)

        image5 = PhotoImage(file = 'Bulledroite.gif')
        image_bulle = fond.create_image(1020,520, image=image5)
        text = fond.create_text(1020,510, text = 'Te voilà enfin Kakarotto',fill = 'black')

        Dialogue1 = Button(fen,text = 'Passer',command = Passer)
        Dialogue1.place(x = 1090,y = 520)

        fond.pack()
        fen.mainloop()

    #####################
    ######TROISIEME######
    #Map Tortue Genial###
    #####################
    #####################
    def Map_Tortue_Genial3():

        def Passer():
            fen.destroy()
            Map1_2()
            
        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image = PhotoImage(file = 'Maison Tortue Genial.gif')
        image_fond = fond.create_image(580,350, image=image)
        
        image2 = PhotoImage(file = 'Goku2.gif')
        image_goku = fond.create_image(320,600, image=image2)

        image3 = PhotoImage(file = 'Gohan enfant pleure.gif')
        image_gohan = fond.create_image(900,625, image=image3)

        image4 = PhotoImage(file = 'Nuage Magique2.gif')
        image_nuage = fond.create_image(100,650, image=image4)

        image6 = PhotoImage(file = 'Radditz2.gif')
        image_radditz = fond.create_image(850,600, image=image6)

        image5 = PhotoImage(file = 'Bulledroite.gif')
        image_bulle = fond.create_image(1020,520, image=image5)
        text = fond.create_text(1020,505, text = "Je suis Radditz et si tu veux le revoir\nviens m'affronter !\nJe t'attendrais dans les montagnes",fill = 'black')

        Dialogue1 = Button(fen,text = 'Passer',command = Passer)
        Dialogue1.place(x = 1090,y = 530)

        fond.pack()
        fen.mainloop()

    #####################
    ######DEUXIEME#######
    ########Map1#########
    #####################
    #####################
    def Map1_2():
        global posx2,posy2,posy3

        posx2 = posx2
        posy2 = posy3

        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image = PhotoImage(file = 'Mont Paozu.gif')
        image_fond = fond.create_image(580,350, image=image)

        image3 = PhotoImage(file = 'Nuage Magique2.gif')
        image_nuage = fond.create_image(370,580, image=image3)
        
        image2 = PhotoImage(file = 'Goku2.gif')
        image_goku = fond.create_image(posx2,posy2, image=image2)

        def Clavier(event):
            global posx2,posy2
            touche = event.keysym

            #Collision a droite
            if touche == 'Right':
                if posx2+40 < 1170:
                    posx2 += 20
                if posx2+40 == 1170:
                    messagebox.showinfo('',"*Je doit demander de l'aide à Piccolo et aller retrouver Gohan*")
                    fen.destroy()
                    Map2()
            #Collision a gauche
            if touche == 'Left':
                #Maison
                if posx2-40 > 610 and posy2+54 <= 174:
                    posx2 -= 20
                #Nuage Magique
                if posx2-40 > 390 and posy2+54 > 574:
                    posx2 -= 20
                #Riviere
                if posx2-40 > 270 and 174 < posy2+54 <= 574:
                    posx2 -= 20

            #Collision en haut
            if touche == 'Up':
                #Arbre haut
                if posy2-54 > 86:
                    posy2 -= 20
                if posx2-40 >= 610 and 66 < posy2-54 <= 86:
                    posy2 -= 20

            #Collision en bas
            if touche == 'Down':
                #Nuage Magique
                if posx2-40 >= 270:
                    if posy2+54 < 574:
                        posy2 += 20
                #Arbre bas
                if posx2-40 >= 390 and posy2+54 >= 574:
                    if posy2+54 < 634:
                        posy2 += 20

            if touche == 'c':
                messagebox.showinfo('Commandes','Flèche du haut : Monter           Flèche de Gauche : Aller a Gauche\nFlèche du bas : Descendre        Flèche de droite : Aller a Droite')


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

    #########
    #########
    #Map 2###
    #########
    #########
    def Map2():
        global posx3,posy3,posy2

        posx3 = posx3
        posy3 = posy2
        
        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image = PhotoImage(file = 'Map 2.gif')
        image_fond = fond.create_image(580,350, image=image)
        
        image2 = PhotoImage(file = 'Goku2.gif')
        image_goku = fond.create_image(posx3,posy3, image=image2)

        def Clavier(event):
            global posx3,posy3
            touche = event.keysym
            if touche == 'Right':
                #Fin de Map
                if posx3+40 == 1160:
                    fen.destroy()
                    Map3()
                #Base
                if posx3+40 > 0 and posy3+54 < 554 and posy3-54 > 26:
                    posx3 += 20
                #Riviere
                if posx3+40 < 1060 and 534 < posy3+54 < 654:
                    posx3 += 20
                #Chemin Bas
                if 460 < posx3+40 < 620 and  634 < posy3+54 <= 714:
                    posx3 += 20
                #Chemin Haut
                if 480 < posx3+40 < 620 and -34 < posy3-54 < 46:
                    posx3 += 20
                
            if touche == 'Left':
                #Fin de Map
                if posx3-40 == 0:
                    fen.destroy()
                    Map1_2()
                #Base
                if posx3+40 > 0 and posy3+54 < 654 and posy3-54 > 26:
                    posx3 -= 20
                #Chemin Bas
                if 500 < posx3+40 < 620 and  634 < posy3+54 <= 714:
                    posx3 -= 20
                #Chemin Haut
                if 520 < posx3+40 < 620 and -34 < posy3-54 < 46:
                    posx3 -= 20
                    
            if touche == 'Up':
                #Arbres haut
                if posy3-54 > 46 and posx3-40 < 440:
                    posy3 -= 20
                if posy3-54 > 46 and posx3-40 >=560:
                    posy3 -= 20
                #Chemin haut
                if 0 < posy3-54 and 440 <= posx3-40 < 560:
                    posy3 -= 20
                    
            if touche == 'Down':
                #Arbre bas
                if posy3+54 < 620 and 420 > posx3-40:
                    posy3 += 20
                if posy3+54 < 620 and 1000 > posx3-40 >= 560:
                    posy3 += 20
                #Chemin bas
                if posy3+54 < 714 and 420 <= posx3-40 < 560:
                    posy3 += 20
                if posy3+54 == 714:
                    messagebox.showinfo('',"*Je sens l'energie de Piccolo vers la cascade *")
                    messagebox.showinfo('',"Info : La cascade est vers la droite")
                #Plan d'eau
                if posy3+54 < 534 and posx3-40 >= 1000:
                    posy3 += 20

            if touche == 'c':
                messagebox.showinfo('Commandes','Flèche du haut : Monter           Flèche de Gauche : Aller a Gauche\nFlèche du bas : Descendre        Flèche de droite : Aller a Droite')

            if touche == 'Return':
                print('x =',posx3)
                print('y =',posy3)
                print('x-40 =',posx3-40)
                print('y-54 =',posy3-54)
                print('x+40 =',posx3+40)
                print('y+54 =',posy3+54)
                
            fond.coords(image_goku,posx3,posy3)

        fond.focus_set()
        fond.bind('<Key>',Clavier)
        fond.pack()
        fen.mainloop()

    #########
    #########
    #Map 3###
    #########
    #########
    def Map3():

        def Passer():
            fond.delete(image_bulle)
            fond.delete(text)
            Dialogue1.destroy()
            image5 = PhotoImage(file = 'Bulledroite.gif')
            image_bulle2 = fond.create_image(770,300, image=image5)
            text2 = fond.create_text(780,280, text = "N'oublie pas que nous sommes ennemis,\nJe vais t'aider uniquement pour sauver Gohan",fill = 'black')
            Dialogue2 = Button(fen,text = 'Passer',command = Equipe)
            Dialogue2.place(x = 850,y = 300)
            fen.mainloop()

        def Equipe():
            messagebox.showinfo('',"Piccolo a rejoint l'equipe")
            fen.destroy()
            Map2_2()
            
        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image = PhotoImage(file = 'Map 3.gif')
        image_fond = fond.create_image(580,350, image=image)
        
        image2 = PhotoImage(file = 'Goku2.gif')
        image_goku = fond.create_image(400,400, image=image2)

        image3 = PhotoImage(file = 'Piccolo3.gif')
        image_piccolo = fond.create_image(600,390, image=image3)

        image4 = PhotoImage(file = 'Bullegauche.gif')
        image_bulle = fond.create_image(230,310, image=image4)
        text = fond.create_text(225,295, text = "Piccolo j'ai besoin de ton aide !\nRadditz a enlevé San Gohan",fill = 'black')
        Dialogue1 = Button(fen,text = 'Passer',command = Passer)
        Dialogue1.place(x = 290,y = 310)

        fond.pack()
        fen.mainloop()


    ##############
    ##DEUXIEME####
    ####Map 2#####
    ##############
    def Map2_2():
        
        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image = PhotoImage(file = 'Map 2.gif')
        image_fond = fond.create_image(580,350, image=image)
        
        image2 = PhotoImage(file = 'Goku2.gif')
        image_goku = fond.create_image(posx4,posy4, image=image2)

        def Clavier(event):
            global posx4,posy4
            touche = event.keysym
            if touche == 'Right':
                #Principal
                if posx4+40 < 1060 and 26 < posy4-54 < 546:
                    posx4 += 20
                #Au dessus de la riviere
                if 1060 <= posx4+40 < 1160 and 26 < posy4-54 < 446:
                    posx4 += 20
                #Arbres haut
                if 500 < posx4+40 < 620 and -24 < posy4-54 < 46:
                    posx4 += 20
                #Arbres bas
                if 50 < posx4+40 < 620 and 634 < posy4+54 <= 694:
                    posx4 += 20
                #Info
                if posx4+40 == 1160:
                    messagebox.showinfo('',"Allons chercher Gohan dans la zone montagne")
                    messagebox.showinfo('',"Info : La zone montagne se trouve en haut")
                
            if touche == 'Left':
                if posx4-40 < 1160 and 546 > posy4-54 > 26:
                    posx4 -= 20
                #Arbre gauche haut
                if  560 > posx4-40 > 440 and 46 > posy4-54 > -34:
                    posx4 -= 20
                #Arbre gauche bas
                if  560 >= posx4-40 > 420 and 606 > posy4-54 > 526:
                    posx4 -= 20
                #Info
                if posx4-40 < 10:
                    messagebox.showinfo('',"Allons chercher Gohan dans la zone montagne")
                    messagebox.showinfo('',"Info : La zone montagne se trouve en haut")
                
                    
            if touche == 'Up':
                if posy4-54 > 46 and posx4-40 < 440:
                    posy4 -= 20
                if 0 < posy4-54 and 440 <= posx4-40 < 560:
                    posy4 -= 20
                if posy4-54 > 46 and posx4-40 >=560:
                    posy4 -= 20
                if posy4-54 == -14:
                    fen.destroy()
                    Map_Radditz_Goku()
                    
            if touche == 'Down':
                #Arbre bas
                if posy4+54 < 620 and 420 > posx4-40:
                    posy4 += 20
                if posy4+54 < 620 and 1000 > posx4-40 >= 560:
                    posy4 += 20
                #Chemin bas
                if posy4+54 < 694 and 420 <= posx4-40 < 560:
                    posy4 += 20
                    
                #Plan d'eau
                if posy4+54 < 534 and posx4-40 >= 1000:
                    posy4 += 20
                #Info
                if posy4+54 == 694:
                    messagebox.showinfo('',"Allons chercher Gohan dans la zone montagne")
                    messagebox.showinfo('',"Info : La zone montagne se trouve en haut")

            if touche == 'c':
                messagebox.showinfo('Commandes','Flèche du haut : Monter           Flèche de Gauche : Aller a Gauche\nFlèche du bas : Descendre        Flèche de droite : Aller a Droite')

            if touche == 'Return':
                print('x =',posx4)
                print('y =',posy4)
                print('x-40 =',posx4-40)
                print('y-54 =',posy4-54)
                print('x+40 =',posx4+40)
                print('y+54 =',posy4+54)
                
            fond.coords(image_goku,posx4,posy4)

        fond.focus_set()
        fond.bind('<Key>',Clavier)
        fond.pack()
        fen.mainloop()


    #####################
    #####################
    ##Map Radditz Goku###
    #####################
    #####################
    def Map_Radditz_Goku():

        def Info_Kikoho():
            messagebox.showinfo('','Fait 2 point de degat\nKikoho est utilisable a tout les tours')

        def Info_Grenade_Lumiere():
            messagebox.showinfo('','Fait 5 points de degats\nGrenade Lumiere est utilisable 1 tour sur 2')

        def Combat2_1():
            fen.destroy()
            Combat2()

        def Combat2():

            def Attaque():
                global ViesRadditz2,ViesPiccolo2,RechargeGrenadeLumiere2
                ViesRadditz2 -= 2
                RechargeGrenadeLumiere2 == 0
                messagebox.showinfo('','Piccolo utilise Kikoho')
                messagebox.showinfo('','Radditz perd 2 point de vie')
                fond.delete(6,7)
                Vie_Radditz = fond.create_text(600,100,text = 'Vie Restante : 80/'+str(ViesRadditz2),fill = 'black')
                messagebox.showinfo('','Radditz utilise Week-End')
                messagebox.showinfo('','Piccolo perd 10 points de vie')
                ViesPiccolo2 -= 10
                fond.delete(4,8)
                Vie_Piccolo = fond.create_text(260,490,text = 'Vie Restante : 20/'+str(ViesPiccolo2),fill = 'black')

                if ViesPiccolo2 == 10:
                    messagebox.showinfo('Piccolo',"Goku retient le, je doit charger mon attaque c'est notre seule chance")
                    fen.destroy()
                    Map_Radditz_Goku2()

                fen.mainloop()

            def Attaque2():
                global ViesRadditz2,ViesPiccolo2,RechargeGrenadeLumiere2
                if RechargeGrenadeLumiere2 == 0:
                    ViesRadditz2 -= 5
                    messagebox.showinfo('','Piccolo utilise Grenade Lumiere')
                    messagebox.showinfo('','Radditz perd 5 points de vie')
                    fond.delete(6,7)
                    Vie_Radditz2 = fond.create_text(600,100,text = 'Vie Restante : 80/'+str(ViesRadditz2),fill = 'black')
                    messagebox.showinfo('','Radditz utilise Week-End')
                    messagebox.showinfo('','Piccolo perd 10 points de vie')
                    ViesPiccolo2 -= 10
                    fond.delete(4,8)
                    Vie_Piccolo = fond.create_text(260,490,text = 'Vie Restante : 20/'+str(ViesPiccolo2),fill = 'black')
                    RechargeGrenadeLumiere2 += 1

                    if ViesPiccolo2 == 10:
                        messagebox.showinfo('Piccolo',"Goku retient le, je doit charger mon attaque c'est notre seule chance")
                        fen.destroy()
                        Map_Radditz_Goku2()
                else:
                    messagebox.showinfo('','Grenade Lumiere sera disponible au prochain tour')

                    fen.mainloop()
            
            fen = Tk()
            fen.title('DBZ')
            hauteur = fen.winfo_screenheight()
            largeur = fen.winfo_screenwidth() 
            fen.wm_state(newstate="zoomed")

            fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

            image = PhotoImage(file = 'Desert rocheux.gif')
            image_fond = fond.create_image(580,350, image=image)

            image4 = PhotoImage(file = 'Combat.gif')
            image_combat = fond.create_image(580,350, image=image4)
        
            image2 = PhotoImage(file = 'Piccolo2.gif')
            image_piccolo = fond.create_image(100,550, image=image2)
            Vie_Piccolo = fond.create_text(260,490, text = 'Vie Restante : 20/'+str(ViesPiccolo2),fill = 'black')


            image3 = PhotoImage(file = 'Radditz2.gif')
            image_radditz = fond.create_image(1060,150, image=image3)
            Vie_Radditz = fond.create_text(600,100,text = 'Vie Restante : 80/'+str(ViesRadditz2),fill = 'black')

            Kikoho1 = Button(fen,text = 'Kikoho',command = Attaque)
            Kikoho1.place(x = 400,y = 455)
            Kikohoinfo = Button(fen,text = 'Info',command = Info_Kikoho)
            Kikohoinfo.place(x = 400,y = 490)

            Grenade_Lumiere1 = Button(fen,text = 'Grenade Lumiere',command = Attaque2)
            Grenade_Lumiere1.place(x = 500,y = 455)
            Grenade_Lumiereinfo = Button(fen,text = 'Info',command = Info_Grenade_Lumiere)
            Grenade_Lumiereinfo.place(x = 500,y = 490)

            fond.pack()
            fen.mainloop()

        def Passer():
            fen.destroy()

        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image = PhotoImage(file = 'Desert rocheux.gif')
        image_fond = fond.create_image(580,350, image=image)
        
        image2 = PhotoImage(file = 'Goku2.gif')
        image_goku = fond.create_image(400,508, image=image2)

        image5 = PhotoImage(file = 'Piccolo2.gif')
        image_piccolo = fond.create_image(300,500, image=image5)

        image3 = PhotoImage(file = 'Radditz2.gif')
        image_radditz = fond.create_image(800,500, image=image3)

        image4 = PhotoImage(file = 'Bulledroite.gif')
        image_bulle = fond.create_image(970,400, image=image4)
        text = fond.create_text(980,385, text = 'Vous voilà enfin !\nIl est temps de voir ce que vaut mon petit frère',fill = 'black')

        Dialogue1 = Button(fen,text = 'Passer',command = Combat2_1)
        Dialogue1.place(x = 1030,y = 410)

        fond.pack()
        fen.mainloop()


    #####################
    ######DEUXIEME#######
    ##Map Radditz Goku###
    #####################
    #####################
    def Map_Radditz_Goku2():

        def Objectif1():
            messagebox.showinfo('Objectif','Reduit la vie de Radditz a 40 ou moins')

        def Info_Kikoho():
            messagebox.showinfo('','Fait 4 point de degat\nKikoho est utilisable a tout les tours')

        def Info_Kamehameha():
            messagebox.showinfo('','Fait 10 points de degats\nKamehameha est utilisable 1 tour sur 2')

        def Attaque():
            global ViesRadditz2,ViesGoku,RechargeKamehameha
            ViesRadditz2 -= 4
            RechargeKamehameha = 0
            messagebox.showinfo('','Goku utilise Kikoho')
            messagebox.showinfo('','Radditz perd 4 point de vie')
            fond.delete(6,7,9,11,13,15)
            Vie_Radditz = fond.create_text(600,100,text = 'Vie Restante : 80/'+str(ViesRadditz2),fill = 'black')

            if ViesRadditz2 <= 40:
                messagebox.showinfo('Piccolo','Je suis prêt, Goku attrape le !')
                fen.destroy()
                Map_Radditz_Goku3()

            else:
                messagebox.showinfo('','Radditz utilise Week-End')
                messagebox.showinfo('','Goku perd 5 points de vie')
                ViesGoku -= 5
                fond.delete(4,8,10,12,14,16)
                Vie_Goku = fond.create_text(260,490,text = 'Vie Restante : 30/'+str(ViesGoku),fill = 'black')

            if ViesGoku == 0:
                messagebox.showinfo('',"Goku est KO")
                fen.destroy()

            fen.mainloop()

        def Attaque2():
            global ViesRadditz2,ViesGoku,RechargeKamehameha
            if RechargeKamehameha == 0:
                ViesRadditz2 -= 10
                messagebox.showinfo('','Goku utilise Kamehameha')
                messagebox.showinfo('','Radditz perd 10 points de vie')
                fond.delete(6,7,9,11,13,15)
                Vie_Radditz = fond.create_text(600,100,text = 'Vie Restante : 80/'+str(ViesRadditz2),fill = 'black')

                if ViesRadditz2 <= 40:
                    messagebox.showinfo('Piccolo','Je suis prêt, Goku attrape le !')
                    fen.destroy()
                    Map_Radditz_Goku3()

                else:
                    messagebox.showinfo('','Radditz utilise Week-End')
                    messagebox.showinfo('','Goku perd 5 points de vie')
                    ViesGoku -= 5
                    fond.delete(4,8,10,12,14,16)
                    Vie_Goku = fond.create_text(260,490,text = 'Vie Restante : 30/'+str(ViesGoku),fill = 'black')
                    RechargeKamehameha += 1

                if ViesGoku == 0:
                    messagebox.showinfo('',"Goku est KO")
                    fen.destroy()
            else:
                messagebox.showinfo('','Kamehameha sera disponible au prochain tour')

                fen.mainloop()
            
        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image = PhotoImage(file = 'Desert rocheux.gif')
        image_fond = fond.create_image(580,350, image=image)

        image4 = PhotoImage(file = 'Combat.gif')
        image_combat = fond.create_image(580,350, image=image4)
        
        image2 = PhotoImage(file = 'Goku2.gif')
        image_goku = fond.create_image(100,550, image=image2)
        Vie_Goku = fond.create_text(260,490, text = 'Vie Restante : 30/'+str(ViesGoku),fill = 'black')


        image3 = PhotoImage(file = 'Radditz2.gif')
        image_radditz = fond.create_image(1060,150, image=image3)
        Vie_Radditz = fond.create_text(600,100,text = 'Vie Restante : 80/'+str(ViesRadditz2),fill = 'black')

        Kikoho1 = Button(fen,text = 'Kikoho',command = Attaque)
        Kikoho1.place(x = 400,y = 455)
        Kikohoinfo = Button(fen,text = 'Info',command = Info_Kikoho)
        Kikohoinfo.place(x = 400,y = 490)

        Kamehameha1 = Button(fen,text = 'Kamehameha',command = Attaque2)
        Kamehameha1.place(x = 500,y = 455)
        Kamehamehainfo = Button(fen,text = 'Info',command = Info_Kamehameha)
        Kamehamehainfo.place(x = 500,y = 490)

        Objectif = Button(fen,text = 'Objectif',command = Objectif1)
        Objectif.place(x = 250,y = 580)

        fond.pack()
        fen.mainloop()

    #####################
    #####TROISIEME#######
    ##Map Radditz Goku###
    #####################
    #####################
    def Map_Radditz_Goku3():

        def Attaque():
            messagebox.showinfo('','Piccolo utilise Makankosappo')
            fen.destroy()
            Map_Radditz_Goku_Mort()
            
        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image = PhotoImage(file = 'Desert rocheux.gif')
        image_fond = fond.create_image(580,350, image=image)

        image4 = PhotoImage(file = 'Combat.gif')
        image_combat = fond.create_image(580,350, image=image4)
        
        image2 = PhotoImage(file = 'Piccolo2.gif')
        image_goku = fond.create_image(100,550, image=image2)
        Vie_Goku = fond.create_text(260,490, text = 'Vie Restante : 30/'+str(ViesGoku),fill = 'black')


        image3 = PhotoImage(file = 'Radditz2.gif')
        image_radditz = fond.create_image(1060,150, image=image3)
        Vie_Radditz = fond.create_text(600,100,text = 'Vie Restante : 80/'+str(ViesRadditz2),fill = 'black')

        Makankosapo = Button(fen,text = 'MAKANKOSAPPO !!',command = Attaque)
        Makankosapo.place(x = 400,y = 480)



        fond.pack()
        fen.mainloop()

    #####################
    #######Mort##########
    ##Map Radditz Goku###
    #####################
    #####################
    def Map_Radditz_Goku_Mort():

        def Passer():
            fen.destroy()
            Map_Radditz_Goku_Fin()
        
        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image = PhotoImage(file = 'Desert rocheux.gif')
        image_fond = fond.create_image(580,350, image=image)

        image4 = PhotoImage(file = 'Goku3.gif')
        image_Makankosappo = fond.create_image(420,500, image=image4)

        image3 = PhotoImage(file = 'Radditz2.gif')
        image_Makankosappo = fond.create_image(390,500, image=image3)
        
        image2 = PhotoImage(file = 'Makankosappotest.gif')
        image_Makankosappo = fond.create_image(185,600, image=image2)

        Passer1 = Button(fen,text = 'Passer',command = Passer)
        Passer1.place(x = 500,y = 580)

        fond.pack()
        fen.mainloop()


    #####################
    ########FIN##########
    ##Map Radditz Goku###
    #####################
    #####################
    def Map_Radditz_Goku_Fin():

        def Passer():
            messagebox.showinfo('',"L'attaque devastatrice de Piccolo est venu a bout de Radditz, mais a aussi emporter San Goku..")
            messagebox.showinfo('',"Apres son arrivé au paradis San Goku se mit en route pour s'entrainer avec le Kaïo du Nord, mais avant ça il va devoir faire face a la terrible route du Serpent")
            fen.destroy()
            Menu_Principal()


        fen = Tk()
        fen.title('DBZ')
        hauteur = fen.winfo_screenheight()
        largeur = fen.winfo_screenwidth() 
        fen.wm_state(newstate="zoomed")

        fond = Canvas(fen, width = largeur, height = hauteur, bg = 'black')

        image = PhotoImage(file = 'Desert rocheux.gif')
        image_fond = fond.create_image(580,350, image=image)
        
        image2 = PhotoImage(file = 'Goku2allonger.gif')
        image_goku = fond.create_image(880,540, image=image2)

        image5 = PhotoImage(file = 'Piccolo2.gif')
        image_piccolo = fond.create_image(300,500, image=image5)

        image3 = PhotoImage(file = 'Radditz2allonger.gif')
        image_radditz = fond.create_image(800,540, image=image3)

        image4 = PhotoImage(file = 'Bulledroite.gif')
        image_bulle = fond.create_image(970,400, image=image4)
        text = fond.create_text(980,385, text = 'Comm..ent est..ce.. possible....',fill = 'black')

        Passer1 = Button(fen,text = 'Passer',command = Passer)
        Passer1.place(x = 500,y = 580)

        fond.pack()
        fen.mainloop()
        
    Map1()
Radditz()
