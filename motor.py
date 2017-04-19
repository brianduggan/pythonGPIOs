import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# INSERT ACTUAL PIN NUMBERS HERE... WHITE, GREY, PURPLE, BLUE
control_pins = [25,24,23,18]

for current_pin in control_pins:
	GPIO.setup(current_pin, GPIO.OUT)
	GPIO.output(current_pin, False)

seq = [ [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1] ]
        

def motorize(rotations):
	rotations = rotations * 512
	for i in range(rotations):
		for halfstep in range(len(seq)):
			for pin in range(len(control_pins)):
				GPIO.output(control_pins[pin], seq[halfstep][pin])
				if GPIO.event_detected(control_pins[pin]):
					print(pin)
			time.sleep(0.001)

motorize(1)

GPIO.cleanup()

#
