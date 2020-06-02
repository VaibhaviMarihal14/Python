import turtle
import random
import time
import winsound

delay = 0.1

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

segments= []



head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"


food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("black")
food.penup()
head.goto(1,100)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align="center",font=("courier", 24 ,"normal"))

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up" :
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down" :
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "left" :
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right" :
        x = head.xcor()
        head.setx(x+20)

#keyboard binding
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

while True:
    wn.update()

    #to check collision with boarder
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290 :
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide segment
        for seg in segments:
            seg.goto(1000 , 1000)

        #clear the segment list
        segments.clear()

        #Reset the score
        score=0
        pen.clear()
        pen.write("Score: {}   High Score: {}".format(score,high_score),align="center",font=("courier",24,"normal"))


    if head.distance(food) < 20 :
        #collision, move food to random
        x=random.randint(-290 , 290)
        y=random.randint(-290 , 290)
        food.goto(x , y)

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)

        #increase score
        score += 10

        if score >high_score:
            high_score=score
        
        pen.clear()
        pen.write("Score: {}   High Score: {}".format(score,high_score),align="center",font=("courier",24,"normal"))

    #make segment actually move with the head
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x , y)

    #mov the segment 0 where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x , y)

    move()

    #check for body collision 
    for seg in segments:
        if seg.distance(head)<20 :
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide segment
            for seg in segments:
                seg.goto(1000 , 1000)

            #clear the segment list
            segments.clear()

    time.sleep(delay)
wn.mainloop()