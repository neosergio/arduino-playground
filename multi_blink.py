from pyfirmata import Arduino

PORT = '/dev/cu.usbmodem1421'
DELAY = .5

board = Arduino(PORT)

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
