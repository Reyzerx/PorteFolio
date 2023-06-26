boolean varmenu = false;

int puissance = 1;
int ki = 0;

int kitap = 10;// depasse pas les 50

int viemob = 20;
int vievegeta = 100;
int viefreezer = 200;
int viefreezer2 = 200;
int viecell = 300;
int viebuu = 400;
int viebeerus = 500;

int mortvegeta = 0;
int mortfreezer = 0;
int mortcell = 0;
int mortbuu = 0;

int mob = 1;
int boss = 0;
int boss2 = 0;
int boss3 = 0;
int boss4 = 0;
int boss5 = 0;

int kaioken = 0;
int supersaiyan = 0;

PImage Fond;
PImage Saibaiman,SaibaimanR,SaibaimanB;
PImage VegetaD;
PImage GokuN,GokuK,GokuG,Gokussj,Gokussj2,Gokussj3;
PImage Guldo,Recoom,Barta,Jeece,Ginyu,Freezer;


void setup(){
  size(540,960);
  //fullScreen();
  Saibaiman = loadImage("Saibaiman.png");
  SaibaimanR = loadImage("SaibaimanR.png");
  SaibaimanB = loadImage("SaibaimanB.png");
  VegetaD = loadImage("Vegetadetecteur.png");
  GokuN = loadImage("gokuN.png");
  GokuG = loadImage("gokussG.png");
  Gokussj = loadImage("gokussj.png");
  Gokussj2 = loadImage("gokussj2.png");
  Gokussj3 = loadImage("gokussj3.png");
  Guldo = loadImage("Guldo.png");
  Recoom = loadImage("Recoom.png");
  Barta = loadImage("Barta.png");
  Jeece = loadImage("Jeece.png");
  Ginyu = loadImage("Ginyu.png");
  Freezer = loadImage("Freezer.png");
  GokuK = loadImage("GokuK.png");


  //Fond = loadImage("fondMenu2.jpg");
}
void draw(){
  if (varmenu == true){
    Menu();
  }
  if (varmenu == false){
    background(0);
  
    Transformation();
    
    CombatMob();
  
    Boss();
 

    //Bouton
    fill(175,175,175);//couleur grisé
    rect(width/10.8,height/1.2,width/1.2,height/6.4);
    rect(width/1.8,height/1.42,width/5.4,height/25.6);
    rect(width/1.3,height/1.42,width/5.4,height/25.6);
  
    //Ki et Puissance
    textSize(width/27);
    fill(255);
    text("KI :",width/10.8,height/4.04);
    text("KI :",width/11,height/4.059);
    text("KI/Tap :",width/10.8,height/1.383);
    text("KI/Tap :",width/11,height/1.385);
    text("Puissance :",width/10.8,height/6.98);
    text("Puissance :",width/11,height/7);
  
    textSize(width/21.6);
    text("TRANSFORMATION",width/3.4,height/1.08);
  
    textSize(width/27);
    text("100 KI",width/1.8,height/1.30);
    text("500 KI",width/1.3,height/1.30);
    text("+1",width/1.65,height/1.37);
    text("+5",width/1.2,height/1.37);

  
    //Text variables
    text(kitap,width/7.2,height/1.30);
    text(puissance,width/7.2,height/5.12);
    text(ki,width/7.2,height/3.34);
    
    if (mob == 5){
      fill(255,0,0);
      rect(width/1.8,height/3.5,width/3.6,height/38.4);
      fill(255);
      text(vievegeta,width/1.54,height/3.25);
    }
    if (mob == 12){
      if (viefreezer > 0){
        fill(255,255,0);
        rect(width/1.8,height/3.5,width/3.6,height/38.4);
        fill(0);
        text(viefreezer,width/1.54,height/3.25);
      }
      if (viefreezer2 > 0 && viefreezer == 0){
        fill(255,0,0);
        rect(width/1.8,height/3.5,width/3.6,height/38.4);
        fill(0);
        text(viefreezer2,width/1.54,height/3.25);
      }
    }
  }
}




