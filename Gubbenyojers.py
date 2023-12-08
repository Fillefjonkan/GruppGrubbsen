import random as rand
strength=20
health=10
vapen=("empty")

print("Hej välkommen till Dungeon Bubbles")
namn= input("Andvändarnamn: ")
while len(namn) >8:
    namn= input("Andvändarnamn som inte är för långt: ")

while health > 0:  
    
    Stats=(f"Hälsa,{health}, styrka, {strength}")
    print(f"Hej {namn} Hur komm du hit")

    dialog_1=int(input("Vad svarar du 1. Vet inte 2.ingen aning 3. absolut inget vetande:"))
    while dialog_1 not in [1, 2, 3]:
        print("ogiltigt nummer")
        dialog_1=int(input("Vad svarar du 1. Vet inte 2.ingen aning 3. absolut inget vetande:"))
    
    print("Okej attans drattans, tur att jag äventyrsmästaren Bubbelius böökius kan hjälpa till.")
    print(f"följ med mig {namn}")
    print("Bubbelius Böökius blev uppäten av monstret")
    
    dialog_2=int(input("Vad gör du nu 1. Öppnar kistan 2. slå monstret med händerna 3. börja gråta"))
    while dialog_2 not in [1,2,3]:
        dialog_2=int(input("Vad gör du nu 1. Öppnar kistan 2. slå monstret med händerna 3. börja gråta"))


    if dialog_2 == 1:
        print("Du öppnade kistan och fann ett ruttetsvärd och ett bandage som läker dig")
        health = health + 20
        random=rand.randint(-20,15)
        strength = strength + random 
        vapen_1="ruttet svärd"
        vapen=vapen_1
        print("Här är din statistik")
        print(vapen, Stats)
    elif dialog_2 == 2:
        print("Du är usel på att slå och monstret slår dig men du blir starkare")
        print("Du öppnade ändå kistan och fann ett ruttetsvärd")
        health=health-5
        strength=strength+4
        vapen_1="ruttet svärd"
        vapen=vapen_1
        print("Här är din statistik")
        print(vapen, Stats)
    elif dialog_2 == 3:
        print("Monstret blir känslosam och bestämmer sig själv för att inte skada dig")
        print("Du öppnade ändå kistan och fann ett ruttetsvärd")
        strength=strength-4
        vapen_1="ruttet svärd"
        vapen=vapen_1
        print("Här är din statistik")
        print(vapen, Stats)
    break


while health>0:
    dialog_4 = int(input("Vill du slå tillbaka mot monstret med svärdet du har? 1. ja 2. nej 3. börja gråta"))
    while dialog_4 not in [1, 2, 3]:
        dialog_4 = int(input("Vill du slå tillbaka mot monstret med svärdet du har? 1. ja 2. 3. nej börja gråta"))

    if dialog_4 == 1:
        print("Du skadade monstret då du var starkare än den tölpen")

    elif dialog_4==2:
        print("Vågade du inte? Monstret bryr sig inte och nitar dig rejält, du dör omedelbums")
        health=0
        break

    elif dialog_4==3:
        print("Monstret bryr sig inte och slår dig till döds")
        health=0
        strength=strength-10
    break


while health>0:
    dialog_5=int(input("Monstret begick sjävlmord på grund av depression och nu står du framför två identisk dörrar. 1. gå in i vänstra rummet 2. gå in i högra rummet 3. gå in i prinsessborgen rakt fram"))
    while dialog_5 not in [1, 2, 3]:
        dialog_5=int(input("Du besegrade monstret utan tvekan och nu står du framför två identisk dörrar och en prinsessborg 1. gå in i vänstra rummet 2. gå in i högra rummet 3. gå in i prinsessborgen rakt fram"))

    if dialog_5 == 1:
        print("Du gick in ett rum med spikar som dödar dig direkt")
        health=0
        break

    elif dialog_5 == 2:
        dialog_6=int(input("Du möttes av ett stort monster 1. slå monstret med ditt svärd 2. vänta på döden"))
        while dialog_6 not in [1]:
             print("Fel svar")
             dialog_6=int(input("Du möttes av ett stort monster 1. slå monstret med ditt svärd 2. vänta på döden"))
        print("Monstret krossade dig totalt till döds")
        health=0
    else:
        dialog_7=int(input("du gick in i borgen där en kista väntar 1. öppna kistan"))
    while dialog_7 not in [1]:
        print("Fel svar")
        dialog_7=int(input("du gick in i borgen där en kista väntar 1. öppna kistan"))
    break


