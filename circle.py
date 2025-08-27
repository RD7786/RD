import turtle
p = turtle.Turtle()
s = turtle.Screen()
p.width(10)
p.penup()
p.goto(-125,45)
p.pendown()
p.fillcolor("yellow")
p.begin_fill()

p.goto(125,45)

p.left(90)
p.forward(65)

for i in range(180):
    p.forward(2.1)
    p.left(1)
p.forward(65)
p.end_fill()


p.forward(125)

for i in range(180):
    p.forward(2.1)
    p.left(1)
p.forward(125)

p.width = 30
p.penup()

p.goto(-60,20)
p.pendown()
p.goto(-60,-30)

p.penup()
p.goto(60,20)
p.pendown()
p.goto(60,-30)

p.width = 8
p.penup()

p.goto(-75,-75)
p.pendown()
p.left(180)

for i in range(180):
    p.forward(1.5)
    p.left(1)

turtle.done()