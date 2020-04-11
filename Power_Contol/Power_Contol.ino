
/*This code goes to the arduino connected to the relay*/
void setup() {
pinMode(13,OUTPUT);
pinMode(12,OUTPUT);
Serial.begin(9600);
}

char data;

void loop() {
  
if(Serial.available() > 0) {
		 data = Serial.read();
                 delay(10);
                          }
 if(String(data)=="s") // the input function works with a 's' but I wiol
    { 
      digitalWrite(13,LOW);
       digitalWrite(12,LOW);
       }
        else if(String(data)=="a")
        {
          digitalWrite(13,HIGH);
          digitalWrite(12,HIGH);
                  
 }

}
