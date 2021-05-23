# axidraw_gcode_reader

This consists of 2 python scripts to help me use my AxiDraw plotter


## reader.py

This is the main script. It reads gcode and converts it to commands the AxiDraw can recognize 

It requires one argument (the gcode file you want to plot)

`python reader.py simple_test.nc`

There are several optional arguments. Unless specified they need a number after them

-scale 			: multiplier for print scale
-s or -speed 	: pen down speed
-up_speed 		: pen up speed
-conts 			: move at constant speed, is not followed by a value
-pos_down 		: pen down height (0-100)  (lower numbers = lower pen, default 45)
-c or -copies	: number of copies (horizontally)
-cs 			: copy spacing (horizontally in inches)
-d 				: pen up delay in millis (-500, 500)
-text 			: slow setting for text (overrides -s, -up_speed, -pos_down), is not followed by a value
-h or -help		: help (prints all of the arguments), is not followed by a value

By and large, these corespond exactly to values in the AxiDraw library
https://axidraw.com/doc/py_api/#options-general

For example, to draw that same file at a constant speed and with a slower speed I might use 

`python reader.py simple_test.nc -s 15 -const`

### Text

The -text flag is unusual as it just sets some good defaults for printing text, especially small text.

Obviously you can find settings that work better for you, but I found myself doing this enough that I wanted an easy way to set it.

## mover.py

The other one (mover.py) lets me move the drawing head to position it where I want before startng a drawing

**WARNING:** The AxiDraw uses dead reckoning to determine if the arm would go out of range. Moving is anythere other than the top left before plotting means you will not have this built in protection


## Trying it out

There are two exmaple files in this repo that you can try plotting:
* simple_test.nc
* text_test.nc