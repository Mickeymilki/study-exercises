import turtle
from turtle import *

scrn = Screen()
scrn.screensize(canvwidth=500, canvheight=500,
                  bg="lightgrey")
t = turtle.Turtle()

t.width(100)
t.speed(10)

t.color('black')
t.pensize(5)

for _ in range(1):
 t.circle(-20)
 t.forward(100)
 t.circle(-20)

t.bk(20)
t.right(90)
t.forward(200)

#Колонна
t.left(180)
t.goto(80,0)
t.left(90)
t.forward(30)
t.left(90)
t.forward(200)
t.left(180)
t.goto(50,0)
t.left(90)
t.forward(30)
t.left(90)
t.forward(200)
t.right(90)
t.goto(0,-200)
t.right(180)
t.circle(20)
t.forward(100)
t.circle(20)

#Арка
t.left(180)
t.forward(120)
t.right(90)
t.forward(150)
t.circle(70,180)

#Колонна левая
t.forward(150)
t.right(90)
t.forward(20)
t.circle(-20)

t.forward(20)
t.right(90)
t.forward(200)
t.right(90)
t.forward(20)
t.circle(-20)

t.left(180)
t.forward(50)
t.left(90)
t.forward(200)
t.left(90)
t.forward(30)
t.left(180)
t.forward(60)
t.right(90)
t.forward(200)
t.right(90)
t.forward(30)
t.left(180)
t.forward(50)
t.circle(20)
t.right(180)
t.forward(20)
t.right(90)
t.forward(200)
t.right(90)
t.forward(20)
t.circle(-20)
t.forward(20)
t.left(90)

    
    

turtle.done()