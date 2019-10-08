
# Imports
import logging
import pymorse


# Logger
logger = logging.getLogger("pymorse")

# Console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)-15s %(name)s: %(levelname)s - %(message)s')
console.setFormatter(formatter)

# Add handler
logger.addHandler(console)

# Connection
with pymorse.Morse() as simu:
    try:
        print(simu.robots)
        simu.quit()
    except pymorse.MorseServerError as mse:
        print('Error !')
        print(mse)
    # end except
# end with

