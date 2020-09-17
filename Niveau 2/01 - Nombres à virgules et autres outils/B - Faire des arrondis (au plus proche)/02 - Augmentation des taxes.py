taxeActuelle = float(input())
nouvelleTaxe = float(input())
prixLégume = float(input())

différence = (round(((prixLégume / (1 + taxeActuelle / 100)) * (1 + nouvelleTaxe / 100)) * 100)) / 100

print (différence)
