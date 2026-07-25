class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food_positions = [(f[1], f[0]) for f in food ]
        self.food_index = 0
        self.snake_body = [(0,0)]
        

    def check_collision(self, pos: tuple[int]):
        x, y = pos
        if x >= self.width or x < 0:
            return True
        if y >= self.height or y < 0:
            return True
        if (x,y) in self.snake_body[1:]:
            return True
        else:
            return False

    def update(self, new_pos: tuple[int]) -> int:
        if self.food_index < len(self.food_positions) and new_pos == self.food_positions[self.food_index]:
            self.snake_body = [new_pos] + self.snake_body
            self.food_index += 1 
        else:
            self.snake_body = [new_pos] + self.snake_body[:-1]
        
        if self.check_collision(new_pos):
            return -1
        else:
            return len(self.snake_body) - 1
    
    def move(self, direction: str) -> int:

        x, y = self.snake_body[0]
        match direction:
            case "R":
                new_pos = (x+1, y)
            case "L":
                new_pos = (x-1, y)
            case "U":
                new_pos = (x, y -1)
            case "D":
                new_pos = (x, y + 1)
        # print(new_pos, self.food_positions, direction)
        return self.update(new_pos)


        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
