import turtle
import time
import random


class Jhonatan:
    def __init__(self):
        self.t = turtle.Turtle()
        self.shapes = ['arrow', 'turtle', 'circle',
                       'square', 'triangle', 'classic']
        self.colors = ['red', 'blue', 'green',
                       'yellow', 'black', 'brown', 'pink']
        self.speed = [5, 6, 7, 8, 9, 10]

    def start(self):
        self.restart_position()
        self.move_to_start()
        self.write_j()
        self.write_h()
        self.write_o()
        self.write_n()
        self.write_a(0)
        self.write_t()

    def restart_position(self):
        self.t.setheading(360)

    def RGB_me(self):
        self.t.speed(random.choice(self.speed))
        self.t.shape(random.choice(self.shapes))
        self.t.color(random.choice(self.colors))

    def move_to_start(self):
        self.RGB_me()
        self.t.penup()
        self.t.setpos(-400, 150)
        self.t.pendown()

    def write_j(self):
        self.RGB_me()
        self.t.forward(50)
        self.t.backward(100)
        self.t.forward(50)
        self.t.right(90)
        self.t.forward(150)
        self.t.right(90)
        self.t.forward(25)
        self.t.right(90)
        self.t.forward(25)
        self.t.penup()
        self.t.right(45)
        self.t.forward(175)

    def write_h(self):
        self.RGB_me()
        self.t.pendown()
        self.t.right(135)
        self.t.forward(150)
        self.t.backward(75)
        self.t.left(90)
        self.t.forward(50)
        self.t.left(90)
        self.t.forward(75)
        self.t.backward(150)
        self.t.right(85)
        self.t.penup()
        self.t.forward(100)

    def write_o(self):
        self.RGB_me()
        self.t.pendown()
        self.t.circle(70)
        self.t.right(5)
        self.t.penup()
        self.t.forward(80)

    def write_n(self):
        self.RGB_me()
        self.t.pendown()
        self.t.left(90)
        self.t.forward(150)
        self.t.right(165)
        self.t.forward(160)
        self.t.left(165)
        self.t.forward(150)
        self.t.right(175)
        self.t.penup()
        self.t.forward(150)

    def write_a(self, angulo):
        self.RGB_me()
        if angulo != 160:
            angulo = 170
        self.t.pendown()
        self.t.left(angulo)
        self.t.forward(150)
        self.t.right(165)
        self.t.forward(150)
        self.t.left(180)
        self.t.forward(75)
        self.t.left(90)
        self.t.forward(20)
        self.t.backward(20)
        self.t.penup()

    def write_t(self):
        self.RGB_me()
        self.t.right(240)
        self.t.forward(90)
        self.t.pendown()
        self.t.left(140)
        self.t.forward(145)
        self.t.left(90)
        self.t.forward(50)
        self.t.backward(100)
        self.t.penup()
        self.t.right(240+20)
        self.t.forward(145)
        self.write_a(160)
        self.t.pendown()
        self.t.penup()
        self.t.right(240)
        self.t.forward(90)
        self.t.left(145)
        self.t.pendown()
        self.t.forward(150)
        self.t.right(165)
        self.t.forward(160)
        self.t.left(165)
        self.t.forward(150)
        self.t.right(175)
        self.t.penup()
        self.t.forward(150)
        self.start()


challenge = Jhonatan()
challenge.start()
