
import turtle
ditya=turtle.Pen()
ditya.shape("turtle")
ditya.color("red")
ditya.circle(100)
ditya.circle(-100)
ditya.up()
ditya.forward(200)
ditya.down()
ditya.width(5)
ditya.circle(100)
ditya.reset()


for i in range(4):
    ditya.forward(100)
    ditya.left(90)
ditya.reset()
ditya.up()
ditya.backward(300)
ditya.down()

for i in range(5):
    ditya.forward(100)
    ditya.left(144)
ditya.up()
ditya.forward(400)
ditya.down()


for i in range(30):
    ditya.forward(10*i)
    ditya.left(90)
ditya.up()
ditya.forward(-40)

