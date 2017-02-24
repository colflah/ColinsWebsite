import turtle, time

wn = turtle.Screen()

alex = turtle.Turtle()

def triangle():
	alex.left(90-50.2)
	alex.forward(39.0512)
	alex.left(100.4)
	alex.forward(39.0512)


def square():
	for i in range(0,4):
		alex.forward(50)
		alex.left(90)

def sideShape():
	for i in range (1,6):
		alex.forward(50)
		alex.left(60)


def house():
	square()
	alex.forward(50)
	alex.left(90)
	alex.forward(50)
	triangle()


def pentagon():
	for i in range(1,7):
		alex.forward(50)
		alex.left(72)


def star():
	pass		


inp = raw_input("Give me a shape:")

if inp == "triangle":
	triangle()
	time.sleep(10)
if inp == "square":
	square()
	time.sleep(10)
if inp == "sideShape":
	sideShape()
	time.sleep(10)
if inp == "house":
	house()		
	time.sleep(10)						
if inp =="pentagon":
	pentagon()
	time.sleep(10)