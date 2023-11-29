import random as rand
import time

PRINT_SPEED = 0.00002

health = 100
namn= input("Andvändarnamn: ")

#while dialog not in (1, 2, 3):
    #print("Inte giltigt svar")
    #dialog = int(input(""))

level = input("Vilken svårhetsgrad vill du köra (lätt, mellansvårt, eller Svår): ")

while level not in ["lätt", "mellansvår", "svår"]:
    print("Inte giltigt försök igen")
    level = int(input("Vilken svårhetsgrad vill du köra (1, 2, eller 3): "))
    
print("Du valde")
if level=="lätt":
   print("Lätt svårighet")
elif level=="mellansvår":
    print("Mellansvår svårighet")
else:
    print("Svår svårighetsgrad")


while health>0:
    print(f"Hej {namn} Hur komm du hit")
    dialog_1=int(input("Vad svarar du 1. Vet inte 2.ingen aning 3. absolut inget vetande:"))
    while dialog_1 not in [1, 2, 3]:
        print("ogiltigt nummer")
        dialog_1=int(input("Vad svarar du 1. Vet inte 2.ingen aning 3. absolut inget vetande:"))
    print("Okej attans drattans, tur att jag äventyrsmästaren Bubbelius böökius kan hjälpa till.")
    print(f"följ med mig {namn}")
    print("Bubbelius Böökius blev uppäten av monstret")
    dialog_2=int(input("Vad gör du nu 1. Öppnar kistan 2. slå monstret med händerna 3. börja gråta"))
    while dialog_2 not in (1, 2,):
        print("Fel svar")
        dialog_2 = int(input("du börjar gråta och tappar 5 hp"))
        health = health-5