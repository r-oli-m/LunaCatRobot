import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
kit.servo[0].set_pulse_width_range(900, 2610)
kit.servo[0].angle =(180) 
kit.servo[1].set_pulse_width_range(900, 2610)
kit.servo[1].angle =(180) 