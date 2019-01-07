from tkinter import Tk
from tello_controller import TelloController

window = Tk()
window.geometry("600x400")
window.title("Remote")

tello = TelloController()
default_speed = 50


def takeoff(event):
    tello.takeoff()
    print("takeoff")


def land(event):
    tello.land()
    print("land")


def spin_left(event):
    tello.spin_left(default_speed)
    print("spin left")


def spin_right(event):
    tello.spin_right(default_speed)
    print("spin right")


def up(event):
    tello.up(default_speed)
    print("up")


def down(event):
    tello.down(default_speed)
    print("down")


def forward(event):
    tello.forward(default_speed)
    print("forward")


def back(event):
    tello.back(default_speed)
    print("back")


def left(event):
    tello.left(default_speed)
    print("left")


def right(event):
    tello.right(default_speed)
    print("right")


def connect(event):
    tello.connect()
    print("connect")


# takeoff and land
window.bind("c", connect)
window.bind("x", takeoff)
window.bind("z", land)

# left stick
window.bind("a", spin_left)
window.bind("d", spin_right)
window.bind("w", up)
window.bind("s", down)

# right stick
window.bind("i", forward)
window.bind("k", back)
window.bind("j", left)
window.bind("l", right)

window.mainloop()
