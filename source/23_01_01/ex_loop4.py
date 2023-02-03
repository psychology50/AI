import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

screen = turtle.Screen()
screen.colormode(255)

for i in range(60):
    t.color(255 - 4*i, 4*i, 0)
    t.circle(120)
    t.right(6)

turtle.mainloop()
# turtle.bye()