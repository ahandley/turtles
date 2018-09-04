# Python turtle driver/demo
# Python 3.7
# Using 4 spaces for indents as per:
#   https://www.python.org/dev/peps/pep-0008/#id17

# See more instructions here: docs.python.org/3.7/library/turtle.html

from turtle import *

def star():
    print(" Making a star!")
    color("red", "yellow")
    begin_fill()
    while True:
        forward(200)
        left(170)
        if (abs(pos()) < 1):
            break
    end_fill()
    # Always call done to let the graphics window finalize itself.
    done()
    
# Function that sets the color based off a seed position in the RGB spectrum
# Each color channel evaluates a piecewise function f(seed) to find the value.
# This uses colormode(255), assuming each of r,g,b is an integer 0-255.
# (The slope for all functions below is just y=x or y=-x)
#
# Red:
# |\         /|
# |*\       /*|     # max at 0, min at 255, min at 510, max at 765
# |**\     /**|
# |***\   /***|
# 0   255 510 765
#
# Green:
#    /|\         
#   /*|*\           # min at 0, max at 255, min at 510
#  /**|**\       
# /***|***\      
# 0   255 510 765
#
# Blue:
#        /|\         
#       /*|*\       # min at 0, max at 255, min at 510
#      /**|**\       
#     /***|***\    
# 0   255 510 765
def color_mutate(seed):
    red = (255 - seed) if (seed < 256) else 0 #descending function over 0-255
    green = seed if (seed < 256) else 0 #ascending function over 0-255
    
    green += (510 - seed) if (seed >= 256 and seed < 511) else 0 #descending over 256-510
    blue = (seed - 255) if (seed >= 256 and seed < 511) else 0 #ascending over 256-510
    
    blue += (765 - seed) if (seed >= 510) else 0 #descending over 510-765
    red += (seed - 510) if (seed >= 510) else 0 #ascending over 510-765
    
    pencolor(red, green, blue)
    
def rainbow_spiral():
    print(" Making a rainbow spiral!")
    colormode(255)
    pensize(10)
    goto(0.0, 0.0)
    setheading(0)
    seed = 1
    dist = 1
    for i in range(200):
        forward(dist)
        left(25)
        color_mutate(seed)
        seed = (seed + 10) % 764
        dist += 1
    done()
    









