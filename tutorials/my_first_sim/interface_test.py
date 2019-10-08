# Morse interface test

import pymorse


def print_pos(pose):
    print("I am currently at {}".format(pose))
# end print_pos


with pymorse.Morse() as simu:
    # Subscribes to updates from the Pose sensor by passing a callback
    simu.r2d2.pose.subscribe(print_pos)

    # Send a destination
    simu.r2d2.motion.publish({
        'x': 10.0,
        'y': 5.0,
        'z': 0.0,
        'tolerance': 0.5,
        'speed': 1.0
    })

    # Give some milliseconds to the simulator to execute
    simu.sleep(0.1)

    # Waits
    while simu.r2d2.motion.get_status() != "Arrived":
        simu.sleep(0.5)
    # end while

    # Print
    print("Arrived !")
# end with
