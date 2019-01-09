from tello_api import TelloApi


class TelloController:
    """
    Abstraction of the tello udp calls into methods.
    """

    def __init__(self):
        self.tello = TelloApi()

    def connect(self):
        self.tello.do("command")

    def takeoff(self):
        self.tello.do("takeoff")

    def land(self):
        self.tello.do("land")

    def disconnect(self):
        self.tello.close_connection()

    # left stick
    def up(self, cm):
        self.tello.do(f"up {cm}")

    def down(self, cm):
        self.tello.do(f"down {cm}")

    def spin_right(self, deg):
        self.tello.do(f"cw {deg}")

    def spin_left(self, deg):
        self.tello.do(f"ccw {deg}")

    # right stick
    def forward(self, cm):
        self.tello.do(f"forward {cm}")

    def back(self, cm):
        self.tello.do(f"back {cm}")

    def left(self, cm):
        self.tello.do(f"left {cm}")

    def right(self, cm):
        self.tello.do(f"right {cm}")

    # flip
    def left_flip(self):
        self.tello.do(f"")


