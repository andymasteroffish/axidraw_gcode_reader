# axidraw_gcode_reader

This repo consists of 2 python scripts to help me use my AxiDraw plotter with G-code files and a few demo g-code files.

I use these on a Raspberry Pi 3 that I keep next to my plotter. They have not been thoroughly tested in any other environment.


## reader.py

This is the main script. It reads g-code and converts it to commands the AxiDraw can recognize. 

It requires one argument: the g-code file you want to plot

`python reader.py simple_test.nc`

There are several optional arguments. Unless the default value is n/a they need to be followed with a numerical value

Flag 			| Default Value | Description
---- 			| ------------- | -----------
-s or -speed 	| 25			| pen down speed
-up_speed 		| 75			| pen up speed
-const 			| n/a 			| move at constant speed (by default the pen will speed up towards the maximum on long strokes)
-pos_down 		| 45			| pen down height (0-100)  (lower numbers = lower pen)
-d 				| 0 			| pen up delay in millis (-500, 500). How long to wait when raising the pen before it starts moving
-scale 			| 1				| multiplier for print scale
-c or -copies	| 1				| number of copies (horizontally)
-cs 			| 2.7 			| copy spacing (horizontally in inches)
-text 			| n/a 			| slow setting for text (overrides -s, -up_speed, -pos_down, -pen_up_delay)
-h or -help		| n/a 			| help (prints all of the arguments)

By and large, these corespond exactly to values in the AxiDraw library
https://axidraw.com/doc/py_api/#options-general

For example, to draw that same file at a constant speed and with a slower speed I might use 

`python reader.py simple_test.nc -s 15 -const`

### Text

The -text flag is unusual as it just sets some good defaults for printing text, especially small text.

Obviously you can find settings that work better for you, but I found myself doing this enough that I wanted an easy way to set it.

## mover.py

The other one (mover.py) lets me move the drawing head to position it where I want before startng a drawing.

Once you run the program, it will wait for keyboard input. Press an arrow key direction fllowed by enter to move the plotter heard. Press space followed by enter to toggle the pen up and down.

Press Q followed by enter to quit.

Be aware that when you first turn it on, you will only be able to move down and right because the AxiDraw attempts to prevent overdraws and recognizes the starting position as the top left.

**WARNING:** The AxiDraw uses dead reckoning to determine if the arm would go out of range. starting a drawing anythere other than the top left of the bed will not have this built in protection. Make sure whatever you are drawing will not take it out of range. Do not use mover.py if you're not sure.

mover.py has a few optional arguments

Flag 			| Default Value | Description
---- 			| ------------- | -----------
-d 				| 0.01			| how far to move with each keystroke (in inches)
-pos_down 		| 45			| pen down height
-h 				| n/a 			| prints help info


## Trying it out

There are two exmaple files in this repo that you can try plotting:
* simple_test.nc (roughly 1" by 5")
* text_test.nc (roughly 2.5" by 1")

## Generating G-code

I create my G-code using my openFrameworks library ofxGCode: https://github.com/andymasteroffish/ofxGCode

Feel free to use it for your own work if you dig C++!

## My Plotter Work

I use this tool for all of my plotter work. You can see what I have for sale at https://shop.andymakes.com/

## Getting in touch

If you wind up using this or modifying it to meet your needs, I'd love to hear from you! Drop me a line at andy [at] andymakes [dot] com.