#########################################################################
# Date: 2018/10/02
# file name: 2nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
        # implement the assignment code here
        while True:

            data =self.car.SEN040134_Tracking.read_digital()
            if data == [0,0,0,0,0]:
                time.sleep(1)
                afterdata =self.car.SEN040134_Tracking.read_digital()
                if afterdata == [0,0,0,0,0]:
                    self.car.drive_parking()
                    break

            if self.car.SEN040134_Tracking.is_in_line(data) == True:
                self.car.accelerator.go_forward(30)
                if self.car.SEN040134_Tracking.in_center(data) == True:
                    continue
                else:
                    if data == [0,0,1,0,0]:
                        self.car.accelerator.steering.center_alignment()
                    elif data == [1,0,0,0,0]:
                        self.car.accelerator.steering.turn_left(35)
                    elif data == [1,1,0,0,0]:
                        self.car.accelerator.steering.turn_left(30)
                    elif data == [0,1,0,0,0]:
                        self.car.accelerator.steering.turn_left(10)
                    elif data == [0,0,0,0,1]:
                        self.car.accelerator.steering.turn_right(35)
                    elif data == [0,0,0,1,1]:
                        self.car.accelerator.steering.turn_right(30)
                    elif data == [0,0,0,1,0]:
                        self.car.accelerator.steering.turn_right(10)

            time.sleep(0.5)


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()