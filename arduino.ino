int lampu[] = {13, 12, 11, 10, 9}; 
int jml_lampu = 5;
int segmentPins[7] = {8,7,6,5,4,3,2}; 

int digit[6][7] = {
  {1, 1, 1, 1, 1, 1, 0},  //0
  {0, 1, 1, 0, 0, 0, 0},  //1
  {1, 1, 0, 1, 1, 0, 1},  //2
  {1, 1, 1, 1, 0, 0, 1},  //3
  {0, 1, 1, 0, 0, 1, 1},  //4
  {1, 0, 1, 1, 0, 1, 1},  //5
};



void setup() {
  for (int i = 0; i < jml_lampu; i++) {
    pinMode(lampu[i], OUTPUT);
  }

  for (int i = 0; i < 7; i++) {
    pinMode(segmentPins[i], OUTPUT);
  }

  Serial.begin(9600);
}

void tampilkan_angka(int angka) {
  for (int i = 0; i < 7; i++) {
    digitalWrite(segmentPins[i], digit[angka][i]);
  }
}

void loop() {
  if (Serial.available() > 0) {
    char data = Serial.read();

    int jumlah_jari = data - '0'; 

    if (jumlah_jari < 0 || jumlah_jari > jml_lampu) {
      jumlah_jari = 0;
    }

    for (int i = 0; i < jml_lampu; i++) {
      if (i < jumlah_jari) {
        digitalWrite(lampu[i], HIGH);
      } else {
        digitalWrite(lampu[i], LOW);
      }

    }
    tampilkan_angka(jumlah_jari);
  }
}


