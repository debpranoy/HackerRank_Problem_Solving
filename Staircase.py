def Staircase(size):

    for i in range(1, size + 1 ):
      spaces = " " * (size - i)
      hashtags = "#" * i
      print(spaces+hashtags)

size = int(input())
Staircase(size)