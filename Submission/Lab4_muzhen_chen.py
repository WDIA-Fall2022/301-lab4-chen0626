from sense_emu import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow= (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
grey = (220, 220, 220)

def getUserchoice():
    while True:
        try:
            choice = int(input("""What do you want to display (0. to exit):
                    1. Logo
                    2. Plus sign
                    3. Equals sign
                    4. Raspberry
                    5. Heart
                    6. Elephant
                    0. Exit"""
                    ))

            if choice > 6 or choice < 0:
                print("Please enter a number between 0 to 6")
        except ValueError:
             print("Please enter an integer")
        else:
           return choice



def trinket_logo(O = nothing, Y = yellow, B = blue, G = green):
    logo = [
    O, O, O, O, O, O, O, O,
    O, Y, Y, Y, B, G, O, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    O, Y, Y, Y, B, G, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def raspi_logo(G = green, R = red, O = nothing):

    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo

def plus(W = white, O = nothing):
    logo = [
    O, O, O, O, O, O, O, O, 
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def equals(W = white, O = nothing):
    logo = [
    O, O, O, O, O, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def heart(P = pink, O = nothing):
    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def elephant (G = grey, O = nothing, W = white):
    logo = [
    O, O, G, G, O, O, O, O,
    O, G, G, G, G, G, G, O,
    G, O, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, W, W, G, G, G, G, G,
    G, O, G, G, G, G, G, G,
    G, O, G, G, O, G, G, O,
    G, O, W, G, O, W, G, O,
]
    return logo

patterns = [trinket_logo(), plus(), equals(), raspi_logo() , heart(), elephant()]

while True:
    choice = getUserchoice()
    if choice == 0:
      print("Exit")
      break
    if choice > 6 or choice < 0:
      print("Please enter a number between 0 to 6")
    else:
      s.set_pixels(patterns[choice - 1])