import turtle

window = turtle.Screen()
t = turtle.Turtle()


def rectangle(height, width, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for _ in [0, 1]:
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.goto(-50,-50)
rectangle(50,50,'red')
t.goto(300,300)
rectangle(50,60,'blue')


window.exitonclick()