import turtle

def draw_concentric_squares(t, num_squares, screen_size):
    t.speed(0)  # Fastest drawing speed
    size = screen_size
    decrement = size / num_squares
    
    #Creates a nested loop 
    for _ in range(num_squares):  # Creates a loop that iterates through the number of squares, which is 20
        t.color(random.color())

        t.begin_fill()
        for _ in range(4):  # Creates another loop that draws the square
            t.forward(size)
            t.right(90)
        t.penup()
        t.goto(-size / 2, size / 2)  # Moves to the next square position
        t.pendown()
        size -= decrement  # Decreases size for the next square
        t.end_fill()
# Creates the turtle screen and turtle object
screen = turtle.Screen()
screen.setup(width=800, height=800)  # Sets the screen size
t = turtle.Turtle()

colors = {
    'AliceBlue': (240, 248, 255),
    'AntiqueWhite': (250, 235, 215),
    'Aqua': (0, 255, 255),
    'Aquamarine': (127, 255, 212),
    'Azure': (240, 255, 255),
    'Beige': (245, 245, 220),
    'Bisque': (255, 228, 196),
    'Black': (0, 0, 0),
    'BlanchedAlmond': (255, 235, 205),
    'Blue': (0, 0, 255),
    'BlueViolet': (138, 43, 226),
    'Brown': (165, 42, 42),
    'BurlyWood': (222, 184, 135),
    'CadetBlue': (95, 158, 160),
    'Chartreuse': (127, 255, 0),
    'Chocolate': (210, 105, 30),
    'Coral': (255, 127, 80),
    'CornflowerBlue': (100, 149, 237),
    'Crimson': (220, 20, 60),
    'Cyan': (0, 255, 255),
    'DarkBlue': (0, 0, 139)
}

# Draws concentric squares
draw_concentric_squares(t, num_squares=20, screen_size=800)

# Function to get coordinates on click
def get_coordinates(x, y):
    print(f"You clicked at ({x}, {y})")

# Capture click events to get coordinates
turtle.onscreenclick(get_coordinates)

# Keep the window open
turtle.mainloop()

# Hide the turtle and finish
t.hideturtle()
screen.mainloop()
