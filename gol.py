import random

def setup_game(size,max_alive):
    a_grid = get_empty_grid(size)
    fill_grid_random(a_grid,max_alive)


def get_empty_grid(size):
    new_grid = []
    for row in range(size):
        new_sublist = []
        for column in range(size):
            new_sublist.append('-')
        new_grid.append(new_sublist)
    return new_grid


def rand_alive():
    number = random.randint(1,3)
    if number == 1:
        return True
    else:
        return False



def fill_grid_random(a_grid,max_alive):
  size = len(a_grid)
  remaining = max_alive
  for r_i in range(size):   #r_i=row index
      for c_i in range(size): #c_i=column index
          if rand_alive() == True:
               if remaining < 0:
                   a_grid[r_i][c_i] = '-'
               else:
                   a_grid[r_i][c_i] = 'X'
                   remaining = remaining - 1
          else:
              a_grid[r_i][c_i] = '-'




def print_grid(a_grid):
   size = len(a_grid)
   for r_i in range(size):
       for c_i in range(size):
           print(a_grid[r_i][c_i],end="")
       print("")