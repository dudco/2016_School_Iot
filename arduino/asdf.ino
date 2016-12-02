int old1 = 10000;
int old2 = 10000;
int old3 = 10000;
int old4 = 10000;
int old5 = 10000;

int cnt = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int val1 = analogRead(A7);
  int val2 = analogRead(A6);
  int val3 = analogRead(A5);
  int val4 = analogRead(A4);
  int val5 = analogRead(A3);
  
  if(val1 > old1 + 100 || var2 > old2 + 100 ||
     var3 > old3 + 100 || val4 > old4 + 100 ||
     var 5 > old5 + 100){
//    Serial.print(cnt);
//    Serial.print(". ");
    Serial.print(val1);
    Serial.print("  ");
    Serial.print(val2);
    Serial.print("  ");
    Serial.print(val3);
    Serial.print("  ");
    Serial.print(val4);
    Serial.print("  ");
    Serial.print(val5);
//    Serial.print("  ");
//    Serial.print("0");
//    Serial.print("  ");
//    Serial.print("0");
//    Serial.print("  ");
//    Serial.print("0");
//    Serial.print("  ");
//    Serial.print("1");
//    Serial.print("  ");
//    Serial.println("0");
//    cnt++;
  }
  old1 = val1;
  old2 = val2;
  old3 = val3;
  old4 = val4;
  old5 = val5;

//  Serial.println(old4);
  
//  Serial.println(old);
  delay(500);
}
