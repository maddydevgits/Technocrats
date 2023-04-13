int siren=D0;
void setup() {  pinMode(siren,OUTPUT);
  Serial.begin(9600);}
void loop() {
  while(Serial.available()){    String s=Serial.readString();
    if(s=="on") {      digitalWrite(siren,1);
    } else {      digitalWrite(siren,0);
    }  }
}
