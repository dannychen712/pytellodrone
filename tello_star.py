from tello_controller import TelloController

tello = TelloController()
tello.connect()
tello.takeoff()

# Adjust height
while True:
    choice = input("u 20 = up 20cm\n"
                   "d 20 = down 20cm\n"
                   "y = accept:\n")

    choice_array = choice.split()

    if choice == "y":
        break
    else:
        if not len(choice_array) == 2:
            print("\n Please use the proper format\n")
            continue
        else:
            try:
                cm = int(choice_array[1])
            except ValueError:
                print("\nThe height must be a number.\n")
                continue

            if choice_array[0] == "u":
                tello.up(int(choice_array[1]))
            elif choice_array[0] == "d":
                tello.down(int(choice_array[0]))
            else:
                print("\n Please use the proper format\n")
                continue

# star size
while True:
    try:
        distance = int(input("distance of arm in cm:\n"))
        break
    except ValueError:
        print("distance must be a number\n")
        continue

# number of points
while True:
    try:
        points = int(input("number of points in the star:\n"))
        break
    except ValueError:
        print("points must be a number\n")
        continue

print(points, distance)


# distance of 180 can fit in my living room
# height of
def draw():
    for _ in range(points):
        tello.forward(distance)
        tello.spin_right(180 - (180 / points))
    tello.land()
    tello.disconnect()


draw()
