from pyfirmata import Arduino, OUTPUT

PORT = '/dev/cu.usbmodem1421'
PIN = 13
DELAY = .5

board = Arduino(PORT)
board.digital[PIN].mode = OUTPUT


while True:
    board.digital[PIN].write(1)
    board.pass_time(DELAY)
    board.digital[PIN].write(0)
    board.pass_time(DELAY)
