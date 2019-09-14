'''
Else statements will be activated if the if or elif statements dont get activated
Elif statements are priority if statements the first one to be activated is the code what will be activated and it wont continue going through the other elifs or else
'''
a = 1 # Sets up
b = 2
c = 3
d = 4

if a != 1:
  print("A doesnt equal 1.")
elif b != 2:
  print("B doesnt equal 2.")
else:
  print("Hit the else part.") # Activate this code
  
  

if a != 1:
  print("A doesnt equal 1.")
elif b == 2:
  print("B equal 2.") # Activate this code.
else:
  print("Hit the else part.")
