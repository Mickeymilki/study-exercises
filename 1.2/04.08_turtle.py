import turtle
from turtle import *

screen = Screen()
print(screen.screensize()) 

t = turtle.Turtle()


t.width(100)
t.speed(10)

t.color('red')
t.pensize(7)

for _ in range(1):
    t.circle(-20)
    t.forward(100)
    t.circle(-20)


t.bk(20)
t.right(90)
t.forward(200)


# Колонна
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

# Плющ
t.color('green')
t.pensize(5)

t.penup()
t.goto(80,-160)
t.down()
t.left(180)
t.circle(-100,40)

for _ in range(2,5):
    t.right(140)
    t.circle(100,40)
    t.left(140)
    t.circle(-100,40)

turtle.done()