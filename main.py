"""
Code written by: Sidharth S aka Sid The Loser

Description: This code is actually a turtle port of a pygame code
written by DaFluffyPotato (links to his YT: https://www.youtube.com/channel/UCYNrBrBOgTfHswcz2DdZQFA).
So all credit goes to him. I hope that you will be able to understand the code even without
the comments, but you can read them to understand things if you get stuck.
"""

import turtle # This imports turtle module
import random # This imports random module

class draw(): # This is just a class named as "draw"
    def __init__(self): # This runs on the initiation of the class in the code
        self.pen = turtle.Turtle() # This makes a turtle object named as "pen"
        self.pen.hideturtle() # This hides the "pen"
        self.pen.penup() # This stops the "pen" from drawing on screen while moving
        self.pen.speed(0) # This makes the "pen" go Sonic speeds

    def circle(self, color, fill_color, position, radious): # This is a defenition on drawing a cicle on the screen
        self.pen.penup() # This again stops the "pen" from drawing on screen while moving
        self.pen.goto(position[0], position[1]) # This will move the "pen" to the provied location/coordiantes/position
        
        if type(fill_color) != type((0, 0, 0)): # This checks if the entered "fill_color" value is a tuple or not (There might be better ways to do this BTW)
                                                # If this if state ment is true then "fill_color" variable is not a tuple
            self.pen.color(color) # This sets the color of the "pen" as "color"
            self.pen.pendown() # This allows the "pen" to draw things on the screen
            self.pen.circle(radious) # This draws the circle in a give radious, ie. the "radious" variable in this case

        else: # This code runs if "fill_color" variable is a tuple
            
            self.pen.color(color, fill_color) # This sets the color of the "pen" including the "fill_color"
            self.pen.begin_fill() # This commands the "pen" to begin the color filling process
            self.pen.pendown() # This allows the "pen" to draw on the screen
            self.pen.circle(radious) # This draws a circle in the given radious, ie. the "radious" variable in this case
            self.pen.end_fill() # This commands the "pen" to fill up the areas drawn after "pen.begin_fill" is called to this line
            
        self.pen.penup() # This again stops the "pen" from drawing on screen while moving

    def clear(self): # This is a defenition on clearing the things done by "pen"
        self.pen.clear() # This clears everything done by "pen"

# From this point on till the line 53 I expect you to understand everything

wn = turtle.Screen()
wn.title("Turtle Particles")
wn.tracer(0)
wn.colormode(255)
wn.bgcolor((0, 0, 0))

pen = draw() # The variable "pen" stores the/references draw class

particles = [] # This just declares a list (this will later change into a dictionary BTW) named as "particles" which will later store data of about 78 or 80 particle in one frame

while True: # This is the main game loop
    wn.update() # This updates the screen while the loop is running
    pen.clear() # This clears the things done by the 
    
    particles.append([[0, 0], [random.randint(-10, 10) / 10, 3], random.randint(4, 10)]) # This stores the data about a single particle and appends this to "particles" list

    """ I'm currently talking about the code written in line 59.

        The 1st value/list in the list states the x and y coordinates of the particle.

        The 2nd value/list in the list states the nature of the movement of the particle.

        The 3rd value in the list states the size for the particle.
    """

    for particle in particles: # This is a for loop cycling through each particle in "particles" list
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] -= 0.1

        pen.circle((255, 255, 255), (255, 255, 255), particle[0], particle[2]) # This draws the circle as we say it its da particle

        if particle[2] <= 0:
            particles.remove(particle) # This removes the particle that are removed from the list when it reaches below or equal to 0 size/radious
