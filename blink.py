from pyfirmata import Arduino, OUTPUT

PORT = '/dev/cu.usbmodem1421'
PIN = 13
DELAY = .5

board = Arduino(PORT)
#board.digital[PIN].mode = OUTPUT

def blink(pin):
    board.digital[pin].write(1)
    board.pass_time(DELAY)
    board.digital[pin].write(0)
    board.pass_time(DELAY)

while True:
    blink(13)
    blink(11)
    blink(9)
    blink(7)
