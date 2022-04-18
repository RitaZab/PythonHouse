import turtle
turtle.speed('slowest')

def turtle_square():

    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)

def turtle_window():
    turtle.color('white')
    turtle.right(90)
    turtle.forward(40)
    turtle.color('black')
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.color('white')
    turtle.left(90)
    turtle.forward(40)
    turtle.color('black')

def turtle_rounding():
    turtle.forward(0.2)
    turtle.right(1)

def turtle_rounding_big():
     turtle.forward(1)
     turtle.left(1)

def turtle_fence():
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(45)
    turtle.forward(10.5)
    turtle.left(90)
    turtle.forward(10.5)
    turtle.left(45)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(15)

def turtle_rounding_big():
    turtle.forward(1)
    turtle.left(1)

def turtle_sun():
    for q in range(10):
        turtle_rounding_big()
    turtle.right(45)
    turtle.forward(30)
    turtle.left(120)
    turtle.forward(30)
    turtle.right(45)


turtle_square()
turtle.right (45)
turtle.forward (106)
turtle.right (90)
turtle.forward (106)
turtle.right(45)
turtle.forward(150)
turtle.right (90)
turtle.forward(15)
turtle_window()
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(15)
turtle_window()
turtle.right(90)
turtle.forward(65)
turtle.right(90)
turtle.forward(50)
turtle.right(45)
turtle.forward(25)
turtle.right(90)
turtle.forward(25)
turtle.right(135)
turtle.forward(35)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.color('white')
turtle.forward(17)
turtle.color('black')
turtle.speed('fastest')
for x in range(360):
    turtle_rounding()
turtle.forward(3)
turtle.color('white')
turtle.speed('slowest')
turtle.forward(15)
turtle.color('black')
turtle.right(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(150)
for y in range(5):
    turtle_fence()
turtle.color('white')
turtle.forward(10)
turtle.left(90)
turtle.forward(300)
turtle.color('orange')
for t in range(9):
    turtle_sun()
turtle.speed('fastest')
for x in range(360):
    turtle_rounding_big()




turtle.done