class Map_2_Perso {
  PImage MontPaozu, NuageMagique, BulleAttention;
  PImage sheet, texture;  // variables de type image

  int xGoku;
  int yGoku;
  int nbPas;
  int index;

  boolean droite, gauche, haut, bas, Interact;

  void importer() {
    sheet = loadImage("Sprites_Goku_Walk_Test.png");
    MontPaozu = loadImage ("Mont_Paozu.gif");
    NuageMagique = loadImage ("Nuage_Magique2.gif");
    BulleAttention = loadImage ("Bulle_Attention.gif");

    xGoku = width/2;
    yGoku = height/2;
    nbPas = index = 0;
    droite = gauche = haut = bas = false;
  }

  void afficher() {
    imageMode(CENTER);
    image(MontPaozu, width/2, height/2);
    image(NuageMagique, 350, 570);
    

    //A chaque frame, on incrémente le nbPas (de 0 à 29). index : de 0 à 4 (car 5 textures).
    nbPas++;
    if (nbPas == 30) nbPas = 0;
    index = nbPas % 4;
    
    //Si Goku se trouve sur le nuage alors apparaitre image
    if(xGoku >= 350 && xGoku < 420 && yGoku >= 570 && yGoku < 600){
      image(BulleAttention, xGoku-30, yGoku-95);
      Interact = true;
    }

    //Si on est en mouvement : on prend la bonne ligne de texture (la colonne est index)
    if (droite || gauche || haut || bas) {
      if (droite) {
        if (xGoku < 1160) {
          xGoku += vitesse; //on avance de 3 px
          texture = sheet.get(index * 60, 78, 60, 78);  //texture de la 2e ligne (donc Y=78)
        }

        //Changement de map a droite
        else if (xGoku == 1160) {
          droite = false;
          Map3.yGoku = yGoku;
          nbMap = 2;
        }
      }
      if (gauche) {
        if (xGoku > 340 && 190 < yGoku 
          || xGoku > 680 && 110 < yGoku) {
          xGoku -= vitesse; // on recule de 3 px
          texture = sheet.get(index * 60, 240, 60, 78);  //texture de la 2e ligne (donc Y=240)
        }
      }
      if (haut) {
        if (yGoku > 200 && 340 < xGoku && xGoku <= 670 
          || yGoku > 120 && 670 < xGoku && xGoku < 1170) {
          yGoku -= vitesse ;
          texture = sheet.get(index * 60, 156, 60, 78);
        }
      }
      if (bas) {
        if (yGoku < 630) {
          yGoku += vitesse ;
          texture = sheet.get(index * 60, 0, 60, 78);
        }
      }
    } else {
      //Sinon on met la texture d'arrêt située en X=120 Y=0 et réinitialise nbPas et index
      nbPas = index = 0;
      texture = sheet.get(120, 0, 60, 78);
    }

    image(texture, xGoku-30, yGoku-39); //affiche la texture L=60 H=78, qu'on recentre en (x,y)
  }

  void keyPressed() {

    if (key == 'd') { 
      droite = true;
    }
    if (key == 'q' ) { 
      gauche = true;
    }
    if (key == 'z') { 
      haut = true;
    }
    if (key == 's') { 
      bas = true;
    }
    //Interaction touche E
    if (key == 'e') { 
      if(Interact == true){
        showMessageDialog(null, "Allons cherchez Gohan");
        nbMap = 3;
      }
    }
    //Touche d'aide A
    if (key == 'a') { 
      showMessageDialog(null,"'Z' Pour aller vers le haut\n 'Q' Pour aller vers la gauche\n 'S' Pour aller vers le bas\n 'D' Pour aller vers la droite\n\n 'E' Pour interagir ");
    }
    
    
    if (keyCode == ENTER) {
      print(xGoku, yGoku);
    }
  }

  void keyReleased() {

    if (key == 'd') { 
      droite = false;
    }
    if (key == 'q' ) { 
      gauche = false;
    }
    if (key == 'z') { 
      haut = false;
    }
    if (key == 's') { 
      bas = false;
    }
  }
}