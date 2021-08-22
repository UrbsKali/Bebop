from pyparrot.Bebop import Bebop


class Utilities:
    def __init__(self):
        bebop = Bebop()

    def get_drone_obj(self):
        return self.bebop

    def connect(self):
        print("connecting")
        success = self.bebop.connect(10)
        print(success)


    def disconnect(self):
        print("Disconnecting")
        success = self.bebop.disconnect()
        print(success)


class Movement:
    def __init__(self):
        bebop = Utilities.get_drone_obj()

    def take(self, x=5):
        self.bebop.safe_takeoff(x)

    def land(self, x=5):
        self.bebop.safe_land(x)

    def foward(self, inclinaison=20,time=1):
        self.bebop.fly_direct(0,inclinaison,0,0,time)

    def up(self, power=5,time=1):
        self.bebop.fly_direct(0,0,0,power,time)

    def down(self, power=5, time=1):
        self.bebop.fly_direct(0,0,0,-power,time)

    def back(self, inclinaison=20,time=1):
        self.bebop.fly_direct(0,inclinaison,0,0,time)

    def r_left(self, inclinaison=10,time=1):
        self.bebop.fly_direct(0,0,inclinaison,0,time)

    def r_right(self, inclinaison=10,time=1):
        self.bebop.fly_direct(0,0,inclinaison,0,time)


    def right(self, degre=10, time=1):
        self.bebop.fly_direct(degre,0,0,0,time)

    def left(self, degre=10,time=1):
        self.bebop.fly_direct(-degre,0,0,0,time)


class LiveVideo:
    def __init__(self):
        bebop = Utilities.get_drone_obj()

    def start_gui(self):
        pass