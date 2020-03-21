#this will not work with python 3

import os
import sys

from pyaxidraw import axidraw

print('starting move tool. Press enter after each command')
print('Arrows - move')
print('Space - pen up/down')
print('Q - quit')

keep_going = True
move_dist = 0.05
pen_down = False


#get arguments
if (len(sys.argv) >= 2):
    i=1
    while i < len(sys.argv):
        arg = sys.argv[i]
        
        val = sys.argv[i+1]
        i += 2
        #print("arg:",arg,"  val:",val)
        if (arg == "-d"):
            move_dist = float(val)

print("move dist "+str(move_dist))

#connect axidraw
ad = axidraw.AxiDraw()
ad.interactive()
connected = ad.connect()

if not connected:
    print("not connected")
    sys.exit()

ad.penup()


while(keep_going):
    inp = raw_input()
    
    if inp == "q":
        keep_going = False

    if inp == " ":
        print("space")
        pen_down = not pen_down
        if pen_down:
            ad.pendown()
        else:
            ad.penup()

    #check for arrows by converting chars to int
    if ord(inp[0]) == 27:
        if ord(inp[2]) == 65:
            print("up")
            ad.go(0,-move_dist)
        if ord(inp[2]) == 66:
            print("down")
            ad.go(0,move_dist)
        if ord(inp[2]) == 67:
            print("right")
            ad.go(move_dist,0)
        if ord(inp[2]) == 68:
            print("left")
            ad.go(-move_dist,0)

    