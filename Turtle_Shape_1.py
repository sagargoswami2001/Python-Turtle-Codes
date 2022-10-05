from tkinter import N
import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor('black')
t.speed(0)

n=50
h=0

for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,0.9)
    h+=1/n
    t.color(c)
    t.forward(i*2)
    t.left(145)