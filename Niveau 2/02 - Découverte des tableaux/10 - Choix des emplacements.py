nbEmplacements = int(input())
tableauEmplacements = [0] * nbEmplacements

for position in range (nbEmplacements):
  marchand = int(input())
  tableauEmplacements[marchand] = position

for loop in range (nbEmplacements):
  print (tableauEmplacements[loop])
