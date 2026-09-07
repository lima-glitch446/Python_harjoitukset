leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

luodit_yht = leiviskat * 20 * 32 + naulat * 32 + luodit

grammat = luodit_yht * 13.3
kilot = int(grammat // 1000)
grammat = grammat % 1000

print(f"Massa on {kilot} kg ja {grammat:.2f} g")

