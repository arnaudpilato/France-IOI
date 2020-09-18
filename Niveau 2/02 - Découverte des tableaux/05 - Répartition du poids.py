nbCharettes = int(input())
charettes = [0] * nbCharettes
poidsTotal = 0

if (nbCharettes <= 3000):
  for loop in range (nbCharettes):
    poids = float(input())
    charettes[loop] = charettes[loop] + poids
    poidsTotal = poidsTotal + poids
    division = poidsTotal / nbCharettes
  
  for loop in range (nbCharettes):
    charettes[loop] = division - charettes[loop]
    print (charettes[loop]

else:
  print ("Erreur")
