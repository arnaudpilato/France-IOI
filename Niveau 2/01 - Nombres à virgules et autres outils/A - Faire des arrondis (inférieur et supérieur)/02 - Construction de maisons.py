from math import *

qtéCiment = float(input())
sac = 60
prix = 45
nbSac = 0
calcul = qtéCiment / sac
nbSac = ceil(calcul)

print (nbSac * prix)
