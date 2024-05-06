import colorgram
import random
from turtle import Turtle, Screen, colormode

# remember the window height and window width are 1200 height and 1280 width

colors = colorgram.extract("image.jpg", 2 ** 32)
# colors has some white colors therefore we filter them out!
# [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]
color_list = [ tuple(color.rgb) for color in colors if not (color.rgb.r > 230 and color.rgb.g > 230 and color.rgb.b > 230) ]

turtle = Turtle()
colormode(255)
turtle.penup()
turtle.hideturtle()

turtle.shape("turtle")
turtle.speed("fastest")

x = -540
y = -450

# end_x = 560
end_y = 540
turtle.setpos(x, y)

while y < end_y:
  for _ in range(-250, 250, 50):
    turtle.dot(20, random.choice(color_list))
    if _ <= 250:
      turtle.fd(120)
  y += 100
  if y < end_y:
    turtle.setpos(x, y)


screen = Screen()
# print("screen.canvheight", screen.canvheight) # 300
# print("screen.window_height()", screen.window_height()) # 1200
# print("screen.canvwidth", screen.canvwidth) # 400
# print("screen.window_width()", screen.window_width()) # 1280
screen.exitonclick()