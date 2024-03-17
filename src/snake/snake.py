from enum import Enum
import turtle
import random

class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3
    

class Snake:
    
    def __init__(self, x, y, direction) -> None:
        self.coordinates = [(x, y)]
        self.direction = direction
        self.snake_pen = turtle.Turtle()
        self.snake_pen.speed(0)
        self.snake_pen.ht()
    
    def move(ate_food: bool) -> None:
        pass
    
    def change_direction(new_direction) -> None:
        pass
    
    def draw() -> None:
        pass
    
    def bumped_into_edge() -> bool:
        pass
    
    def bumped_into_itself() -> bool:
        pass
    
    def is_position_in_snake(self, position) -> bool:
        for coordinate in self.coordinates:
            if coordinate[0] == position[0] and coordinate[1] == position[1]:
                return True
        return False
    
    
class Game:
    
    def __init__(self) -> None:
        self.score = 0
        self.food = None
        self.food_pen = turtle.Turtle()
        self.food_pen.speed(0)
        self.food_pen.ht()
        turtle.bgcolor('yellow')
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        
    def generate_new_food(self, s: Snake) -> None:
        # what is the formula for the min and max x and y coordinates of the new food?
        # screen has self.width width and self.height height
        # the x of the food has to be between - self.width / 2 and self.width / 2
        # to generate a random number between m and n use random.randint(m, n)
        found = False
        # This might not work only if the snake is the size of the entire screen - unlikely to happen
        while not found:
            x = random.randint(-self.width/2, self.width/2)
            y = random.randint(-self.height/2, self.height/2)  
            found = not s.is_position_in_snake((x, y))
        self.food = (x, y)
    
    def draw_food(self) -> None:
        pass
    
    
g = Game()
s = Snake(0, 0, Direction.NORTH)