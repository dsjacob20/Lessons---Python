

import turtle
 
def drawMulticolorSquare(t, sz):
    """Make turtle t draw a multi-colour square of size sz."""
    for colors in ['red','purple','hotpink','blue']:
        t.color(colors)
        t.forward(sz)
        t.left(90)
 
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("darkblue")
 
tess = turtle.Turtle()           # create tess and set some attributes
tess.pensize(3)
 
size = 20                        # size of the smallest square
for colored_squares in range(15):
    drawMulticolorSquare(tess, size)
    size = size + 10             # increase the size for next time
    tess.forward(10)             # move tess along a little
    tess.right(18)               # and give her some extra turn
 
wn.exitonclick()
