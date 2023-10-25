from graphics import *   #import the graphics.py module (must be in the same folder this file)


#OPEN THE WINDOW
win = GraphWin("My First Graphics Window", 500, 500)#open a window object called "win" with size and title 
win.setBackground("Mint Cream")# Set the background colour of the window

x = 250
y = 250
left_right = False
up_down = False
color = "Red"
def move():
    global x
    global y
    global z
    global color
    global up_down
    global left_right
    global win

    if x < 480 and left_right == False:
        x += 2
        if x == 480:
            left_right = True
            color = "Green"
    elif x > 20 and left_right == True:
        x -= 2
        if x == 20:
            left_right = False
            color = "Blue"

    if y < 480 and up_down == False:
        y += 1
        if y == 480:
            up_down = True
            color = "Orange"
    elif y > 20 and up_down == True:
        y -= 1
        if y == 20:
            up_down = False
            color = "Brown"

    circle = Circle(Point(x,y),20)
    circle.setFill(color)
    circle.draw(win)



def circle():
    my_heading = Text(Point(250,30), 'Welcome to the Circles')
    my_heading.draw(win)

    while True:
        move()
        win.update()
        win.delete("all")


circle()
