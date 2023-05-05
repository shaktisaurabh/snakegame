from turtle import Turtle
class score(Turtle):#Turtle class is the superclass of score class
    def __init__(self):
        super().__init__()#this will import all attributes and methods from Turtle class which is super class of score class
        self.score=0#the value of score attribute of score class is zero
        with open("D:\snakegamepythonscore.txt") as data:#this is complete filepath,relative path starts w.r.t the working directory like
            #this ./talk.ppt and . here means look into the current working directory,go inside it and search for talk.ppt or ./project/talk.ppt
            #would mean in the current directory go inside project folder and within that search for talk.ppt,now suppose our working directory is
            #project folder which is inside work folder which has 2 items report.txt and project folder and we have to get hold of report.txt then
            #to access report.txt from current working directory project folder we do ../report.txt which means from current folder(project folder),we
            #go a step back access the work-folder and from there we access report.txt,now if in a root folder we have 2 files a.txt and b.txt and you
            #are inside b.txt then to access a.txt we can either write 'a.txt, or './a.txt',to acccess root folder from a working directory we can directly do
            #/Users/Project/ads.txt
            #../ means going outside the folder one place above and then (../abc.txt) searching for abc.txt within that
            self.high_score=int(data.read())
        self.color("white")#the color is method of Turtle class in which white is passed an argument
        self.penup()#pen is up when shifting turtle to the north of y axis so that a pencil mark is not left behind
        self.goto(0,270)#now the turtle is sent to the position (0,270)
        self.hideturtle()#after all that the turtle itself is hidden
        self.update_score()#this is to display score
    def update_score(self):
        self.write(f"Score:{self.score},HighScore:{self.high_score}",align="center",font=("Courier",24,"normal"))
    def reset_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open('D:\snakegamepythonscore.txt',mode='w') as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.clear()#deletes turtle drawings or any written thing from screen
        self.update_score()
    def increment_score(self):
        # if self.score>self.high_score:
        #     self.high_score=self.score
        self.score+=1
        self.clear()#everytime the score is incremented this object is first clear and then update_score function is called here to update
        #a new score
        self.update_score()

        #f=open("demofile.txt","r")
        #print(f.readlines())
        #the readlines() method returns the list containing each line in the file as list item