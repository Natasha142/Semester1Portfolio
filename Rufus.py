#Elephant Line Drawing

#Initialize
import turtle
cameron = turtle.Turtle()
cameron.forward(90)
cameron.left(90)

import turtle
natasha=turtle.Turtle()
natasha.goto(0,0)
natasha.dot(50000,"#fcc0c8")

#Functions
#This code creates a colorful elephant named Rufus.

#This function draws one of the elephant's feet.
#CameronD
def drawFoot():
    cameron.penup()
    cameron.right(90)
    cameron.forward(20)
    cameron.right(90)
    cameron.forward(200)
    cameron.pendown()
    cameron.dot(140, "#b3b3cc")
    cameron.penup()
    cameron.forward(25)
    cameron.pendown()
    cameron.left(90)
    cameron.penup()
    cameron.backward(20)
    cameron.pendown()
    

#This function draws the elephant's toes on one foot.
#CameronD
def drawToes():
    for i in range(3):
        cameron.dot(30,"#ff0080")
        cameron.penup()
        cameron.forward(30)
        cameron.pendown()

#This function draws both of the elephant's feet with toenails.
#CameronD
def drawFeet():
    drawFoot()
    drawToes()
    cameron.penup()
    cameron.backward(180)
    cameron.left(90)
    cameron.forward(30)
    cameron.right(90)
    cameron.pendown()
    drawFoot()
    cameron.left(180)
    cameron.backward(50)
    cameron.left(90)
    cameron.backward(50)
    drawToes()

#This function draws the elephant's head.
#CameronD
def drawHead():
    cameron.penup()
    cameron.goto(140,0)
    cameron.pendown()
    cameron.color("#b3b3cc")
    cameron.begin_fill()
    cameron.circle(150)
    cameron.end_fill()

#This function draws the elephant's body.
#CameronD
def drawBody():
    cameron.penup()
    cameron.goto(190,-90)
    cameron.pendown()
    cameron.color("#9494b8")
    cameron.begin_fill()
    cameron.circle(200)
    cameron.end_fill()

#This function draws the elephant's right tusk: https://pythonturtle.academy/tutorial-drawing-egg-shape-with-python-turtle/
#CameronD
def drawRTusk():
    cameron.up()
    cameron.color('white')
    cameron.begin_fill()
    cameron.goto(110,-110)
    cameron.right(80)
    cameron.down()
    turtle.seth(270)
    cameron.color('white')
    cameron.circle(25,180)
    cameron.color('white')
    cameron.circle(2*25,45)
    cameron.color('white')
    cameron.circle(0.586*25,90)
    cameron.color('white')
    cameron.circle(2*25,45)
    cameron.end_fill()

#This function draws the eleaphant's left tusk.
#CameronD
def drawLTusk():
    cameron.up()
    cameron.color('white')
    cameron.begin_fill()
    cameron.goto(-80,-110)
    cameron.right(20)
    cameron.down()
    turtle.seth(270)
    cameron.color('white')
    cameron.circle(25,180)
    cameron.color('white')
    cameron.circle(2*25,45)
    cameron.color('white')
    cameron.circle(0.586*25,90)
    cameron.color('white')
    cameron.circle(2*25,45)
    cameron.end_fill()
    
#This function draws the trunk.
#NatashaF
def drawTrunk():
    natasha.penup()
    natasha.goto(-10,-100)
    natasha.pendown()
    natasha.dot(75,"#ccffff")
    natasha.penup()
    natasha.goto(-28,-100)
    natasha.pendown()
    natasha.color("#ccffff")
    natasha.width(7)
    natasha.left(90)
    natasha.forward(100)
    natasha.penup()
    natasha.goto(28,-100)
    natasha.pendown()
    natasha.forward(100)
    natasha.penup()
    natasha.goto(5,-30)
    natasha.pendown()
    natasha.left(60)
    natasha.circle(15,50)
    natasha.penup()
    natasha.goto(10,-10)
    natasha.left(-35)
    natasha.pendown()
    natasha.circle(35,40)
    natasha.penup()
    natasha.goto(20,10)
    natasha.left(-60)
    natasha.pendown()
    natasha.circle(45,60)

#This function draws the eyes.
#NatashaF
def drawEyes():
    natasha.penup()
    natasha.goto(-40,70)
    natasha.pendown()
    natasha.dot(75,"white")
    natasha.penup()
    natasha.goto(40,70)
    natasha.pendown()
    natasha.dot(75, "white")
    natasha.penup()
    natasha.goto(-35,65)
    natasha.pendown()
    natasha.dot(25,"#996600")
    natasha.penup()
    natasha.goto(35,65)
    natasha.pendown()
    natasha.dot(25,"#996600")
    
#This function draws the ears.
#NatashaF
def drawEars():
    natasha.penup()
    natasha.goto(-200,30)
    natasha.pendown()
    natasha.dot(150,"#b3d9ff")
    natasha.penup()
    natasha.goto(200,30)
    natasha.pendown()
    natasha.dot(150,"#b3d9ff")

#This function draws a star.
#NatashaF
def drawStar():
    for i in range(5):
        natasha.left(144)
        natasha.forward(20)
    
#This function draws the earrings.
#NatashaF
def drawEarrings():
    natasha.color("#ff0080")
    natasha.penup()
    natasha.goto(-250,5)
    natasha.pendown()
    drawStar()
    natasha.penup()
    natasha.goto(240,5)
    natasha.pendown()
    drawStar()
    

#This function draws the entire elephant.
#NatashaF, CameronD
def drawElephant():
    drawBody()
    drawEars()
    drawHead()
    drawEyes()
    drawTrunk()
    drawEarrings()
    drawFeet()
    drawRTusk()
    drawLTusk()


#Main

drawElephant()