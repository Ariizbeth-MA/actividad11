"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
import turtle
import math 

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""   #Se dibujo el circulo 
    up()
    goto (start.x, start.y)
    down ()
    begin_fill()
    r =math.sqrt((abs((int(end.x-start.x)))^2)+abs ((int((end.y - start.y)))^2))
    turtle.circle(r*2)   # con ayuda de la función de python math se dibujo el circulo 
    end_fill()    


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y) #Inicia el rectangulo
    down()
    begin_fill()

    for i in range(2):
        forward(end.x - start.x) #Controla la base del rectangulo
        right(90)
        forward(2*end.x -start.x) #Altura del rectangulo
        right(90)

    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for i in range (2):
        forward(end.x - start.x) #Genera dos lados
        right(120)
    fd(end.x - start.x) #Ultimo lado del triangulo
    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple'),'P')   #Se agrego un color
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
