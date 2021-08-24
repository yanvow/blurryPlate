from Floutage import *
from Numéro_de_plaque import *

while True:
    choice = str(input("Tapez 1 pour flouter une image \nTapez 2 pour retouver la plaque d'immatricaltion d'une voiture \n"))
 
    if choice == "1":
        mainfloutage()
        break
    elif choice == "2":
        main_screen()
        break

        
