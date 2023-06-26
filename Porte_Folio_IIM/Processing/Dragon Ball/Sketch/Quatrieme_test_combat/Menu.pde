class Menu {
  PImage Logo,Ombre;
  
  void importer() {
    Logo = loadImage ("Logo.gif");
    Ombre = loadImage ("Ombre_saiyan.gif");
  }
  
  void afficher() {
    imageMode(CENTER);
    image(Logo, width/2, height/1.5);
    image(Ombre, width/2, height/2.3);
  }
  
   void mouseReleased() {
    nbMap++;
  }
}