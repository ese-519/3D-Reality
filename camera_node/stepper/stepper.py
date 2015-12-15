import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
enable_pin2 = 27
enable_pin = 18
coil_A_1_pin = 4
coil_A_2_pin = 17
coil_B_1_pin = 23
coil_B_2_pin = 24

GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(enable_pin2, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

GPIO.output(enable_pin, 1)
GPIO.output(enable_pin2, 1)

def forward(delay,steps):
  GPIO.output(enable_pin,1)
  GPIO.output(enable_pin2,1)
  for i in range(0, steps):
    setStep(1, 0, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    setStep(1, 0, 0, 1)
    time.sleep(delay)
    setStep(0, 0, 0, 0)
    GPIO.output(enable_pin,0)
    GPIO.output(enable_pin2,0)
   

def backwards(delay, steps):
  GPIO.output(enable_pin,1)
  GPIO.output(enable_pin2,1)  
  for i in range(0, steps):
    setStep(1, 0, 0, 1)
    time.sleep(delay)
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(1, 0, 1, 0)
    time.sleep(delay)

  
def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)

while True:
  delay = raw_input("Delay between steps (milliseconds)?")
  if delay =='c':
    GPIO.output(enable_pin,0)
    GPIO.output(enable_pin2,0)
    setStep(0,0,0,0)
    sys.exit()
#  steps = raw_input("How many steps forward? ")
#  if steps =='c':
#    GPIO.output(enable_pin,0)
#    GPIO.output(enable_pin2,0)
#    setStep(0,0,0,0)
#    sys.exit()
#  forward(int(delay) / 1000.0, int(steps))
#  setStep(0, 0, 0, 0)
#  GPIO.output(enable_pin,0)
#  GPIO.output(enable_pin2,0)

  steps = raw_input("How many steps backwards? ")
  if steps == 'c':
    GPIO.output(enable_pin,0)
    GPIO.output(enable_pin2,0)
    setStep(0,0,0,0)
    sys.exit()
  backwards(int(delay) / 1000.0, int(steps))
  setStep(0, 0, 0, 0)
  GPIO.output(enable_pin,0)
  GPIO.output(enable_pin2,0)

