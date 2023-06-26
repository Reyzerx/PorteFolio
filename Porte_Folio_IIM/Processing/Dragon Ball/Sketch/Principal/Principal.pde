import static javax.swing.JOptionPane.*;
Combat Cbt = new Combat();

int y = 455;
int Attaque = 0;

void setup() {
  size(1160, 700);
  Cbt.importer();
}

void draw() {
  background(127);
  Cbt.afficher();
}

void keyPressed() {
  if (keyCode == DOWN) {
    if(Attaque == 0){
      if(y < 485){
        y += 30;
      }
    }
  }
  
  if (keyCode == UP) {
    if(Attaque == 0){
      if(y > 455){
        y -= 30;
      }
    }
  }
  
  if(key == ENTER){
    if(Cbt.Vie1 <= 0){
      showMessageDialog(null, "Piccolo est K.O");
      stop();
    }
    
    //Attaque 1
    if(y == 455){
      Attaque++; 
      
      if(Attaque == 2){
        Cbt.Vie2 -= Cbt.Degat1;
      }
      if(Attaque == 4){
        Cbt.Vie1 -= 15;      
      }
      if(Attaque == 5){
        Attaque = 0;
        Cbt.RelanceDegat2 = 0;
      }
    }
    
    //Attaque 2
    if(y == 485){
      if(Cbt.RelanceDegat2 == 0 ){
        Attaque--; 
    }else{
      showMessageDialog(null, "Disponible au prochain tour");
    }
      
      if(Attaque == -2){
        Cbt.Vie2 -= Cbt.Degat2;
      }
      if(Attaque == -4){
        Cbt.Vie1 -= 15;      
      }
      if(Attaque == -5){
        Attaque = 0;
        Cbt.RelanceDegat2 = 1;
      }
    }
  }
}

void mouseReleased(){
  if(mouseX < 320 && mouseX > 300 && mouseY < 480 && mouseY > 460){
    showMessageDialog(null, "Inflige 2 Points de Dégats");
  }
  if(mouseX < 275 && mouseX > 255 && mouseY < 515 && mouseY > 495){
    showMessageDialog(null, "Inflige 5 Points de Dégats \nUtilisable 1 tour sur 2");
  }
}