from pyfirmata import Arduino

PORT = '/dev/cu.usbmodem30'
PIN = 13

board = Arduino(PORT)
board.digital[PIN].write(1)
board.pass_time(1)
board.digital[PIN].write(0)