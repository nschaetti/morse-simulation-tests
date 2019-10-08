
# Imports
import pymorse


# Destination reached
def done(evt):
    print("We have reached our destination")
# end done


with pymorse.Morse() as simu:
    # Start the motion. It may take several seconds before finishing
    # The line below is however non-blocking.
    goto_action = simu.r2d2.motion.goto(2.5, 0, 0)

    # Register a callback to know when the action is done
    goto_action.add_done_callback(done)

    # Currently moving
    print("Am I currently moving ? ".format(goto_action.running()))

    # While running
    while goto_action.running():
        simu.sleep(0.5)
    # end while
# end with
