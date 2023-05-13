from time import sleep
from RPi import GPIO


#d0 = Button(17)
#d1 = Button(27)
#d2 = Button(22)
#d3 = Button(23)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(23, GPIO.IN)

def binaryToDecimal(binary):
    if binary == 1010:
        return 0
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    if decimal == 12:
        return "End"
    if decimal == 11:
        return "Continue"
    return decimal


while True:
    d0 = GPIO.input(17)
    d1 = GPIO.input(27)
    d2 = GPIO.input(22)
    d3 = GPIO.input(23)
    
    number = int(f"{d0}{d1}{d2}{d3}")
    number = binaryToDecimal(number)
    print(number)
    #print(f"D0 = {d0}, D1 = {d1}, D2 = {d2}, D3 = {d3}.")
    sleep(0.8)

