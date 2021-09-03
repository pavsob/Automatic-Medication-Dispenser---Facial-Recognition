//Servo
#include <Servo.h>
// creating servo object to control a servo
Servo upservo;
Servo downservo;
// Color value
int color = 0;
// For reading pushbutton
const int buttonPin = 2;
int buttonState = 0;
int click = 0;

//****************** Screen ******************
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
// The pins for I2C are defined by the Wire-library. 
// On an arduino UNO:       A4(SDA), A5(SCL)
#define OLED_RESET     4 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3D ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Counts of pills
int numY=0;
int numR=0;
int numG=0;
int numO=0;

// State of the machine
int state = 1;


void setup() {
  // Setups serial for communication
  Serial.begin(9600);

  // Servo pin 9 and 10
  upservo.attach(9);
  downservo.attach(10);
  downservo.write(30);
  // initialize the pushbutton pin
  pinMode(buttonPin, INPUT);

  //******** Screen Setup ********
  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
  }
  // Clear the buffer
  display.clearDisplay();
  display.display();
  delay(2000); // Pause for 2 seconds
}

void loop() {

// Display controll
  if (state == 1){
    dispHello();
  }
  else if(state == 2){
    dispCounts(numY, numR, numG, numO);
  }

  // Serial check
  serialCheck();

  // Button
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {
    click = 1;
    if (state == 1){
      state = 2;
      }
  } else {
    if (click == 1) {
      pickColor(color);
      click = 0;
      if (color == 3) {
        color = 0;
      }
      else {
        color++;
      }
    }
  }
}

// Checks for serial communication
void serialCheck() {
  if (Serial.available() > 0) {
    // Gets machine to the state 1
    state = 1;
    String inBytes = Serial.readStringUntil('\n');
    if (inBytes.charAt(0)== '*') {
      String pills = inBytes.substring(1);
      // Dysplays the machine in the state 2 where it informs the patient about what pills are dispensed
      dispCounts(numY, numR, numG, numO);
      // Restarts pill counts
      resetCounts();
      // Dispense particular pills received from python program for the given patient
      for(int i =0; i < pills.length(); i++ ) {
        char ch = pills.charAt(i);
        if(ch != ',') {
          int curr_color = ch - '0';
          pickColor(curr_color);
          dispCounts(numY, numR, numG, numO);
        }
      }
      // After dispensing it pauses for 5 seconds and then returns the machine to the state 1
      delay(5000);
      state = 1;
      // Reset pill counts
      resetCounts();
    }
    else if(inBytes.charAt(0)=='@'){
      String comeAt = inBytes.substring(1);
      comeAtTime(comeAt);
      delay(5000);
      }
  }
}

// Reset pill counts
void resetCounts(){
  numY=0;
  numR=0;
  numG=0;
  numO=0;
}

// Dispenses particular color
void pickColor(int color) {
  // picking color
  if (color == 0){
    upservo.write(45);
    numY++;
    delay(1500);
    dispense();
    delay(500);
  } else if (color == 1) {
    upservo.write(90);
    numR++;
    delay(1500);
    dispense();
    delay(500);
  } else if (color == 2) {
    upservo.write(140);
    numG++;
    delay(1500);
    dispense();
    delay(500);
  } else if (color == 3) {
    upservo.write(180);
    numO++;
    delay(1500);
    dispense();
    delay(500);
  }
}

void dispense() {
  downservo.write(70);
  delay(1000);
  downservo.write(30);
}

void dispCounts(int numY, int numR, int numG, int numO) {
    dispPills();
    dispYellow(numY);
    dispRed(numR);
    dispGreen(numG);
    dispOrange(numO);
    display.display();
}
void dispHello() {
  display.clearDisplay();
  display.setCursor(0,0); // Start at top-left corner
  display.println(F("Hello! To dispense"));
  display.println(F("your pills:"));
  display.println(F("1. Place your head in front of the camera"));
  display.println(F("2. Or press the"));
  display.println(F("button on the side"));
  display.println(F("for a test"));
  display.setTextColor(WHITE);
  display.display();
}

void comeAtTime(String AtTime) {
  display.clearDisplay();
  display.setCursor(0,0); // Start at top-left corner
  display.print(F("Come again at "));
  display.println(AtTime);
  display.setTextColor(WHITE);
  display.display();
}

void dispPills() {
  display.clearDisplay();
  display.setCursor(0,0); // Start at top-left corner
  display.println(F("Dispensed pills: "));
  display.setTextColor(WHITE);
  //display.display();
}

void dispYellow(int numY) {
  display.print(F("Yellow: "));
  display.println(numY);
  display.setTextColor(WHITE);
  //display.display();
}

void dispRed(int numR) {
  display.print(F("Red: "));
  display.println(numR);
  display.setTextColor(WHITE);
  //display.display();
}

void dispGreen(int numG) {
  display.print(F("Green: "));
  display.println(numG);
  display.setTextColor(WHITE);
  //display.display();
}

void dispOrange(int numO) {
  display.print(F("Orange: "));
  display.println(numO);
  display.setTextColor(WHITE);
  //display.display();
}
