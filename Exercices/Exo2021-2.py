fichier = input("Nom du fichier :")
p = 0
print("Téléchargement de", fichier)
for i in range(100) :
    print(p, "%")
    p = p + 1
print("Téléchargement terminé.")
