
# Imports
import pymorse

# Connection
with pymorse.Morse() as simu:
    try:
        print(simu.robots)
        simu.quit()
    except pymorse.MorseServerError as mse:
        print("Problem !")
        print(mse)
    # end except
# end while