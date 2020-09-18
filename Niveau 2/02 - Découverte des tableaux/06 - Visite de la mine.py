totalDéplacement = int(input())
déplacement = [0] * totalDéplacement

for loop in range (totalDéplacement):
  action = int(input())
  
  if action == 1:
    déplacement[loop] = 2
  elif action == 2:
    déplacement[loop] = 1
  elif action == 3:
    déplacement[loop] = 3
  elif action == 4:
    déplacement[loop] = 5
  elif action == 5:
    déplacement[loop] = 4

for loop in range (totalDéplacement):
  print (déplacement[-loop - 1])
