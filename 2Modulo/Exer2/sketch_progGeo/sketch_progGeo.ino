int dl = 2000;
int u = 2;
int r = 2;
int n = 10;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int x=0; x < n; x++){
    int res = u * r;
    u = res;
    Serial.println(res);
    delay(dl);
  }
}
