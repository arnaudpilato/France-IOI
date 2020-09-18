nbParticipants = int(input())
liste = [0] * nbParticipants
listeDécroissant = 0

for loop in range (nbParticipants):
  liste[loop] = int(input())

liste.sort()

for loop in range (nbParticipants // 2):
  listeDécroissant = listeDécroissant - 1
  
  print ("{} {}". format(liste[loop] , liste[listeDécroissant]))
