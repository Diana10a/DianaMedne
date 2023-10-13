import random
print('Metāmā kauliņa mešanas sacensības')
vards1 = input('Ievadiet pirmā spēlētāja vārdu: ')
vards2 = input('Ievadiet otrā spēlētāja vārdu: ')
metieni = int(input('Ievadiet metienu skaitu: '))
punkti1 = 0
punkti2 = 0
for i in range(metieni): #nosaka cik metieni
    kaulins1 = random.randint(1,6)#izvēlas metiena rezultatu
    kaulins2 = random.randint(1,6)
    punkti1+=kaulins1#skaita punktus
    punkti2+=kaulins2
    print(vards1 , i, '.metienā uzmeta', kaulins1)
    print(vards2 , i, '.metienā uzmeta', kaulins2)
print('Spēlētāja', vards1, 'punktu summa:', punkti1)
print('Spēlētāja', vards2, 'punktu summa:', punkti2)

if punkti1 > punkti2:
    print("Uzvarēja:", vards1)
elif punkti2 > punkti1:
    print("Uzvarēja:", vards2)
else:
    print("Neizšķirts")