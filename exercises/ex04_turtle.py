"""Exercise 04: Turtle. Draws a Duke Fan (;.

*Draw something twice: crazy_square call (lines 111, 113)
*Loop usage: triangle func (lines 30-40); square func (lines 43-54)
*Fill color: utilize triangle func to create brown-filled triangle (lines 108-110)
*Marker color: within crazy_square func def (lines 76-94); called twice in main (lines 114, 116).
*Function definitions:
***horizontal_line (18-24)
***vertical_line (28-35)
***triangle (39-49)
***square (53-64)
***crazy_triangle (68-82) [uses triangle as helper func]
***crazy_square (86-103) [uses square as helper func]
***frowny_face (107-111) [uses horizontal_line and vertical_line as helper funcs]
"""

__author__ = "730231193"

from turtle import Turtle, colormode, done


def horizontal_line(turtle: Turtle, x: float, y: float, length: float) -> None:
    """Draws a horizontal line."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(length)
    turtle.hideturtle()


def vertical_line(turtle: Turtle, x: float, y: float, length: float) -> None:
    """Draws a vertical line (going down)."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(-90)
    turtle.forward(length)
    turtle.hideturtle()


def triangle(turtle: Turtle, x: float, y: float, length: float) -> None:
    """Draws a triangle."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    i: int = 0
    while i < 3:
        turtle.forward(length)
        turtle.left(120)
        i += 1
    turtle.hideturtle()


def square(turtle: Turtle, x: float, y: float, length: float) -> None:
    """Draws a square."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    i: int = 0
    while i < 4:
        turtle.forward(length)
        turtle.left(90)
        i += 1
    turtle.end_fill()
    turtle.hideturtle()


def crazy_triangle(turtle: Turtle, x: float, y: float, length: float) -> None:
    """Draws a triangle with a bit of extra spice."""
    outline: Turtle = Turtle()
    triangle(outline, x, y, length)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.speed(15)
    i: int = 0
    while i < 33:
        length *= 0.97
        turtle.forward(length)
        turtle.left(120.3)
        i += 1
    turtle.hideturtle()


def crazy_square(turtle: Turtle, x: float, y: float, length: float) -> None:
    """Draws a square with a bit of extra spice."""
    outline: Turtle = Turtle()
    square(outline, x, y, length)
    colormode(255)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(51, 11, 214)
    turtle.speed(15)
    i: int = 0
    while i < 53:
        length *= 0.97
        turtle.forward(length)
        turtle.left(90.3)
        i += 1
    turtle.end_fill
    turtle.hideturtle()


def frowny_face(turtle: Turtle, x: float, y: float, length: float) -> None:
    horizontal_line(turtle, x, y, length)
    vertical_line(turtle, x, y, length / 5)
    turtle.left(90)
    vertical_line(turtle, x + length, y, length / 5)


def main() -> None:
    """The Dookie!."""
    turtle_1: Turtle = Turtle()
    colormode(255)
    turtle_1.begin_fill()
    turtle_1.fillcolor(189, 129, 94)
    triangle(turtle_1, -100, 100, 200)  # Draws the Dunce cap
    turtle_1.end_fill()
    turtle_1.pencolor("red")
    square(turtle_1, -100, -100, 200)  # Draws the blockhead
    crazy_square(turtle_1, -75, 25, 50)  # Draws a wonky right eye
    turtle_2: Turtle = Turtle()  # Creating a new variable bc it's too much of a headache to figure out angle position after crazy_square call
    crazy_square(turtle_2, 25, 25, 50)  # Draws a wonky left eye
    turtle_3: Turtle = Turtle()  # Same concept as line 105
    turtle_3.begin_fill()
    turtle_3.fillcolor(224, 18, 197)
    triangle(turtle_3, -25, 0, 50)  # Draws a nose w/ pink fill
    turtle_3.end_fill()
    turtle_3.pencolor(199, 163, 185)
    crazy_triangle(turtle_3, -25, 0, 50)  # Makes the nose look extra dumb
    turtle_4: Turtle = Turtle()  # Same concept as line 105
    turtle_4.pencolor(51, 11, 214)
    frowny_face(turtle_4, -75, -25, 150)  # Draws a frowny face for the Duke fan -- as it should be
    done()


if __name__ == "__main__":
    main()
