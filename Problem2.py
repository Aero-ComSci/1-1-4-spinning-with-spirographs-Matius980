import turtle

# Setup the screen
screen = turtle.Screen()
screen.setup(width=800, height=800)  # Set screen to width of 800
screen.title("Centered Objects")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)  # Fastest drawing

# Create a class with functions to create a dot
def draw_object(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("blue")
    pen.begin_fill()
    pen.circle(object_radius)  # Object size 
    pen.end_fill()

