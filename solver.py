import kociemba

import RPi.GPIO as GPIO
import time 

#"Down Motor."

GPIO.setmode(GPIO.BOARD)
control_pins = [7,11,13,15]

#clockwise rotation function
def clockwise():
  for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
  halfstep_seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
  ]
  for i in range(128):
    for halfstep in range(8):
      for pin in range(4):
        GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
      time.sleep(0.001)



#counterclockwise motor turn (90 degrees)
def counter():
  for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
  halfstep_seq = [
    [1,0,0,1],
    [0,0,0,1],
    [0,0,1,1],
    [0,0,1,0],
    [0,1,1,0],
    [0,1,0,0],
    [0,1,0,0],
    [1,0,0,0]
    ]
  for i in range(128):
    for halfstep in range(8):
      for pin in range(4):
        GPIO.output(control_pins[pin], (halfstep_seq)[halfstep][pin])
      time.sleep(0.001)

GPIO.cleanup()



#u = kociemba.solve('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD')

#print(u)

z = kociemba.solve('ULBUUUULDBBRDRDLDRRULRFBDLFLFURDFBDFBFFULFLBFDBRLBRDRU')
print(z)

for i in z:
    if i == 'D':
        clockwise()

