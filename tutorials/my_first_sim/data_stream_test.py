
# Imports
import pymorse


def printer(data):
    print("Incoming data! " + str(data))
# end printer


with pymorse.Morse() as simu:
    try:    
        # Get the 'Pose' sensor datastream
        pose = simu.r2d2.pose

        # Block
        print(pose.get())

        # Asynchronous
        pose.subscribe(printer)

        # Read for 10 seconds
        simu.sleep(10)
    except pymorse.MorseServiceError as mse:
        print("Oups! An error occured!")
        print(mse)
    # end except
# end while

