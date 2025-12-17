from turtle import Turtle, Screen
import pandas as pd


turtle = Turtle()
turtle.hideturtle()
turtle.penup()

screen = Screen()
screen.title("U.S.STATES GAME QUIZ")
screen.bgpic("blank_states_img.gif")


data = pd.read_csv("50_states.csv")
turtle.goto(x=100, y=50)

screen.exitonclick()



