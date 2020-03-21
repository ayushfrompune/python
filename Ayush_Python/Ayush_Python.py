
import turtle
ayush=turtle.Pen()
ayush.shape("turtle")
ayush.color("red")
ayush.circle(100)
ayush.circle(-100)
ayush.up()
ayush.forward(200)
ayush.down()
ayush.width(5)
ayush.circle(100)
ayush.reset()


for i in range(4):
    ayush.forward(100)
    ayush.left(90)
ayush.reset()
ayush.up()
ayush.backward(300)
ayush.down()

for i in range(5):
    ayush.forward(100)
    ayush.left(144)
ayush.up()
ayush.forward(400)
ayush.down()


for i in range(30):
    ayush.forward(10*i)
    ayush.left(90)
ayush.up()
ayush.forward(-40)

