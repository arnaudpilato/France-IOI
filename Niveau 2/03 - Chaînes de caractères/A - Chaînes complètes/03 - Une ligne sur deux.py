nbLignes = int(input())
tableau = [0] * nbLignes

for loop in range (nbLignes):
  tableau[loop] = input()

for loop in range (0, nbLignes, 2):
  print (tableau[loop])
