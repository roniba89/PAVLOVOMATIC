/*
   PAVLOVOMATIC

   Bamba treat dispenser

*/

#include <Stepper.h>

void giveOneTreat(int bamba);

const int STEPS_PER_REVOLUTION = 64;
int treat = 0;

Stepper bambaStepper(STEPS_PER_REVOLUTION, 8, 9, 10, 11);

void setup() {
  bambaStepper.setSpeed(300);
  Serial.begin(9600);
}

void loop() {
  while (Serial.available() > 0) {
    treat = Serial.parseInt();
    if (treat == 1) {
      giveOneTreat(treat);
    }
    treat = 0;
  }
}


void giveOneTreat(int bamba) {
  if (bamba == 1) {
    Serial.println("One treat");
    for (int i = 0; i < 32; i++) {
      bambaStepper.step(STEPS_PER_REVOLUTION);
      delay(3);
    }
  }

}

