/*
 * PAVLOVOMATIC
 * by Gal Weinstock, Roni Ben Ari, Ishai Shoham
 * 
 */

#include <Stepper.h>

const int STEPS_PER_REVOLUTION = 200;

Stepper bambaStepper(STEPS_PER_REVOLUTION, 8, 9, 10, 11);

void setup() {
  bambaStepper.setSpeed(60);
  Serial.begin(9600);
}

void loop() {
  Serial.println("One treat");
  bambaStepper.step(STEP_PER_REVOLUTION);
}
