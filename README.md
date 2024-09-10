[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SkD24yV8)
# 1.1.4 Spirographs

*Complete the following.*

1. Compare and contrast zero-iteration conditions and infinite loops.
2. A link to your code where you solve the following problem. Take the screen size of 800px. Create code or algorithm that always places the object(s), up to 5, in the center an equal distance from one another and from the edges of the screen.
3. Concentric Squares -- Add a screenshot of your result and the code to create it on your repo.
Objective: Write a Python program using the turtle module to draw a pattern of concentric squares. The pattern should be created using nested loops.

Instructions:

Setup the Turtle Environment:
Import the turtle module.
Create a turtle object.
Set the turtle speed to the fastest setting.
Draw Concentric Squares:
Use a nested loop to draw multiple squares.
The outer loop should control the number of squares.
The inner loop should draw each square.
Each square should be slightly larger than the previous one.
Customize the Pattern:
Use different colors for each square.
Ensure the squares are centered on the screen.
Example Output:

The turtle should draw a series of squares, each one larger than the last, creating a pattern of concentric squares.

Hints:

Use the penup() and pendown() methods to move the turtle without drawing.
Use the color() method to change the turtle’s color.
Use the forward() and right() methods to draw the sides of the squares.


4. Complete the steps 17, 18 and 19 from [mypltw use clever to sign on](https://pltw.read.inkling.com/a/b/5310c007377c46e28d745961310f0c2e/p/728c751a6c4145bea0ea83c5058fb9f9#44b0003a2ee14fcc9865e7bb5faec747)
5. Answer to step 21
6. Insert a screenshot or picture of the algorith you used for your tokenizer on the previous activity.
7. Give an example of an undecidable problem, attach code.
   

## 1. Zero Iteration Conditions vs. Infinite Loops

### Zero Iteration Conditions
*  A zero iteration condition is a loop that never starts. For example, I can set the loop to run 0 times or set it to false, which will turn into a zero iteration condition.
*  Zero iteration conditions are useful when certain conditions aren't met, which allows less errors to occur.
*  This is an example of what a zero iteration condition could look like:
*  ![image](https://github.com/user-attachments/assets/465a2cd3-ad15-4c40-a353-bcbc6223ab66)
* In this photo, the condition is that the code will print "I love apples!" if the value of apples is greater than 10, which will never happen.
### Infinite Loops
* Infinite loops are the exact opposite of zero iteration conditions. The loop continues to run constantly because the terminating condition is never met. The infinite loop can only be terminated externally
* Infinite loops can be used for keeping an application running, along with various reasons.
* This is an example of what an infinite loop would look like:
* ![image](https://github.com/user-attachments/assets/9caa386d-b6da-4011-a858-615920017abd)
* In this piece of code, apple is equal to zero and the while condition is stating that if apple is less than 1, then it will print "I love apples!". Because apple will always be less than 1, it will run forever.
