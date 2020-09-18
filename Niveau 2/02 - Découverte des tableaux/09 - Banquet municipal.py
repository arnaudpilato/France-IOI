positions = int(input())
changements = int(input())
tableauPositions = [0] * positions

for loop in range (positions):
  tableauPositions[loop] = int(input())

for loop in range (changements):
  position1 = int(input())
  position2 = int(input())
  valeur1 = tableauPositions[position1]
  valeur2 = tableauPositions[position2]
  tableauPositions[position1] = valeur2
  tableauPositions[position2] = valeur1

for loop in range (positions):
  print (tableauPositions[loop])
