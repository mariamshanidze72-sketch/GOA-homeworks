from turtle import *



shape('turtle')
speed(5)
color('brown')
begin_fill()
width(5)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()


penup()
color("orange")
begin_fill()
left(90)
forward(70)
pendown()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("orange")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
width(3)
color('blue')
goto(15,150)
pendown()
begin_fill()
circle(20)
end_fill()


penup()
goto(145,150)
pendown()
begin_fill()
circle(20)
end_fill()


exitonclick()