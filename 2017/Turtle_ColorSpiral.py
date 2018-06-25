#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import turtle

import time

turtle.speed("fastest")
turtle.pensize(2)
turtle.bgcolor("black")
colors=['red','yellow','purple','orange']
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(colors[x%4])
    turtle.left(91)
turtle.tracer(True)
turtle.done()