# Angel-Shanika Gadsden
# 23 October 2025
# P4LAB1
# Turtle is instructed to draw the roof of a house, fill it, draw its body, then make a silly little sun.

#turtle info
import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.speed(8)

#color+pen
wn.bgcolor("skyblue")
t.pensize(2)
t.pencolor("#ff0055")


#roof
t.fillcolor("pink")
t.begin_fill()

for _ in range(1):
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)

t.end_fill()

#house
t.left(30)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
  
#painfully abstract sun thats hard to look at
#just like the real one
t.pencolor("#ffee80")
t.up()
t.goto(-100,50)
t.down()

#equally painful use of a while loop
x=0
while x < 75:
  t.forward(x+1)
  t.right(4+x)
  x+=2

#end
wn.mainloop()