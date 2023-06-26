import static javax.swing.JOptionPane.*;

Map_2_Perso Map2 = new Map_2_Perso();
Map_3_Perso Map3 = new Map_3_Perso();


int nbMap = 0;


void setup() {
  size(1160, 700);
  frameRate(20);
  Map2.importer();
  Map3.importer();
}

void draw() {
  background(0);
  if(nbMap == 0){
    Map2.afficher();

  }
  if(nbMap == 1){
      Map3.afficher();
  }
}

void keyPressed(){
  if(nbMap == 0){
    Map2.keyPressed();
  }
  if(nbMap == 1){
    Map3.keyPressed();
  }
}
void keyReleased(){
  if(nbMap == 0){
    Map2.keyReleased();
  }
  if(nbMap == 1){
    Map3.keyReleased();
  }
}