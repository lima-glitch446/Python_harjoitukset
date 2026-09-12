vuosiluku= int(input("Anna vuosiluku: "))

if vuosi % 4 == 0:

  print("Vuosi ei ole karkausvuosi")

elif vuosi % 200 == 0:
   print("Vuosi on karkausvuosi")

else:
   print("Vuosi ei ole karkuvuosi")

