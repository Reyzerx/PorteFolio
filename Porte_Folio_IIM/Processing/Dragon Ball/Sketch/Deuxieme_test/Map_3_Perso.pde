class Map_3_Perso {
  PImage Mapdeux;
  PImage sheet, texture;  // variables de type image

  int xGoku;
  int yGoku;
  int nbPas;
  int index;

  boolean droite, gauche, haut, bas;

  float vitesse = 10;

  void importer() {
    sheet = loadImage("Sprites_Goku_Walk_Test.png");
    Mapdeux = loadImage ("Map2.gif");

    xGoku = 60;
    yGoku = Map2.yGoku;
    nbPas = index = 0;
    droite = gauche = haut = bas = false;
  }

  void afficher() {
    imageMode(CENTER);
    image(Mapdeux, width/2, height/2);

    //A chaque frame, on incrémente le nbPas (de 0 à 29). index : de 0 à 4 (car 5 textures).
    nbPas++;
    if (nbPas == 30) nbPas = 0;
    index = nbPas % 4;

    //Si on est en mouvement : on prend la bonne ligne de texture (la colonne est index)
    if (droite || gauche || haut || bas) {
      if (droite) {
        if (xGoku < 610 && yGoku >= 80 && yGoku < 120
        || xGoku < 1170 && yGoku >= 120 && yGoku < 640
        || xGoku < 610 && yGoku >= 630 && yGoku <= 700) {
          xGoku += vitesse; //on avance de vitesse px
          texture = sheet.get(index * 60, 78, 60, 78);  //texture de la 2e ligne (donc Y=78)
        }
      }
      if (gauche) {
        if (xGoku > 520 && yGoku >= 80 && yGoku < 120
        || xGoku > 60 && yGoku >= 120 && yGoku < 640
        || xGoku > 510 && yGoku >= 630 && yGoku <= 700) {
          xGoku -= vitesse; // on recule de vitesse px
          texture = sheet.get(index * 60, 240, 60, 78);  //texture de la 2e ligne (donc Y=240)
        }
        
        //Changement de map a gauche
        else if (xGoku == 60) {
          gauche = false;
          Map2.yGoku = yGoku;
          nbMap = 0;
        }
        
      }
      if (haut) {
        if (yGoku > 120 && xGoku > 0 && xGoku <= 500 
        || yGoku > 80 && xGoku > 500 && xGoku < 620 
        || yGoku > 120 && xGoku > 620) {
          yGoku -= vitesse ;
          texture = sheet.get(index * 60, 156, 60, 78);
        }
      }
      if (bas) {
        if (yGoku < 630 && xGoku > 0 && xGoku <= 500 
        || yGoku < 700 && xGoku > 500 && xGoku < 620 
        || yGoku < 630 && xGoku > 620) {
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
  
  if(keyCode == ENTER){
    print(xGoku, yGoku);
    showMessageDialog(null, "YoupiYoupalala");
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