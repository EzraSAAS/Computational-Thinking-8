# 1
### SETUP ###
import turtle
#

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("purple")
t.pendown()

for i in range(200):
    t.forward(20)
    t.left(20)
    t.forward (20)
    t.left(20)

# ###
# ### ENDING ###
turtle.exitonclick()