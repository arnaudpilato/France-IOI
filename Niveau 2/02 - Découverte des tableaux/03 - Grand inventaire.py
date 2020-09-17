nbOpérations = int(input())
inventaire = [0] * 11

for loop in range (nbOpérations):
  ingrédient = int(input())
  quantité = int(input())
  inventaire =[ingrédient] += quantité

for loop in range (1, 11):
  print (inventaire[loop])
