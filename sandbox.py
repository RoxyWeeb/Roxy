def sandbox():
    import turtle
    import math
    import random

    wn = turtle.Screen()
    wn.title("Sandbox")
    wn.bgcolor("Yellow")

    mypen = turtle.Turtle()
    mypen.penup()
    mypen.setposition(-300, -300)
    mypen.pendown()
    mypen.pensize(3)
    for side in range(4):
        mypen.forward(600)
        mypen.left(90)
    mypen.hideturtle()

    player = turtle.Turtle()
    player.color("green")
    player.shape("triangle")
    player.penup()
    player.speed(0)

    speed = 1


    def turnLeft():
        player.left(30)


    def turnRight():
        player.right(30)


    def increasespeed():
        global speed
        speed += 1

    turtle.listen()
    turtle.onkey(turnLeft, "Left")
    turtle.onkey(turnRight, "Right")
    turtle.onkey(increasespeed, "Up")

    while True:
        player.forward(speed)

        if player.xcor() > 300 or player.xcor() < -300:
            player.right(180)

        if player.ycor() > 300 or player.ycor() < -300:
            player.right(180)

    turtle.done()