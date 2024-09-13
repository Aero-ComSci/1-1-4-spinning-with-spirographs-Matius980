import turtle

# Function to draw a black dot at a specific position
def draw_object(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(50, "blue")  # Draws a black circle with a radius of 50
