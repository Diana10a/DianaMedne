telefons = {
    'Jānis': 3432743,
    'Rita': 54526356,
    'Anna': 52345345
}
#Jānim ir 2 telefona nummuri
telefons.update({'Jānis':11111111})
print ('Šis ir Ritas nr', telefons['Rita'])
print ('Šis ir Jāņa nr', telefons['Jānis'])
print ('Šis ir Annas nr', telefons['Anna'])

#izveido vardnicu ar atslegu virkni un fromkeys() metodi
#vārdnīca nenorādot ierakstu vērtības
kk = ('viens', 'divi', 'trīs')
dd = dict.fromkeys(kk)
print(dd)
val = 0 #šī vērtība būs visai vārdnīcai
dd = dict.fromkeys(kk,val)
print(dd)

#izveidot vārnīcu, kas satur sarakstu 
valstis = {
    'Somija':['Helsinki', 'Tamperi', 'Rovaniemi'],
    'Norvēģija': ['Oslo', 'Bergena', 'Trumse'],
    'Dānija': ['Kopenhāgena', 'Ronne', 'Odense']
}

for atslega, vertiba in valstis.items():
    for i in vertiba:
        print("{}: {}".format(atslega,i))
    print('😉😉😉')