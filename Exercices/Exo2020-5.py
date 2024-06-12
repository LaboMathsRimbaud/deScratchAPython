oui = int(input("Nombre de oui : "))
non = int(input("Nombre de non : "))
N = oui + non
if oui > non :
    p = oui / N * 100
    print("Bravo le oui !")
else :
    p = non / N * 100
    print("Bravo le non !")
print("score :", p, "%")
