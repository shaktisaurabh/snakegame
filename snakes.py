from turtle import Turtle
pos=[(0,0),(-20,0),(-40,0)]#the first three turtle objects(conmbination of 3 turtle objects) will be made using these 3 x,y coordinates enclosed
#in the form of tuple
class creatim:
    def __init__(self):
        self.segments=[]#the segment attribute of this class is a list which stores in all the turtle objects
        self.shamin()#the moment an object is made from this class,3 turtles will immediately be made and placed one after the other
        self.head=self.segments[0]#then head attribute of this class is initialized with 1st element of the segment 
    def shamin(self):
        for sha in pos:#this method will run through each element of pos list containing the coordinates and pass each of them to create_saap method
            self.create_saap(sha)

    def create_saap(self,pos):
        newseg=Turtle("square")#the create_saap method first creates a turtle of square shape
        newseg.penup()#this will ensure that a line doesnot get printed when the turtle slides across
        newseg.color("white")#the color of the turtle is set to white here as opposed to its black background
        newseg.goto(pos)#this is for the displacement of the newly created turtle object to a new coordinate
        self.segments.append(newseg)#now the newly created turtle is appended to segment list
    def extend(self):
        self.create_saap(self.segments[-1].position())#now when the snake is to be extended then this method would be called and the position
        #of last Turtle object in segment list is passed in create_saap method's argument which will add a new Turtle object to the segment list which when
        #displaced taking up each other's positions then it will look as if the size of the over-all turtle ha increased
    def move(self):
        for n in range(len(self.segments)-1,0,-1):#len(self.segment)-1 refers to last value of the segment list and 1st value that is to be worked upon,0 represents the last value 
            #range(start,stop,step),so here the for loop will start at start and end at stop and go further in steps
            x_range=self.segments[n-1].xcor()#first the x coordinate of the second last turtle object is pulled up and put in variable x_range
            y_range=self.segments[n-1].ycor()#y coordinate of second last turtle object is pulled up and put in variable y_range
            #this entire process is repeated until you come on segment 1
            self.segments[n].goto(x_range,y_range)#now the position x_range and y_range of segments[n-1] is passed to segments[n]
        self.head.forward(20)#after having done all this the head too is moved 20 places ahead which was not touched upon in the for loop
    def reset(self):
        # self.goto(1000,1000)
        for sjh in self.segments:
            sjh.goto(1000,1000)
        self.segments.clear()
        self.shamin()
        self.head=self.segments[0]
    def up(self):
        if self.head.heading()!=270:#heading is the angular position of turtle,if the direction of Turtle in this case is not south then the
            #direction is set to north on clicking
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!=90:#if the direction of turtle is mot north then direction is set to south
            self.head.setheading(270)
    def left(self):
        if self.head.heading()!=0:#when direction is not east then it can be set to west
            self.head.setheading(180)
    def right(self):
        if self.head.heading()!=180:#when direction is not west then it can be set to east onclick
            self.head.setheading(0)
