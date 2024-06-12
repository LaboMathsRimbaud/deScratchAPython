jour = int(input("Quel jour est-on (nombre entier) ? "))
mois = int(input("De quel mois (de 1 à 12)? "))
if mois < 12 :
    reste = 12 - mois
    print(reste, "mois avant Noël.")
else :
    reste = 25 - jour
    if reste > 0 :
        print(reste, "jour(s) avant Noël.")
    else :
        print("C'est Noël !")
