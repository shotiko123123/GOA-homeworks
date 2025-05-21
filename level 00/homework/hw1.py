from turtle import *
#draw a square
speed(30)
width(7)
color("blue")


forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)
forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color('yellow')
begin_fill()
left(90)
forward(120)   #height of door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()        
goto(200,200)
pendown()
color('red')
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#windows
begin_fill()
penup()
goto(20,160)
pendown()
left(30)
begin_fill()
forward(40)
right(270)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()


#2 window
begin_fill()
penup()
goto(140,160)
pendown()
left(90)
forward(40)
right(270)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()


exitonclick()
