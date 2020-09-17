from math import *

population = int(input())
croissance = float(input())
calcul = croissance / 100 * population + population
arrondiInf = floor(calcul)

print (arrondiInf)
