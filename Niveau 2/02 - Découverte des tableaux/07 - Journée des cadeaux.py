nbHabitants = int(input())
valeur = [0] * nbHabitants

for loop in range (nbHabitants):
  fortune = int(input())
  valeur[loop] = fortune

valeur.sort()

if nbHabitants % 2 == 1:
  valeurImpair = (nbHabitants - 1) // 2
  
  print (valeur[valeurImpair])
else:
  valeurPair = nbHabitants // 2
  
  print ((valeur[valeurPair -1] + valeur[valeurPair]) / 2)
