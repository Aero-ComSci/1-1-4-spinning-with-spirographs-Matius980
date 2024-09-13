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
6. Insert a screenshot or picture of the algorithm you used for your tokenizer on the previous activity.
7. Give an example of an undecidable problem, attach code.
   

## Project 1. Zero Iteration Conditions vs. Infinite Loops

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

## Project 2. Create an algorithm that places up to 5 objects in equal distance from each other

* ![image](https://github.com/user-attachments/assets/41401bd7-9038-465d-b8cb-32628bc0f4df)
* The output of problem 2 shows 5 yellow dots perfectly spaced from each other. Additionally, the dots are drawn in the middle of the screen.
## Project 3. Concentric Squares
* Concentric Squares code:
* ![Screenshot 2024-09-10 135359](https://github.com/user-attachments/assets/035ca481-3012-40d0-a6f0-bfe3bf4ad72b)
* ![image](https://github.com/user-attachments/assets/5eceb96b-7ff3-4b3f-814f-25bf10ec4055)

* Output of the code:
* ![image](https://github.com/user-attachments/assets/f8bdc660-5392-461c-aa3f-185fa0a9b6d7)

## Project 4. Complete steps 17,18,19 (mypltw)

### Step 17:

*  ![image](https://github.com/user-attachments/assets/156197bd-2166-456d-a71a-8adcb94b8237)
* For step 17, I added a for loop to iterate through the code twice, drawing 2 mountains instead of one.
### Step 18:

*  ![image](https://github.com/user-attachments/assets/5849da6a-6e5d-4bd3-ad27-3d6758ab4f07)
* I added similar code to the algoritm that draws the 2 mountains, except they are upside down.
* To do this, I changed the values of x, y, move_x, move_y.
### Step 19:

*  ![image](https://github.com/user-attachments/assets/80f4d8bd-cc68-48fa-a60f-cca791ef880b)
* This was probably the most simple part of the code, added a condition stating "while True" and it creates an infinite loop.

## Project 5. Answer Step 21

* Question: ![image](https://github.com/user-attachments/assets/9882739e-ec1a-4fa0-89c5-bf306e5b6cae)

* The flowchart represents the algorithm where you avoid a zero iteration condition and draw five circles on the screen. 

## Project 6. Explain Tokenizer

* ![image](https://github.com/user-attachments/assets/09bb5072-e7b2-4a32-8a11-43d08c69b780)

+ In this tokenizer, the goal is to grab the user input, break it down, and if the user's input consist of a specific flower in our shop, then it will call the function.
+ Also, if the user input is similar to the flower in our shop, and is inside our dictionary, then it will still call the function. My partner and I created a dictionary that takes the user input with its mispelled plurals and translates it to a string that is compatible with the code.
+ Next, the flower that the user input chooses will be called and will be drawn at its corresponding coordinate.
+ Additionally, there will be another piece of code that creates an error for the user if the flower they request isn't in the shop.
+ Once the user has specified their flower, they have the ability to choose the quantity of flowers, and we take that input and draw however many flowers they want, unless it is more than 5 flowers. If there are more than 5 flowers requested, an error will occur.
+ Lastly, our code comprises of a code that provides the name of our flower shop and the prompt to answer.

## Project 7. Undecidable Problem
* An undecidable problem is an algorithm that cannoth be solved
* I've created a short replica of an infinite loop which can't be solved because the statement is always true.
* ![image](https://github.com/user-attachments/assets/740a8877-20ae-47d8-b0bd-3a63af7bc8fc)
* This is the same loop I created to give an example of the infinite loop.
