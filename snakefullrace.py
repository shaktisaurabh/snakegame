from turtle import Screen#turtle is a module of which Screen is a class
from foodpipe import foods#foods is a class existing in foodpipe module
from scorecard import score#score is a class existing in scorecard module
from snakes import creatim#creatim is a class existing in snakes module
import time
s=Screen()#s is an object of the Screen class
s.setup(width=600,height=600)#s is an object and setup is method existing within Screen class 
s.bgcolor("black")#s is an object of Screen class and bgcolor is one of its attribute
s.title("My snake game")#s is an object of Screen class and title is one of its methods 
s.tracer(0)#tracer is off,so it basically switches off user to see any changes in the turtle until the update is done after every displacement
#below,we actually get to see the actual displacement after the sleep time below

food=foods()#food is an object of foods class
scored=score()#scored is an object of score class
saanp=creatim()#saanp is an object of creatim class
s.listen()#listen method is used to listen to every click movements on the screen
s.onkey(saanp.up,"Up")#so when Up arrow gets pressed then up method of saanp object gets called
s.onkey(saanp.down,"Down")#when Down arrow is pressed then down method of saanp object gets called
s.onkey(saanp.left,"Left")#when Left arrow is pressed then left method of saanp object gets called
s.onkey(saanp.right,"Right")#when Right arrow is pressed then right method of saanp object gets called
game_is_on=True
while game_is_on:
    # s.listen()
    # s.onkey(saanp.up,"Up")
    # s.onkey(saanp.down,"Down")
    # s.onkey(saanp.left,"Left")
    # s.onkey(saanp.right,"Right")
    s.update()#this will ensure that the snake will get shown only after all the turtle objects have been displaced and the relative
    #displacements of all the blocks will not be shown
    time.sleep(0.2)#after all the relative displacement of square shaped tuples,there will be a gap of 0.5 seconds,then the movement of 
    #the entire turtle block by 20 places will be shown,this sleep is used to increase or decrease the speed of turtle object
    saanp.move()#this will call the move method of saanp class
    if saanp.head.distance(food)<15:#distance too is a method of saanp object which is of Turtle class,this actually calculate the distance between head
        #head of turtle object and the food turtle object(which is of circular shape)
        saanp.extend()#if the head turtle object hits the food then its length is to be extended
        food.refresh()#if the head turtle object hits the food then its position is to be refreshed
        scored.increment_score()#if the length turtle object hits the food turtle object then score is first refreshed and the increased
    if saanp.head.xcor()>280 or saanp.head.xcor()<-280 or saanp.head.ycor()>280 or saanp.head.ycor()<-280:#if the xcoordinate of the current
        #position of snake head is greater than 280 or less than -280,if the ycoordinate of the current position of snake head is greater than 280 or
        #less than -280 then this loop will become active
        # game_is_on=False#now the programme will come out of the while loop
        # saanp.goto(1000,1000)
        saanp.reset()
        saanp.move()
        scored.reset_score()
        # scored.match_over()#and match_over() method of scored object is called again
    for sm in saanp.segments:#this for loop is meant for finding out collision between snake head turtle object and rest of the snake body
        if sm==saanp.head:#this if clause is meant to skip head of turtle object
            pass
        elif saanp.head.distance(sm)<10:#else if the distance between snake head and any of the body of the rest of the turtle object is less 
            #than 10 then the below will happen
            # game_is_on=False#this will stop the while loop
            # scored.match_over()#this will call the match_over() method of scored object which belongs to a class which has turtle as super class
            saanp.reset()
            saanp.move()
            scored.reset_score()
s.exitonclick()#this will not exit the screen until you dont click on any screen on the keyboard
