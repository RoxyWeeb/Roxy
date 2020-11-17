def shooter():
    import turtle
    import os
    import math

    print("Loading...")
    # Create Screen
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Shooter")

    # Draw Border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.penup()
    border_pen.setposition(-300, -300)
    border_pen.pendown()
    border_pen.pensize(3)
    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
    border_pen.hideturtle()

    score = 0

    score_pen = turtle.Turtle()
    score_pen.speed(0)
    score_pen.color("white")
    score_pen.penup()
    score_pen.setposition(-290, 280)
    scorestring = "Score: %s" % score
    score_pen.write(scorestring, False, align="left", font=("Comic Sans MS", 14, "normal"))
    score_pen.hideturtle()

    player = turtle.Turtle()
    player.color("green")
    player.shape("triangle")
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    player.setheading(90)

    playerspeed = 18

    enemy = turtle.Turtle()
    enemy.color("red")
    enemy.shape("square")
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(-200, 250)
    enemy.turtlesize(1.3)

    enemyspeed = 2

    bullet = turtle.Turtle()
    bullet.color("blue")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.hideturtle()

    bulletspeed = 20

    bulletstate = "ready"

    def move_left():
        x = player.xcor()
        x -= playerspeed
        if x < -280:
            x = - 280
        player.setx(x)

    def move_right():
        x = player.xcor()
        x += playerspeed
        if x > 280:
            x = 280
        player.setx(x)

    def shoot():
        global bulletstate
        if bulletstate == "ready":
            bulletstate = "shooting"
            x = player.xcor()
            y = player.ycor() + 10
            bullet.setposition(x, y)
            bullet.showturtle()

    def isCollision(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.xcor(), 2))
        if distance < 30:
            return True
        else:
            return False

    turtle.listen()
    turtle.onkey(move_left, "a")
    turtle.onkey(move_right, "d")
    turtle.onkey(shoot, "space")
    while True:

        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280:
            y = enemy.ycor()
            y -= 40
            enemyspeed *= -1
            enemy.sety(y)

        if enemy.xcor() < -280:
            y = enemy.ycor()
            y -= 40
            enemyspeed *= -1
            enemy.sety(y)

        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            enemy.setposition(-200, 250)
            score += 1
            scorestring = "Score: %s" % score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Comic Sans MS", 14, "normal"))
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            turtle.write("Game Over!", align="center", font=("Comic Sans MS", 80, "normal"))
            break
        if bulletstate == "shooting":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)

        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"

    turtle.done()