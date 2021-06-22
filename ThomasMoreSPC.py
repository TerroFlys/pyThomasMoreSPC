#made by TerroFlys
#
#Thomas More studiepunt calculator
#
#
#Bij amount1 kan je 0 ingeven, dan stopt het pas als je bij input 0 ingeeft.

total = 0
prijs = 0
prijs_sp = 11.90
min_uur = 0
max_uur = 0
min_mp = 25
max_mp = 30
add = ""

amount1 = input("How many additions would you like?: ")

if int(amount1) != 0:
    for i in range(0, int(amount1)):
        add = input("input: ")
        total += int(add)
        i += 1
elif int(amount1) == 0:
    while(add != "0"):
        add = input("input: ")
        total += int(add)
        
prijs = total * prijs_sp
min_uur = total * min_mp
max_uur = total * max_mp

print("totaal studiepunten: " + str(total))
print("Dat zijn tussen de " + str(min_uur) + "u en " + str(max_uur) + "u.")
print("de prijs is: €" + str(prijs) + ".")
