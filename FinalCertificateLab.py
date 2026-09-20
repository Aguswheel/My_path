import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, cantidad in kwargs.items():
            self.contents += [color] * cantidad
    
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            all_balls = self.contents
            self.contents = []
            return all_balls
        else:
            drawn_balls = []
            for _ in range(num_balls):
                ball = random.randrange(len(self.contents))
                drawn_balls.append(self.contents.pop(ball))
            return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        success = True
        for color, count in expected_balls.items():
            if drawn_balls.count(color) < count:
                success = False
                break
        if success:
            successful_experiments += 1
    return successful_experiments / num_experiments
    