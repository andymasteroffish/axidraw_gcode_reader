import os
import sys

from pyaxidraw import axidraw

print('starting move tool. Press enter after each command')
print('Arrows - move')
print('Space - pen up/down')
print('Q - quit')

python_version = sys.version_info[0]
#print("python version: "+str(python_version))

keep_going = True
move_dist = 0.01
pen_down_height = 45
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

        if (arg == "-pos_down"):
            pen_down_height = float(val)

        if (arg == "-h"):
            print("-d : move distance")
            print("-pos_down : pen down position (lower numbers = lower pen, default 45)")
            sys.exit()


print("move dist "+str(move_dist))
print("pen down height "+str(pen_down_height))

#connect axidraw
ad = axidraw.AxiDraw()
ad.interactive()
connected = ad.connect()

if not connected:
    print("not connected")
    sys.exit()

ad.options.model=2  #AxiDraw V3/A3
ad.options.pen_pos_down = pen_down_height
ad.update() #set the options

ad.penup()


while(keep_going):
    if python_version >= 3:
        inp = input()
    else:
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

    if inp == 'h':
        ad.penup()
        ad.goto(0,0)

    #check for arrows by converting chars to int
    if ord(inp[0]) == 27:
        #up
        if ord(inp[2]) == 65:
            ad.go(0,-move_dist)

        #down
        if ord(inp[2]) == 66:\
            ad.go(0,move_dist)

        #right
        if ord(inp[2]) == 67:
            ad.go(move_dist,0)

        #left
        if ord(inp[2]) == 68:
            ad.go(-move_dist,0)

    