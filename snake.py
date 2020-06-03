import turtle
import random
import time

delay = 0.1

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

segments= []

obj1= turtle.Turtle()
obj1.speed(9)
obj1.shape("triangle")
obj1.color("red")
obj1.penup()
obj1.goto(-100 , 190) 

obj2= turtle.Turtle()
obj2.speed(9)
obj2.shape("triangle")
obj2.color("red")
obj2.penup()
obj2.goto(-200 , 75)

obj3= turtle.Turtle()
obj3.speed(9)
obj3.shape("triangle")
obj3.color("red")
obj3.penup()
obj3.goto(100 , -190)

obj4= turtle.Turtle()
obj4.speed(9)
obj4.shape("triangle")
obj4.color("red")
obj4.penup()
obj4.goto(200 , -75)

obj5= turtle.Turtle()
obj5.speed(9)
obj5.shape("triangle")
obj5.color("red")
obj5.penup()
obj5.goto(100 , 190)

obj6= turtle.Turtle()
obj6.speed(9)
obj6.shape("triangle")
obj6.color("red")
obj6.penup()
obj6.goto(200 , 75)

obj7= turtle.Turtle()
obj7.speed(9)
obj7.shape("triangle")
obj7.color("red")
obj7.penup()
obj7.goto(-100 , -190)

obj8= turtle.Turtle()
obj8.speed(9)
obj8.shape("triangle")
obj8.color("red")
obj8.penup()
obj8.goto(-190 , -75)



head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("grey")
head.penup()
head.goto(0,0)
head.direction = "stop"


food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("pink")
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


    #obstacles1
    if head.distance(obj1) < 20 :
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

    #obstacles2
    if head.distance(obj2) < 20 :
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

    #obstacles1
    if head.distance(obj3) < 20 :
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

    #obstacles1
    if head.distance(obj4) < 20 :
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

    #obstacles1
    if head.distance(obj4) < 20 :
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

    #obstacles1
    if head.distance(obj5) < 20 :
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

    #obstacles1
    if head.distance(obj6) < 20 :
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

    #obstacles1
    if head.distance(obj7) < 20 :
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

    #obstacles1
    if head.distance(obj8) < 20 :
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