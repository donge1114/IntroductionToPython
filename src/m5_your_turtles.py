"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Enyi Dong.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

jia = rg.SimpleTurtle('turtle')
jia.pen = rg.Pen('green', 3)
jia.speed = 12
jia.left(90)
jia.forward(50)

size = 100
for k in range (15):
    jia.draw_circle(size)
    jia.pen_up()
    jia.right(45)
    jia.forward(10)
    jia.left(45)
    jia.pen_down()
    size = size-5

yi = rg.SimpleTurtle('turtle')
yi.pen = rg.Pen('red', 5)
yi.speed = 12
yi.right(90)
yi.forward(50)

size = 150
for k in range (16):
    yi.draw_circle(size)
    yi.pen_up()
    yi.right(45)
    yi.forward(10)
    yi.left(45)
    yi.pen_down()
    size = size-10

bing = rg.SimpleTurtle('turtle')
bing.pen = rg.Pen('yellow', 5)
bing.speed = 15

size = 180
for k in range (8):
    bing.draw_circle(size)
    bing.pen_up()
    bing.right(90)
    bing.forward(10)
    bing.left(45)
    bing.pen_down()
    size = size
bing.pen = rg.Pen('blue',3)
size = 90
for k in range (8):
    bing.draw_circle(size)
    bing.pen_up()
    bing.right(90)
    bing.forward(10)
    bing.left(45)
    bing.pen_down()
    size = size

ding = rg.SimpleTurtle('turtle')
ding.pen = rg.Pen('orange', 4)
ding.speed = 15

size = 160
for k in range (14):
    ding.draw_regular_polygon(6,size)
    ding.pen_up()
    ding.right(45)
    ding.forward(10)
    ding.left(45)
    ding.pen_down()
    size = size-6

window.close_on_mouse_click()