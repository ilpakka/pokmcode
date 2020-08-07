import turtle
import math
import pygame


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Pokemon Map Grid Generator")
wn.setup(700, 700)

class Generator(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.goal = 0

    def go_up(self):
        # Coordinate sum check
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        # Collision check
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        # Coordinate sum check
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        # Collision check
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        # Coordinate sum check
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        # Collision check
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        # Coordinate sum check
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        # Collision check
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

class Goal(turtle.Turtle):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.goal = 1
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


# Creating a list of levels
levels = [""]

# Defining the first level
# player = 'P'  wall = 'X'  goal = 'M'
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXXX   M  XXXXXXXX",
    "X  XXXXXXXX      XXXXXXXX",
    "X  XXXXXXXXXX  XXXXXXXXXX",
    "X  XXXXXXXXXX  XXXXXXXXXX",
    "X                       X",
    "X        XXXXXXXXX  XXXXX",
    "XXXXXXX  XXXXXXXXX  XXXXX",
    "XXXXXXX  XXXXXXXXX  XXXXX",
    "XXXXXM     XXXXXXX  XXXXX",
    "XXXXX      XXXXXXX  XXXXX",
    "XXXXX      XXXXXXX  XXXXX",
    "XXXXX      XXXXXXX  XXXXX",
    "XXXXXXX  XXXXXXXXX  XXXXX",
    "XXXXXXX  XXXXXXM    XXXXX",
    "XXXXXXX  XXXXXX  XXXXXXXX",
    "XXXXXXX  XXXXXX  XXXXXXXX",
    "XXXXXXX          XXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

# Adding grid to grid list
levels.append(level_1)

# Creating Grid Setup Function
def setup_grid(level):

    for y in range(len(level)):
        for x in range(len(level[y])):
            # Finding each char at x and y coordinates
            char = level[y][x]
            # Calculating the screen coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # Check for walls 'X'
            if char == "X":
                gen.goto(screen_x, screen_y)
                gen.stamp()
                walls.append((screen_x, screen_y))

            if char == "P":
                player.goto(screen_x, screen_y)

            if char == "M":
                goals.append(Goal(screen_x, screen_y))

# Creating the instance
gen = Generator()
player = Player()

# Creating coordinates for walls
walls = []

# Creating coordinates for goal
goals = []

# Setup the level
setup_grid(levels[1])

# Keyboard binds
turtle.listen()
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")

# Ignoring screen update
wn.tracer(0)

# Main loop
while True:
    # Checking player collision with goal
    # Iterating through goal list
    for goal in goals:
        if player.is_collision(goal):
            player.goal += goal.goal
            # Print to check function validity
            print("Reached goals: {}".format(player.goal))
            # Removing the goal
            goal.destroy()
            # And also removing the goal from respective list
            goals.remove(goal)
    # Update
    wn.update()
