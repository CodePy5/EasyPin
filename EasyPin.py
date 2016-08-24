import RPi.GPIO as GPIO
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(int(sys.argv[1]), GPIO.OUT)
if sys.argv[2] == "on":
	GPIO.output(int(sys.argv[1]), True)
elif sys.argv[2] == "off":
	GPIO.output(int(sys.argv[1]), False)
	GPIO.cleanup()
else:
	print("Invalid arg!")
