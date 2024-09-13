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

# Number of objects
num_objects = 5
object_radius = 20  # Radius of each circular object
object_diameter = 2 * object_radius

# Calculate spacing by grabbing the screen size then using math to create spacing between each dot
total_width = 800
total_objects_width = num_objects * object_diameter
spacing = (total_width - total_objects_width) / (num_objects + 1)

# Calculate the starting x position to center objects
starting_coordinate = -total_width / 2 + spacing + object_radius

# Draw objects
for i in range(num_objects):
    x = starting_coordinate + i * (object_diameter + spacing)
    y = 0  # Center the dots
    draw_object(x, y)

# Keep the window open until closed by the user
turtle.done()
