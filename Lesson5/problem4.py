from turtle import *
import random

Tahleek = Turtle()

Tahleek.color('orange')
Tahleek.pensize()
Tahleek.speed(3)
Tahleek.shape('turtle')
Tahleek.turtlesize(2,2,2)

def drawHexagon():
	for x in range(6):
		Tahleek.forward(50)
		Tahleek.left(60)

for x in range(10):
	drawHexagon()
	Tahleek.forward(54)
	





	

mainloop()