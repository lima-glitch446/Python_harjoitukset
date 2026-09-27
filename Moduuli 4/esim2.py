komento = input("Anna uusi komento: ")


while komento != "lopeta":
    if komento == "MAYDAY":
        break
    print("Suoritetaan komento:", komento)
    komento = input("Anna uusi komento: ")

print("Ohlelma loppuu")