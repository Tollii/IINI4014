import math
import turtle
"""
Modular multiplication visualization

Run with python2
"""



def getPoints(intervals, radius):
    """ Returns an array with points the turtle will go towards

    Arguments:
    intervals -- number of intervals
    radius -- size of circle
    """
    points = []
    for x in range(intervals):
        points.append([math.sin(x * (2 * math.pi) / intervals) * radius, math.cos(x * (2 * math.pi) / intervals) * radius])
    return points

def multiplication(points, multiplier):
    """ Returns an array of points multiplied by the parameter 'multiplier'

    Arguments:
    points -- array of point coordinates
    multiplier -- integer of how much the points will be multiplied
    """
    sum = []
    for point in range(len(points)):
        sum.append(point * multiplier)
    return sum

def multiplicationGenerator(points, multiplier):
    """ Returns an array of points multiplied by the parameter 'multiplier'

    Arguments:
    points -- array of point coordinates
    multiplier -- integer of how much the points will be multiplied
    """
    for point in range(len(points)):
        yield point * multiplier

def draw(tl, points, multiplicatedArray):
    """ Draw lines to and from the points given

    Arguments:
    tl -- turtle, created with turtle.Turtle()
    points -- array of point coordinates
    multiplicatedArray -- array of points multiplied
    """
    tl.circle(radius)
    for point in range(0, len(points)):
        tl.penup()
        tl.goto(points[point])
        tl.pendown()
        tl.goto(points[multiplicatedArray[point] % intervals])



def drawGenerator(tl, points, sumGen):
    """ Draws lines to and from the points given

    Arguments:
    tl -- turtle, created with turtle.Turtle()
    points -- array of point coordinates
    multiplicatedGen -- generator ver. of the multiplication function

    """
    tl.circle(radius)
    for x, y in zip(points, sumGen):
        tl.penup()
        tl.goto(x)
        tl.pendown()
        tl.goto(points[y % intervals])


if __name__ == "__main__":
    """Turtle setup"""
    turtle.setup(500, 500)
    tl = turtle.Turtle()
    tl.speed(0)
    tl.penup()
    tl.goto(0, -200)
    tl.pendown()

    #Initial values
    intervals = 128
    radius = 200
    multiplier = 2
    positions = getPoints(intervals, radius)

    sum = multiplicationGenerator(positions, multiplier)
    drawGenerator(tl, positions, sum)


    turtle.done()