void Menu(){
  background(0);
  
  fill(255);
  rect(0,height/38.8,width,height/6.4);
  image(GokuK,width/10.8,height/38.8);
  fill(0);
  text("Kaioken",width/2.4,height/19.2);
  text("-2 Ki/tap",width/2.4,height/9.6);
  text("Puissance 2",width/2.4,height/6.4);
  //cacher image avec rect tant que boss pas tuer
  
  fill(255);
  rect(0,height/4.8,width,height/6.4);
  image(Gokussj,width/10.8,height/4.8);
  fill(0);
  text("Super Saiyan",width/2.4,height/4.26);
  text("-4 Ki/tap",width/2.4,height/3.49);
  text("Puissance 4",width/2.4,height/2.95);
  
  if ( mortvegeta == 0){
    fill(255);
    rect(0,height/4.8,width,height/6.4);
  }
  
  fill(255);
  rect(0,height/2.4,width,height/6.4);
  image(Gokussj2,width/10.8,height/2.4);
  fill(0);
  text("Super Saiyan 2",width/2.4,height/2.25);
  text("-6 Ki/tap",width/2.4,height/2.02);
  text("Puissance 6",width/2.4,height/1.82);
  
  if ( mortfreezer == 0){
    fill(255);
    rect(0,height/2.4,width,height/6.4);
  }
  
  fill(255);
  rect(0,height/1.6,width,height/6.4);
  image(Gokussj3,width/10.8,height/1.6);
  fill(0);
  text("Super Saiyan 3",width/2.4,height/1.53);
  text("-8 Ki/tap",width/2.4,height/1.42);
  text("Puissance 8",width/2.4,height/1.32);
  
  if ( mortcell == 0){
    fill(255);
    rect(0,height/1.6,width,height/6.4);
  }
  
  fill(255);
  rect(0,height/1.2,width,height/6.4);
  image(GokuG,width/10.8,height/1.2);
  fill(0);
  text("Super Saiyan God",width/2.4,height/1.16);
  text("-10 Ki/tap",width/2.4,height/1.09);
  text("Puissance 10",width/2.4,height/1.03);
  
  if ( mortbuu == 0){
    fill(255);
    rect(0,height/1.2,width,height/6.4);
  }
  
  //bouton retour
  fill(200);
  rect(width/1.27,height/19.2,width/5.4,height/9.6);
  fill(0);
  text("Retour",width/1.21,height/9.2);
  
}

void Transformation(){
  //perso normal
  if (kaioken == 0 && supersaiyan == 0){
    image (GokuN,width/6,height/2);
    puissance = 1;
  }
  //perso kaioken
  if (kaioken == 1){
    image (GokuK,width/6,height/2);
    puissance = 2;
  }
  if (kaioken == 2){
    kaioken = 0;
  }
  //perso ssj
  if (supersaiyan == 1){
    image (Gokussj,width/6,height/2);
    puissance = 4;
  }
  if (supersaiyan == 2){
    supersaiyan = 0;
  }
}

void CombatMob(){
  if (1 <= mob && mob <= 4 || 6 <= mob && mob <= 11){
    fill(255,0,0);
    rect(width/1.8,height/3.5,width/3.6,height/38.4);
    fill(255);
    text(viemob,width/1.54,height/3.25);
  }
  //Saibaiman
  if (mob == 4){
    mob = 1;
  }
    
  if (mob == 1){
    image (Saibaiman,width/1.64,height/2);
  }
  if (mob == 2){
    image (SaibaimanR,width/1.64,height/2);
  }
  if (mob == 3){
    image (SaibaimanB,width/1.64,height/2);
  }
  //Commando Ginyu
  if (mob == 11){
    mob = 6;
  }
  if (mob == 6){
    image (Guldo,width/1.64,height/2);
  }
  if (mob == 7){
    image (Recoom,width/1.64,height/2);
  }
  if (mob == 8){
    image (Barta,width/1.64,height/2);
  }
  if (mob == 9){
    image (Jeece,width/1.64,height/2);
  }
  if (mob == 10){
    image (Ginyu,width/1.64,height/2);
  }
 
}

void Boss(){
  //boss Vegeta
  if (boss == 3){
    fill(175,175,175);//couleur grisé
    rect(width/1.8,height/19.2,width/2.7,height/6.4);
    textSize(width/21.6);
    fill(255);
    text("Boss",width/1.45,height/6.98);
    textSize(width/30);
    text("Requis : KaioKen",width/1.67,height/6);
   
    if (mob == 5){
      image (VegetaD,width/1.64,height/2);
    }
    if (vievegeta <= 0){
      mortvegeta = 1;
      mob = 6;
      kaioken = 0;
      vievegeta = 0;
      boss = 4;
    }
  }
  
  //Boss Freezer
  if (boss2 == 5){
    fill(175,175,175);//couleur grisé
    rect(width/1.8,height/19.2,width/2.7,height/6.4);
    textSize(width/21.6);
    fill(255);
    text("Boss",width/1.45,height/6.98);
    textSize(width/30);
    text("Requis : Super Saiyan",width/1.67,height/6);
   
    if (mob == 12){
      image (Freezer,width/1.64,height/2);
    }
    if (viefreezer2 <= 0){
      mortfreezer = 1;
      mob = 12;
      viefreezer2 = 0;
      boss2 = 11;
    }
  }
}




