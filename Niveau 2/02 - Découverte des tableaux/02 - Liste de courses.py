prixKilo = [9, 5, 12, 15, 7, 42, 13, 10, 1, 20]
résultat = 0

for loop in range (10):
  kilo = int(input())
  calcul = kilo * prixKilo[loop]
  résultat = résultat + calcul

print (résultat)
