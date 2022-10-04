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

def getUserChoice():
    print("What do you want to display(0. to exit):")
    print("1. Logo")
    print("2. Plus sign")
    print("3. Equals sign")
    print("4. Raspberry")
    print("5. Heart")
    print("6. Elephant")
    print("0. Exit")

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

getUserChoice()
while True:
    try:
       i = int(input())
        if i == 1:
            s.set_pixels(trinket_logo())

        if i == 2:
            s.set_pixels(plus())

        if i == 3:
            s.set_pixels(equals())

        if i == 4:
            s.set_pixels(raspi_logo())

        if i == 5:
            s.set_pixels(heart())

        if i == 6:
            s.set_pixels(elephant())
            
        if i == 0:  
            print("Exit")
            break
        if i > 6 or i < 0:
            print("choose between 0 to 6")
    except ValueError:
        print("Must be integer, try again.")
