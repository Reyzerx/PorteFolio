PImage sheet, texture;  // variables de type image
int x, y, nbPas, index;    // variables entières
boolean right, left, up, down; //variables booléennes
 
void setup() {
  size (800, 800); //taille de la fenêtre
  sheet = loadImage("sonicSheet.png");
  x = width/2;
  y = height/2;
  nbPas = index = 0;
  right = left = up = down = false;
}
 
void draw() {
  background(200, 160, 240); //fond d'écran
   
  //A chaque frame, on incrémente le nbPas (de 0 à 29). index : de 0 à 5 (car 6 textures).
  nbPas++;
  if (nbPas == 30) nbPas = 0;
  index = nbPas % 5;
   
  //Si on est en mouvement : on prend la bonne ligne de texture (la colonne est index)
  if (right || left || up || down) {
    if (right) {
        x = x+3; //on avance de 3 px
        texture = sheet.get(index * 50, 50, 50, 50);  //texture de la 2e ligne (donc Y=50)
      }
    if (left)  {
        x = x-3; // on recule de 3 px
        texture = sheet.get(index * 50 , 150, 50, 50);  //texture de la 2e ligne (donc Y=150)
      }
    if (up)  {
        y = y-3 ;
        texture = sheet.get(index * 50 , 0 ,  50, 50);
      }
    if (down) {
        y = y+3 ;
        texture = sheet.get(index * 50 , 100 , 50, 50);
      }
  } else {
    //Sinon on met la texture d'arrêt située en X=0 Y=200 et réinitialise nbPas et index
    nbPas = index = 0;
    texture = sheet.get(0 , 200, 50, 50);
  }
   
  image(texture, x-25, y-25); //affiche la texture L=50 H=50, qu'on recentre en (x,y)
}
 
void keyPressed() {
    if (keyCode == RIGHT) { right = true;}
    if (keyCode == LEFT ) { left = true; }
    if (keyCode == UP)    { up = true;   }
    if (keyCode == DOWN)  { down = true; }
}
 
void keyReleased() {
    if (keyCode == RIGHT) { right = false;}
    if (keyCode == LEFT ) { left = false; }
    if (keyCode == UP)    { up = false;   }
    if (keyCode == DOWN)  { down = false; }
}