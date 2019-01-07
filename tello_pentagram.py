from tello_controller import TelloController

tello = TelloController()
tello.connect()
tello.takeoff()
tello.up(100)

for _ in range(5):
    tello.forward(120)
    tello.spin_right(144)

tello.land()
tello.disconnect()
