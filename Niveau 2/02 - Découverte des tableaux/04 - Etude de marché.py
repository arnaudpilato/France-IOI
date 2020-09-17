nbProduits = int(input())
nbPersonnes = int(input())
produits = [0] * nbProduits

if (nbPersonnes <= 1000):
  for loop in range (nbPersonnes):
    choix = int(input())
    produits[choix] = produits[choix] + 1
  
  for loop in range (nbProduits):
    print (produits[loop])

else:
  print ("Erreur")
