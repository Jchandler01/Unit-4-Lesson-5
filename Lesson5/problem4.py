from turtle import *
import random

Tahleek = Turtle()

Tahleek.color('orange')
Tahleek.pensize(4)
Tahleek.speed(4)
Tahleek.shape('turtle')

def drawHexagon(side):
	for x in range(6):
		Tahleek.forward(side)
		Tahleek.left(60)

drawHexagon(10)
drawHexagon(20)
drawHexagon(30)
drawHexagon(40)
drawHexagon(50)
drawHexagon(60)
drawHexagon(70)
drawHexagon(80)
drawHexagon(90)

mainloop()