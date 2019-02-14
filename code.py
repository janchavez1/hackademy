import math

import datetime

import os





def hello(a_name):

  print("Hello! " + a_name)





def hello2(name_a,name_b):

  print("Hello! " + name_a + " and " + name_b)





def sum_two(x,y):

  z = x + y

  return z





def circle_area(radius):

  a = math.pi * radius ** 2

  return a





def today():

  now = datetime.datetime.now()

  return now.day





def my_sum(a_list):

  total = 0

  for n in a_list:

    total = total + n

  return total





def my_prod(a_list):

  total = 1

  for n in a_list:

    total = total * n

  return total


def my_count(a_list):

  count = 0

  for n in a_list:

    count = n + count

  return count


def my_count_less_5(a_list):

  count = 0

  for n in a_list:

    if n < 5:

      count = count + 1

  return count


def my_count_ones(a_list):

  count = 0

  for n in a_list:

    if n == 1:

      count = count + 1

  return count


def is_list_empty(a_list):

  if my_count(a_list) == 0:

    return True

  else:

    return False


def my_max(a_list):

  if is_list_empty(a_list):

    return None

  else:

    b = a_list[0]

    for n in a_list:

      if n > b:

        b = n

    return b



# get_filenames('C:\\Users\\JChavez')

# --> list of file names

# ['C:\\Users\\JChavez\\code.py', 'C:\\Users\\JChavez\\imageprocessor.py', 'C:\\Users\\JChavez\\loops.py', 'start.py']

def get_filenames(a_dirname):

  list_of_files = os.listdir(a_dirname)

  all_files = []

  for filename in list_of_files:

    full_path = os.path.join(a_dirname,filename)

    if os.path.isdir(full_path): # if the file is a dir we skip it

      pass

    else:

      all_files.append(full_path)

  return all_files


first_list = [12, 34, [56, 67]]
def flatten(a_list_with_lists):
  new_list = []
  for n in a_list_with_lists:
    if isinstance(n,list):
      for i in n:
        new_list.append(i)
    else:
      new_list.append(n)
  return new_list

#number -> number of stars
def single_row_stars(number):
  for n in range(number):
    print("*",end="") 

#repeat string printed out
def single_row_of(number, string):
  for n in range(number):
    print(string,end="")

#square_of_stars(4)
def square_of_stars(number):
  for n in range(number):
    for n in range(number):
      print("*",end="")
    print()


#less stars
def less_stars(number):
  for n in range(0,number):
    for i in range(number,n,-1):
      print("*",end="")
    print()

def list_by_2(a_list):
  new_list = []
  for n in a_list:
    new_list.append(n*2)
a =[1,2,3]
print(a)

#create grid

def create_grid(size):
  new_grid = []
  for row in range(size):
    new_sublist = []
    for column in range(size):
      new_sublist.append('-')
    new_grid.append(new_sublist)
  return new_grid


