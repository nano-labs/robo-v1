#include <SparkFun_TB6612.h>

#define AIN1 2
#define BIN1 8
#define AIN2 4
#define BIN2 7
#define PWMA 5
#define PWMB 6
#define STBY 9

const int offsetA = -1;
const int offsetB = -1;

Motor motor2 = Motor(AIN1, AIN2, PWMA, offsetA, STBY);
Motor motor1 = Motor(BIN1, BIN2, PWMB, offsetB, STBY);

int inByte = 0;
float speed = 100.0;
float throttle = 0.0;
float pan = 0.0;
float m1 = 0.0;
float m2 = 0.0;

void setup()
{
Serial.begin(9600);
  while (!Serial) {
  }
  establishContact();
}

void loop()
{
if (Serial.available() > 0) {
    // get incoming byte:
    inByte = Serial.read();
    if (inByte == 119) { // w
        Serial.write("w");
        throttle = 1;
//        forward(motor1, motor2, speed);
    }
    else if (inByte == 87) { // W
        Serial.write("W");
        throttle = 0;
//        brake(motor1, motor2);
    }
    else if (inByte == 97) { // a
        Serial.write("a");
        pan = -0.3;
//        left(motor1, motor2, speed);
    }
    else if (inByte == 65) { // A
        Serial.write("A");
        pan = 0;
    }
    else if (inByte == 115) { // s
        Serial.write("s");
        throttle = -1;
    }
    else if (inByte == 83) { // S
        Serial.write("S");
        throttle = 0;
    }
    else if (inByte == 100) { // d
        Serial.write("d");
        pan = 0.3;      
    }
    else if (inByte == 68) { // D
        Serial.write("D");
        pan = 0;
    }
    else if (inByte == 61) { // +=
        Serial.write("+");
        speed = speed + 10.0;
    }
    else if (inByte == 45) { // -_
        Serial.write("-");
        speed = speed - 10.0;
    };
    if (speed < 0.0) {
      speed = 0.0;
    }
    else if (speed > 220.0) {
      speed = 220.0;
    }
    if (throttle == 0.0) {
      m1 = speed * -pan * 3;
      m2 = speed * pan * 3;
    }
    else {
      m1 = speed * (throttle + (pan * throttle));
      m2 = speed * (throttle - (pan * throttle));
    }
    motor1.drive(int(m1));
    motor2.drive(int(m2));
  }
}

void establishContact() {
  while (Serial.available() <= 0) {
    delay(300);
  }
}
