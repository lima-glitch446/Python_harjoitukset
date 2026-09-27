#----------YKSINKERTAINEN TOISTORAKENNE------#

#Alustetaan muuttujat
hinta = 5
kolikot = 0

while True: 
    #Päivitetään ehto
    kolikot += 1
    print("Annettu", kolikot, "kolikkoa.")

    #Tarkistetaan ehto
    if kolikot == hinta:
        break

print("kiitos näkemiin!")
