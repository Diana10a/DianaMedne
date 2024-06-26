darzeni = { 
    'burkans': 5,
    'sipols': 7,
    'kaposts': 25,
    'kartupelis': 25,
    'kaposts': 25,
    'gurkis': 250,
    'tomats': 65,
    'kirbis': 100,
    'kiploks': 10,
    'paprika': 40,
    'rabarbers': 130,
    'kukuruza': 20,
    'brokolis': 45,
    'bietes': 9,
    'rediss': 3,
    'dilles': 15,
    'skabene': 10
}

print('Laipni lūgti dārzniecības programmā!')
print('* * * * * * * * * *')
try:
    vagas_daudzums = int(input('Ievadiet vagu daudzumu: '))
    vagas_garums = int(input('Ievadiet vagu garumu(cm): '))
    vagas_platums = int(input('Ievadiet vagu platumu(cm): '))
except ValueError:
    print("Ievadiet pareizus datus!")
    vagas_daudzums = int(input('Ievadiet vagu daudzumu: '))
    vagas_garums = int(input('Ievadiet vagu garumu(cm): '))
    vagas_platums = int(input('Ievadiet vagu platumu(cm): '))
vagas_laukums = vagas_garums*vagas_platums*vagas_daudzums #aprēķina vagas laukumu cm^2(lai var vēlāk izmantot aprēķinos)
print('* * * * * * * * * *')


def info():
    print('* * * * * * * * * *')
    print('Šie ir pieejamie dati: ')
    for i in range(len(darzeni)):#parāda uz konsoles visu dārzeņu nosakumus un datus
        atslega = list(darzeni.keys())[i]
        print(atslega + ':', darzeni[atslega])
    print('* * * * * * * * * *')

def lietotaja_darzeni():
    print('* * * * * * * * * *')
    darzena_nosaukums = input('Ievadiet dārzeņa nosaukumu: ')
    try:
        darzena_attalums = int(input('Ievadiet dārzeņu attālumu: '))
    except ValueError:
        print("Ievadiet pareizus datus!")
        darzena_attalums = int(input('Ievadiet dārzeņu attālumu: '))
    
    darzeni[darzena_nosaukums] = darzena_attalums  #pievieno lietotāja ievadīto dārzeni un tā datus sarakstam 
    print('* * * * * * * * * *')

def agropleve(): 
    print('* * * * * * * * * *')
    agropleve_vajaga = input('Vai jums vajaga agroplēvi?(Ja/Ne): ') 
    if agropleve_vajaga == 'Ja':
        vaga_metros = vagas_laukums/100  
        pleves_maksa = vaga_metros*0.3 #aprēķina agroplēves maksu
        print('Agroplēves izmaksa: ', pleves_maksa, '€')

        agropleve_instrukcija = input('Vai jums vajaga instrukciju agroplēvei?(Ja/Ne): ')
        if agropleve_instrukcija == 'Ja':
            print('* * * * * * * * * *')
            print("1. Vispirms sagatavo dobes formu.\n2. Sagatavo augsni.\n3. Uzklāj agroplēvi visas domes izmērā. \n4. Novieto stādus paradzētajās vietās.\n5. Šajās vietās veic krustenisku iegriezumu.\n6. Izrakt stādam paradzēto bedri un iestādi stādu. \n7. Stādu kārtīgi aplaistīt. \n8. Uz agroplēvēs uzklāt ~5 cm biezu mulčas kārtu.\n9. Rūpēties atbilstoši stāda vajadzībām. ")
        elif agropleve_instrukcija == 'Ne':
            print('* * * * * * * * * *')

    elif agropleve_vajaga == 'Ne':
        print('Priecīgu ravēšanu!')
        print('* * * * * * * * * *')

def apreikini():
    kurs_darzenis = input('Kuru dārzeni jūs stādīsiet? (Ievadiet bez garumzīmēm un ar mazajiem burtiem nominatīvā): ')
    try:
        darzenu_apreikins = vagas_laukums/darzeni[kurs_darzenis]#aprēķina cik daudz dārzeņus var iestādīt vagā
    except KeyError:
        print("Šis dārzenis nav sarakstā!")
        kurs_darzenis = input('Kuru dārzeni jūs stādīsiet? (Ievadiet bez garumzīmēm un ar mazajiem burtiem nominatīvā): ')
        darzenu_apreikins = vagas_laukums/darzeni[kurs_darzenis]
    apalots_apreikins = round(darzenu_apreikins, 1)
    print('Jūs varēsiet iestādīt', apalots_apreikins, 'gab.')
    tirgus = input('Vai jūs plānojat pārdot '+kurs_darzenis+' Rīgas tirgū? (Ja/Ne): ')
    if tirgus == 'Ja':
        tirgus_cena = float(input('Kāda ir šobrīdējā cena: '))
        print('Jūs pārdodot visu iegūsiet', apalots_apreikins*tirgus_cena, '€')
    elif tirgus == 'Ne':
        ()
    print('* * * * * * * * * *')

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