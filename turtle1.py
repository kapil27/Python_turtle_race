from turtle import *
from random import *
pen1 = Pen()
#pen2 = Pen()
pen1.screen.bgcolor("#4f6676")

pen1.up()


pen1.right(90)
for i in range(0,16):
    pen1.goto(-250+20*i+5,250)
    pen1.write(i)
    pen1.down()
    for j in range(8):
        pen1.forward(10)
        pen1.up()
        pen1.forward(10)
        pen1.down()
    pen1.up()
    
    #pen1.right(90)    
pen1.up()
turt = []
color = ["red","blue","green","yellow","orange"]
for i in range(5):
    turt.append(Turtle())
    turt[i].color(color[i])

for i in range(5):
    turt[i].shape("turtle")
    #turt[0].color("red")
    turt[i].up()
    turt[i].right(360)
    turt[i].goto(-280,232-i*30)
pen1.write(pen1.pos())
for i in range(150):
    for j in range(5):
        turt[j].forward(randint(0,5))
        if(turt[0].xcor()== 55 or turt[1].xcor()== 55 or turt[2].xcor()== 55 or turt[3].xcor()== 55 or turt[4].xcor()== 55 ):
            turt[j].right(360)
            turt[j].right(360)
            write("try")
            break
            
#key = keyboard.is_pressed('')
