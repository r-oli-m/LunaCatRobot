# This program demonstrates the use of the PCA9685 PWM driver
# This is useful to effectively control multiple servos or motors
# In this example, there is a servo on channel 0 and channel 1
# The code also shows how you can control a motor (on channel 2)

# Libraries
import time
from adafruit_servokit import ServoKit

# Initialize ServoKit for the PWA board.
kit = ServoKit(channels=16)

# GPIO library not necessary if we only use the PWM driver
#import RPi.GPIO as GPIO

 
# GPIO Mode (BOARD / BCM)
#GPIO.setmode(GPIO.BOARD)


print("Press CTRL+C to end the program.")

# Main program 
try:#180 135
        
    noError = True
    while noError:
        
        
        
        
        

        angle = 180
        channel = 2 
        kit.servo[channel].angle = angle
        print ('angle: {0} \t channel: {1}'.format(angle,channel))
        time.sleep(1)




 
            
# Quit the program when the user presses CTRL + C
except KeyboardInterrupt:
            pass