while health>0:   
    
    print("Kistan innehöll ett silversvärd som stärker dig och även ett bandage som läker din hälsa")
    strength=strength+10
    health=health+10
    vapen_2 = "Silversvärd"
    vapen=vapen_2
    dialog_8=int(input("Hur vill du gå till väga nu 1. röda dörren till vänster 2. gröna dörren till höger 3. gula dörren rakt fram"))
    while dialog_8 not in [1, 2, 3]:
        print("Inte ett alternativ")
        dialog_8=int(input("Hur vill du gå till väga nu 1. röda dörren till vänster 2. gröna dörren till höger 3. gula dörren rakt fram"))
    utval=("Gyllene svärd", "Bubbelsvärdet", "OPsvärdet")
    vapen_3=rand.choice(utval)
    print(f"du fann en kista som innehöll {vapen_3} och en brandsläckare")
    vapen=vapen_3
    strength=strength+2
    print("Med ditt nya svärd borde du kunna besegra vilket monster som helst")

    monster_1=rand.randint(10,18) 
    if monster_1>strength:
        print("Monstret är starkt och får dig att tappa 10 hp")
        health=health-10
    break

while health>0:
    if monster_1<strength:
       print("monstret är starkt men du är starkare därför besegrade du eländet och blev starkare")
       strength=strength+2
    monster=rand.randint(7,12) 
    monster_1 = monster
    if monster_1>strength:
        print("Monstret besegrade dig du var inte tillräckligt stark")
    break



while health>0:
    dialog_9=int(input("Grattis du besegrade monstret och fick hans svärd 1. gå vidare 2. öppna inventory"))
    vapen_4="Excalibur"
    vapen=vapen_4
    while dialog_9 not in [1,2]:
        dialog_9=int(input("Grattis du besegrade monstret och fick hans svärd 1. gå vidare 2. öppna inventory"))
    while dialog_9 not in [1]:
        print(vapen, Stats)
        dialog_9=int(input(" 1. gå vidare 2. öppna inventory"))
    while dialog_9 not in [1]:
        dialog_9=int(input(" 1. gå vidare "))
    if dialog_9==1:
        dialog_10=int(input("Nu kommer det svåra valet går du in i 1. Rummet med en döskalle på 2. rummet men festliga bubblor"))
        while dialog_10 not in [1, 2]:
            dialog_10=int(input("Nu kommer det svåra valet går du in i 1. Rummet med en döskalle på 2. rummet men festliga bubblor"))
    if dialog_10==1:
        print("""Du gick in i Det läskiga rummet men som tur var det bara en kista där inne
              Onej när du öppnar kistan kommer ett jätte stort monster fram ut ur kistan för att bita dig
              dags att slåss""")
        dialog_12=int(input("Du ser en lucka i taket 1. spring mot luckan 2. Slåss mot monstret"))
        while dialog_12 not in [1, 2]:
            dialog_12=int(input("Du ser en lucka i taket 1. spring mot luckan  2. Slåss mot monstret"))
        slump=rand.randint(1,2)
        if dialog_12==1:
            
            if slump ==1:
                print("""Du springer mot luckan men precis innan du kryper ut
                      Monstret greppar tag i dig och sliter dig i bitar""")
                break
        
            elif slump==2:
                print("""Du springer mot luckan
                      Och du hinner nästan men monstret greppar tag i ditt ben
                      du lyckas glida ur och fly monstret""")
        elif dialog_12==2:
            print("Vad tänkte du monstret var mycket starkare än dig du dog")
            health=0
    elif dialog_10==2:
        print("""Du gick in i ett bubbligt rum
              du kände dig avslappnad tills du ser Bubblius Bökkius resa sig
              han skriker på dig eftersom du inte ens tittade ifall han var död påriktigt
              du bryter ihop och storgråter
              som gräddet på moset utmanar han dig på en duel
              du tackar ja för du är nervös""")
        Bubbelius_Böökius=30
        if Bubbelius_Böökius>strength:
            print("""Han är starkare än du trodde och du blir besegrad
                  Du ber om nåd men hans känslor är korrupta""")
            health=0
            break
        else:
            dialog_11=int(input("""Du Vann
                  Han ber om nåd
                  1. Låt han leva 2. döda han"""))
            while dialog_11 not in [1, 2]:
                dialog_11=int(input("""Du Vann
                  Han ber om nåd
                  1. Låt han leva 2. döda han"""))
            if dialog_11==1:
                print("Du lät han leva och han ger dig en bamsekram")
            elif dialog_11==2:
                print("Du dödade han aja baja")
    break
if health>0:
    print("Grattis du klarade det")
else:
    print("Game over")
        

        
    
    
    