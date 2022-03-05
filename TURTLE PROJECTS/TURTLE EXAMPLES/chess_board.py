import turtle

NUM_SQUARES = 8  # Number of squares along one size of board.
SQUARE_SIZE = 40  # Pixels
BOARD_SIZE = SQUARE_SIZE * NUM_SQUARES
BORDER_FRACTION = 1.025  # Add a slight border to the board.
STAMP_SIZE = 20  # Size of turtle square image.

screen = turtle.Screen()
screen.title("Chess Board")
screen.setup(400, 400)

screen.tracer(0)  # Disable animation.
pen = turtle.Turtle(shape='square', visible=False)
pen.shapesize(BOARD_SIZE / STAMP_SIZE * BORDER_FRACTION)
pen.color('black')
pen.stamp()

pen.shapesize(SQUARE_SIZE / STAMP_SIZE)
pen.color('white')
pen.penup()

for y in range(-NUM_SQUARES // 2, NUM_SQUARES // 2):
    parity = y % 2 == 0

    for x in range(-NUM_SQUARES // 2, NUM_SQUARES // 2):
        if parity:
            pen.goto(x * SQUARE_SIZE + SQUARE_SIZE // 2, y * SQUARE_SIZE + SQUARE_SIZE // 2)
            pen.stamp()

        parity = not parity

turtle.done()