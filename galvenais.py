
while True:
    print('1. Pieejamie dati \n2. Pievienot savus datus \n3. Agroplēve \n4. Apreiķini')
    print('* * * * * * * * * *')
    liet_ievade = int(input('Ievadiet ko jūs vēlaties darīt: ')) #pēc lietotāja ievadītā izsauc noteiktās funkcijas
    if liet_ievade == 1:
        info()
    elif liet_ievade == 2:
        lietotaja_darzeni()
    elif liet_ievade == 3:
        agropleve()
    elif liet_ievade == 4:
        apreikini()
    else:
        print('Nepareiza datu ievade! Lūdzu ievadiet skaitli no 1-4!')

    beigt = input('Vai jūs vēlaties beigt?(Ja/Ne): ')
    if beigt == 'Ja':
        print('Jauku stādīšanu! Uz redzēšanos!')
        exit()
    elif beigt == 'Ne':
        print('* * * * * * * * * *')
    else:
        print('Ievadiet Ja vai Ne!')
        beigt = input('Vai jūs vēlaties beigt?(Ja/Ne): ')