"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and John Neill.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

anatoli = rg.SimpleTurtle()
ivan = rg.SimpleTurtle()
boris = rg.SimpleTurtle()
redpen = rg.Pen('red', 5000)
yellowpen = rg.Pen('yellow', 10)

anatoli.pen = redpen
anatoli.forward(1)

ivan.pen = yellowpen
ivan.left(120)
ivan.forward(200)
ivan.right(90)
ivan.forward(60)
ivan.left(130)
ivan.forward(100)
ivan.left(50)
ivan.forward(100)
ivan.left(90)
ivan.forward(60)
ivan.left(90)
ivan.forward(40)
ivan.right(90)
ivan.forward(300)
ivan.left(90)
ivan.forward(65)
ivan.left(90)
ivan.forward(100)

boris.pen = yellowpen
boris.left(120)
boris.forward(40)
boris.right(120)

for k in range(24):
    boris.left(4.25)
    boris.forward(k)

boris.right(300)

for k in range(28):
    boris.right(4.5)
    boris.backward(k)

for k in range(23):
    boris.right(3.15)
    boris.backward(k)


boris.right(90)
boris.forward(60)
boris.right(90)
boris.forward(40)
boris.right(90)
boris.forward(120)
boris.right(120)

for k in range(19):
    boris.left(2.5)
    boris.forward(k)


for k in range(17):
    boris.left(3.6)
    boris.forward(k)


window.close_on_mouse_click()
