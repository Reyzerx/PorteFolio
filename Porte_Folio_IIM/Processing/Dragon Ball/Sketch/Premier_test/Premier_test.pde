PImage MontPaozu;

PImage Goku_Droite;
PImage Goku_Droite1;
PImage Goku_Droite2;
PImage Goku_Gauche;
PImage Goku_Gauche1;
PImage Goku_Gauche2;

float xGoku = 350;
float yGoku = 250;

float vitesse = 5;

float d;
float g;
float h;
float b;



void setup() {
  //fullScreen();
  size(1160, 700);
  frameRate(60);
  MontPaozu = loadImage ("Mont_Paozu.gif");
  Goku_Droite = loadImage ("Goku_Droite.gif");
  Goku_Droite1 = loadImage ("Goku_Droite1.gif");
  Goku_Droite2 = loadImage ("Goku_Droite2.gif");
  Goku_Gauche = loadImage ("Goku_Gauche.gif");
  Goku_Gauche1 = loadImage ("Goku_Gauche1.gif");
  Goku_Gauche2 = loadImage ("Goku_Gauche2.gif");
}

void draw() {

  background(0);
  imageMode(CENTER);
  image(MontPaozu, width/2, height/2);

  //Image de base
  if (d == 0) {
    image(Goku_Droite, xGoku, yGoku);
  }


  /*##########################################
   ############# Pression clavier #############
   ############################################*/
  if (keyPressed == true) {

    //######## Changement d'image toute les ** sec
    if (frameCount % 15 == 0) {
      d++;
      g++;
      h++;
      b++;
    }

    if (key == 'z') {
      yGoku -= vitesse;
    } else if (key == 's') {
      yGoku += vitesse;
    }

    //Mouvement Droite
    else if (key == 'd') {
      xGoku += vitesse;
      if (d == 1) {
        image(Goku_Droite1, xGoku, yGoku);
      } else if (d == 2) {
        image(Goku_Droite2, xGoku, yGoku);
      } else {
        d = 1;
      }
    } else if (key == 'q') {
      xGoku -= vitesse;
      if (g == 1) {
        image(Goku_Gauche1, xGoku, yGoku);
      } else if (g == 2) {
        image(Goku_Gauche2, xGoku, yGoku);
      } else {
        g = 1;
      }
    }
  }

  /*##########################################
   ########### Non Pression clavier ###########
   ############################################*/

  //Si la touche est relaché affiche limage de base
  if (keyPressed == false) {
    d = 0;
    g = 0;
    h = 0;
    b = 0;
  }
  
}