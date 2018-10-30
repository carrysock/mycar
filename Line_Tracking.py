from SEN040134 import SEN040134_Tracking as Tracking_Sensor
import rear_wheels
import front_wheels
# import Tracking sensor module(time module included)
import time
import RPi.GPIO as GPIO

if __name__ == "__main__":
    Tracker = Tracking_Sensor.SEN040134_Tracking()
    steering = front_wheels()
    accelerator = rear_wheels()
    try:
        while True:

            data =Tracker.read_digital()
            if data == [0,0,0,0,0]:
                time.sleep(1)
                afterdata =Tracker.read_digital()
                if afterdata == [0,0,0,0,0]:
                    accelerator.stop()
                    break

            if Tracker.is_in_line(data) == True:
                accelerator.go_forward(30)
                if Tracker.in_center(data) == True:
                    continue
                else:
                    if data == [0,0,1,0,0]:
                        steering.center_alignment()
                    elif data == [1,0,0,0,0]:
                        steering.turn_left(35)
                    elif data == [1,1,0,0,0]:
                        steering.turn_left(30)
                    elif data == [0,1,0,0,0]:
                        steering.turn_left(10)
                    elif data == [0,0,0,0,1]:
                        steering.turn_right(35)
                    elif data == [0,0,0,1,1]:
                        steering.turn_right(30)
                    elif data == [0,0,0,1,0]:
                        steering.turn_right(10)

            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()