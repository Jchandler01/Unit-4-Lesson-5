from turtle import *

Tahleek = Turtle()

Tahleek.color('orange')
Tahleek.pensize()
Tahleek.speed(3)
Tahleek.shape('turtle')
Tahleek.turtlesize(2,2,2)

def drawTriangle():
	for x in range(3):
		Tahleek.forward(80)
		Tahleek.left(120)

for x in range(12):
	drawTriangle()
	Tahleek.left(30)

	

mainloop()