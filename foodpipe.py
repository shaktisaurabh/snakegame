from turtle import Turtle
import random
class foods(Turtle):
    def __init__(self):
        super().__init__()#the Turtle class is superclass of foods class
        self.shape("circle")#the shape of the Turtle object is circle
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)#the shapesize of the circle is set to 0.5 width and 0.5 length
        self.color("blue")#the color of circle is blue
        self.penup()#this is to ensure that the pen is up and line doesnot get drawn when position of the circlular food object changes
        self.speed("fastest")#speed of turtle is now set to fastest
        self.refresh()#the moment the food object is created,the food object is placed at a random position on the screen
    def refresh(self):
        x_cor=random.randint(-280,280)#this will select any random integer between -280 to 280 
        y_cor=random.randint(-280,280)#this will select any random integer between -280 to 280
        self.goto(x_cor,y_cor)#and then finally the food object will be positioned at the given x and y coordinates
