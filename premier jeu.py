import turtle

wn = turtle.Screen()
wn.title(" Mon premier jeu ")
wn.bgcolor("black")
wn.setup(width = 800 , height = 600)
wn.tracer(0)


scoreA=0
scoreB=0



pad_A= turtle.Turtle()
pad_A.speed(0)
pad_A.shape("square")
pad_A.color("red")
pad_A.shapesize(stretch_wid=5, stretch_len=1)
pad_A.penup()
pad_A.goto(-350,0)

pad_B= turtle.Turtle()
pad_B.speed(0)
pad_B.shape("square")
pad_B.color("blue")
pad_B.shapesize(stretch_wid=5, stretch_len=1)
pad_B.penup()
pad_B.goto(350,0)


ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2


pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
#pen.write("Joueur A:    Joueur B:",aligne="center")


def pad_A_up():
	y=pad_A.ycor()
	y+=20
	pad_A.sety(y)


def pad_A_down():
	y=pad_A.ycor()
	y-=20
	pad_A.sety(y)


def pad_B_up():
	y=pad_B.ycor()
	y+=20
	pad_B.sety(y)


def pad_B_down():
	y=pad_B.ycor()
	y-=20
	pad_B.sety(y)


wn.listen()
wn.onkeypress(pad_A_up, "z")
wn.onkeypress(pad_A_down, "s")
wn.onkeypress(pad_B_up, "Up")
wn.onkeypress(pad_B_down, "Down")



while True:
	wn.update()
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy*= -1

	if ball.xcor() > 390:
		ball.goto(0,0)
		ball.dx*= -1
		scoreA +=1
	if ball.xcor() < -390:
		ball.goto(0,0)
		ball.dx*= -1
		scoreB +=1



	if ball.xcor() > 340 and (ball.ycor() < pad_B.ycor() + 40 and ball.ycor() > pad_B.ycor()-40):
		ball.setx(340)
		ball.dx *=-1
	if ball.xcor() < -340 and (ball.ycor() < pad_A.ycor() + 40 and ball.ycor() > pad_A.ycor()-40):
		ball.setx(-340)
		ball.dx *=-1