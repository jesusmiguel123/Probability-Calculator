import copy
import random
# Consider using the modules imported above.

class Hat:
   def __init__(self, **kwargs):
      contents = []
      for k in kwargs:
         contents.extend([k for _ in range(kwargs[k])])
      self.contents = contents
   
   def draw(self, n_balls):
      if n_balls >= len(self.contents):
         return self.contents
      balls  = []
      for _ in range(n_balls):
         ix = random.randint(0, len(self.contents) - 1)
         balls.append(self.contents.pop(ix))
      return balls

def experiment(
   hat,
   expected_balls,
   num_balls_drawn,
   num_experiments):
   ocurrencies = 0
   for _ in range(num_experiments):
      new_hat = copy.deepcopy(hat)
      sample = new_hat.draw(num_balls_drawn)
      d = {}
      for ball in sample:
         if ball in expected_balls:
            d[ball] = d[ball] + 1 if ball in d else 1
      for ball in expected_balls:
         if ball not in d:
            break
         if d[ball] < expected_balls[ball]:
            break
      else:
         ocurrencies = ocurrencies + 1
   return ocurrencies / num_experiments
