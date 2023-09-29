print("Programmu izstrādāja: Evelīna, Diāna")
print("Laukuma aprēķins ģeometriskām figūrām")

print("\t****")
a_mala = float(input("Ievadiet malas A garumu:"))
print(a_mala)
print("Malas A garums:", a_mala/1)

print("\t****")
b_mala = int(input("Ievadiet B malas garumu:"))
print(b_mala)
print("Malas B garums:", b_mala/1)

print("\t****")
augstums = int(input("Ievadiet augstumu"))
print(augstums)
print("Augstums:", augstums/1)

print("Laukums trijstūrim:", (a_mala*augstums)/2)
print("Laukums trapecei", ((a_mala+b_mala)/2)*augstums)
print("Laukums paralelogramam:", (a_mala*augstums)/1)

print("\t****")
print("Paldies!")
