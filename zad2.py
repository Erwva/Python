try:
ocjena=float(input("Unesite ocjenu izmedju 0.0 i 1.0"))
except:
print("Pogresan unos, unesite ocjenu izmedju 0.0 i 1.0")
exit()

if ocjena >= 0.9:
k_ocj = "A"
elif ocjena >= 0.8:
k_ocj = "B"
elif ocjena >= 0.7:
k_ocj ="C"
elif ocjena >= 0.6:
k_ocj "D"
else :
k_ocj= "F"

print("Kategorija ocjene je: "{k_ocj})
