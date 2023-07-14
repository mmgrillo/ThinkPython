# Page 27

def grid_exercise(a,b,c):
    print(a, b * 4, a, b * 4, a, end="\n")
    print(c, " " * 4, c, " " * 4, c)
    print(c, " " * 4, c, " " * 4, c)
    print(c, " " * 4, c, " " * 4, c)
    print(c, " " * 4, c, " " * 4, c)
    print(a, b * 4, a, b * 4, a, end="\n")
    print(c, " " * 4, c, " " * 4, c)
    print(c, " " * 4, c, " " * 4, c)
    print(c, " " * 4, c, " " * 4, c)
    print(c, " " * 4, c, " " * 4, c)
    print(c, " " * 4, c, " " * 4, c)
    print(a, b * 4, a, b * 4, a, end="\n")

print(grid_exercise("+", "-", "|"))


#Bard suggestion:

def grid_exercise(a, b, c):

  top_row = a + b * 4 + a + b * 4 + a
  middle_row = c + " " * 4 + c + " " * 4 + c
  bottom_row = a + b * 4 + a + b * 4 + a

  for row in [top_row, middle_row, middle_row, middle_row, middle_row, bottom_row]:
    print(row)


print(grid_exercise("+", "-", "|"))


