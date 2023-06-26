class Combat{
  PImage Combat,Piccolo,Radditz,Interrogation;
  int Vie1 = 20;
  int Vie2 = 50;
  int Degat1 = 2;
  int Degat2 = 5;
  int RelanceDegat2 = 0;
  
  
  void importer(){
    Combat = loadImage ("Combat.gif");
    Piccolo = loadImage ("Piccolo2.gif");
    Radditz = loadImage ("Radditz2.gif");
    Interrogation = loadImage ("Bulle_Interrogation.gif");
  }
  
  void afficher(){
    imageMode(CENTER);
    image(Combat,width/2, height/2);
    image(Piccolo,100, 550);
    image(Radditz,1070, 150);
    image(Interrogation,310, 470);
    image(Interrogation,265, 505);
    
    textSize(15);
    fill(0);
    
    //Vies
    text(Vie1,150,470);
    text(Vie2,800,100);
    
    //Attaque
    textSize(13);
    text("Coup de Poing",200,475);
    text("Kikoho",200,510);
    //Rectangle de selection
    noFill();
    strokeWeight(3);
    rect(190,y,150,35);
    
    
    //Degat selon l'attaque choisi
    if(Attaque >= 1){
      fill(0);
      text("Piccolo utilise Coup de Poing",200,550);
    }
    if(Attaque >= 2){
      fill(0);
      text("Radditz Perd 2 Points de Vie",200,570);
    }
    if(Attaque >= 3){
      fill(0);
      text("Radditz utilise Week-End",200,590);
    }
    if(Attaque >= 4){
      fill(0);
      text("Piccolo Perd 15 Points de Vie",200,610);
    }
    
    if(Attaque <= -1){
      fill(0);
      text("Piccolo utilise Kikoho",200,550);
    }
    if(Attaque <= -2){
      fill(0);
      text("Radditz Perd 5 Points de Vie",200,570);
    }
    if(Attaque <= -3){
      fill(0);
      text("Radditz utilise Week-End",200,590);
    }
    if(Attaque <= -4){
      fill(0);
      text("Piccolo Perd 15 Points de Vie",200,610);
    }
  }
  
}