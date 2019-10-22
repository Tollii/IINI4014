import turtle

def dots(tl, color, windowSize):
	x = windowSize / 10
	y = 90
	tl.pencolor(color)

	for _ in range(0, 4):
		tl.dot()
		tl.forward(x)
		tl.rt(y)
	tl.forward(x * 2)
	
def square(tl, color, windowSize):
	x = windowSize / 10
	y = 90
	tl.pendown()
	tl.fillcolor(color)
	tl.begin_fill()

	for _ in range(0, 4):
		tl.forward(x)
		tl.rt(y)

	tl.forward(x)
	tl.end_fill()

def turn(tl, dir, windowSize):
	x = windowSize / 5
	y = 90
	if(dir):
		tl.rt(y)
		tl.forward(x)
		tl.rt(y)
	else:
		tl.lt(y * 2)

def drawIllusion(pencolor, fillcolor, dotcolor, windowSize):
	# Initial setup
	turtle.setup(windowSize, windowSize)
	tl = turtle.Turtle()
	tl.pencolor(pencolor)
	tl.speed(0)
	tl.penup()
	tl.goto(-windowSize/2, windowSize/2)
	tl.pensize(5)
	tl.pendown()

	# Draw all squares
	for x in range(0, 10):
		tl.pendown()

		for _ in range(0, 10):
			square(tl, fillcolor, windowSize)	

		tl.penup()
		if x % 2 == 0:
			turn(tl, True, windowSize)
		else:
			turn(tl, False, windowSize)

	# Reset turtle position
	tl.goto(-windowSize/2, windowSize/2)

	#Draw all dots
	for x in range(0, 10):
		dots(tl, dotcolor, windowSize)
		for _ in range(4):
			dots(tl, dotcolor, windowSize)

		if x % 2 == 0:
			turn(tl, True, windowSize)
		else:
			turn(tl, False, windowSize)

	dots(tl, dotcolor, windowSize)
	turtle.done()

if __name__ == "__main__":
	drawIllusion("dim gray", "yellow", "blue", 1000)