void mouseReleased (){
  if (varmenu == false){
    //vie mob + ki  + puissance transfo + degat etc
    if (0 < mouseX && mouseX < width && 0 < mouseY && mouseY < (height/1.50)){
      if (1 <= mob && mob <=3 || 6 <= mob && mob <= 10){
        ki+=kitap;
        viemob -= puissance;
      }
        //kaioken
        if (kaioken == 1){
          ki -= puissance;
          if (ki <= 0){
            ki = 0;
            kaioken = 0;
          }
          if (ki <= 0){
            if (vievegeta > 0){
              vievegeta = 100;
              kaioken = 0;
              ki = 0;
              mob = 1;
            }
          }
        }
        //ssj
        if (supersaiyan == 1){
          ki -= puissance;
          if (ki <= 0){
            if (viefreezer > 0 || viefreezer2 > 0){
              viefreezer = 200;
              viefreezer2 = 200;
              supersaiyan = 0;
              ki = 0;
              mob = 6;
            }
          }
        }
      
      //vie Boss
      if (mob == 5 || mob == 12){
        viemob = 20;
        if(kaioken == 1){
          vievegeta -= puissance;
        }
        if (supersaiyan == 1){
          if (viefreezer > 0){
            viefreezer -= puissance;
          }
          if (viefreezer == 0){
            viefreezer2 -= puissance;
          }
        }
      }
      //mob a tuer pour aller a boss
      if(viemob <= 0){
        mob++;
        if (boss < 3){
          boss++;
        }
        if (mortvegeta == 1){
          if (boss2 < 5){
            boss2++;
          }
        }
          viemob = 20;
      }
    }
    //bouton +1ki
    if (ki >= 100){
      if ( (width/1.8) < mouseX && mouseX < (width/1.35) && (height/1.42) < mouseY && mouseY < (height/1.35)){
        if (kitap < 50){
          ki -= 100;
          kitap++;
        }
      }
    }
    
    //bouton +5ki
    if (ki >= 500){
      if ( (width/1.27) < mouseX && mouseX < (width/1.028) && (height/1.42) < mouseY && mouseY < (height/1.35)){
        if (kitap < 50){
          ki -= 500;
          kitap += 5;
          if (kitap > 50){
            kitap = 50;
          }
        }
      }
    }
  
    //acces au boss1
    if (kaioken == 1){
      if(boss >= 3){
        if (width/1.8 < mouseX && mouseX < width/1.08 && height/19.2 < mouseY && mouseY < height/4.8){
          mob = 5;
        }
      }
    }
    //acces au boss2
    if (supersaiyan == 1){
      if(boss2 >= 5){
        if (width/1.8 < mouseX && mouseX < width/1.08 && height/19.2 < mouseY && mouseY < height/4.8){
          mob = 12;
        }
      }
    }
  }
  
    //menu transfo
    if (width/10.8 < mouseX && mouseX < width/1.08 && height/1.2 < mouseY && mouseY < height/1.01){
      if (varmenu == false){
        varmenu = true;
      }
    }
  
    //bouton retour dans transfo
    if(width/1.27 < mouseX && height/38.4 < mouseY && mouseY < height/7.68){
      if (varmenu == true){
        varmenu = false;
      }
    }
  
    //transfo kaioken
    if(0 < mouseX && mouseX < width && height/38.8 < mouseY && mouseY < height/4.8){
      if(varmenu == true){
        varmenu = false;
        kaioken += 1;
        if (supersaiyan == 1){
          supersaiyan = 0;
        }
      }
    }
    //transfo ssj
    if(0 < mouseX && mouseX < width && height/4.8 < mouseY && mouseY < height/3.84){
      if (vievegeta == 0){
        if(varmenu == true){
          varmenu = false;
          supersaiyan += 1;
            if (kaioken == 1){
            kaioken = 0;
          }
        }
      }
    }
    println(viefreezer2);
}