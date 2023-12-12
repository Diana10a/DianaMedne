kontakti = {
    'vards': [],
    'nummurs': []
}

kontakti['vards'] =['Karlsons', 'Vinnijs pūks', 'Pepija garzeķe','Sprīdītis']
kontakti['nummurs'] =['790291059', '53859184', '05395483', '45295848']

print('1 - drukāt kontaktus uz ekrāna', '\t2 - pievienot kontaktu', '\t3 - izdzēst kontaktu', '\t4 - iziet')
izvele = input('Ko Jūs vēlaties darīt?')



if izvele == '1':
    print(izvele, "Jūs uzspiedāt taustiņu 1: jūsu kontakti uz ekrāna:")
    print(kontakti)
    print('---------------------')
elif izvele == '2':
    print(izvele, "Jūs uzspiedāt taustiņu 2: pievienot jaunu kontaktu:")
    jauns_vards = input('Ievadiet kontaktpersonas vārdu:')
    jauns_num = input('Ievadiet kontaktpersonas numuru:')
    kontakti['vards'].append(jauns_vards)
    kontakti['nummurs'].append(jauns_num)
    print(kontakti)
    print('---------------------')
elif izvele == '3':
    print(izvele, "Jūs uzspiedāt taustiņu 3: izdzēst kontaktu:")
    izdzesamais = input('Kuru kontaktu Jūs vēlaties izdzēst?')
    del kontakti[izdzesamais]
    print(kontakti)
else:
    close()


