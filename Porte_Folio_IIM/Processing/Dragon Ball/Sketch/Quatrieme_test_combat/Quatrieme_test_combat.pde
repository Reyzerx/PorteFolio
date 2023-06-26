import static javax.swing.JOptionPane.*;

Map_2_Perso Map2 = new Map_2_Perso();
Map_3_Perso Map3 = new Map_3_Perso();
Map_4_CutScene Map4 = new Map_4_CutScene();
Combat Cbt = new Combat();
Menu Menu = new Menu();


int nbMap = 0;
int y = 455;
int Attaque = 0;
float vitesse = 20;


void setup() {
  size(1160, 700);
  frameRate(20);
  Map2.importer();
  Map3.importer();
  Map4.importer();
  Cbt.importer();
  Menu.importer();
}

void draw() {
  background(127);
  if(nbMap == 0){
    background(255);
    Menu.afficher();
  }
  if(nbMap == 1){
    Map2.afficher();
  }
  if(nbMap == 2){
    Map3.afficher();
  }
  if(nbMap == 3){
     Cbt.afficher();
    //Map4.afficher();
  }
}

void keyPressed(){
  if(nbMap == 1){
    Map2.keyPressed();
  }
  if(nbMap == 2){
    Map3.keyPressed();
  }
  if(nbMap == 3){
    Cbt.keyPressed();
  }
}
void keyReleased(){
  if(nbMap == 1){
    Map2.keyReleased();
  }
  if(nbMap == 2){
    Map3.keyReleased();
  }
}
void mouseReleased(){
  if(nbMap == 3){
    Cbt.mouseReleased();
  }
  if(nbMap == 0){
    Menu.mouseReleased();
  }
}