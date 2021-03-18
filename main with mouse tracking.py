import turtle
import random

class draw():
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.speed(0)

    def circle(self, color, fill_color, position, radious):
        self.pen.penup()
        self.pen.goto(position[0], position[1])
        
        if type(fill_color) != type((0, 0, 0)):
            
            self.pen.color(color)
            self.pen.pendown()
            self.pen.circle(radious)

        else:
            
            self.pen.color(color, fill_color)
            self.pen.begin_fill()
            self.pen.pendown()
            self.pen.circle(radious)
            self.pen.end_fill()
            
        self.pen.penup()

    def clear(self):
        self.pen.clear()

wn = turtle.Screen()
wn.title("Turtle Particles")
width, height = 600, 400
wn.screensize(width, height)
wn.tracer(0)
wn.colormode(255)
wn.bgcolor((0, 0, 0))
wn.cv._rootwindow.resizable(False, False)

pen = draw()

particles = []

x, y = 0, 0

def motion(event):
    global x, y
    x, y = event.x, event.y

canvas = wn.getcanvas()
canvas.bind('<Motion>', motion)

while True: 
    wn.update()
    pen.clear()
    
    particles.append([[x-(width*0.53), -y+(height*0.65)], [random.randint(-10, 10) / 10, 3], random.randint(5, 10)])

    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] -= 0.1

        pen.circle((255, 255, 255), (50, 100, 50), particle[0], particle[2])

        if particle[2] <= 0:
            particles.remove(particle)
