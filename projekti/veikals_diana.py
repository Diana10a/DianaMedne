veikals = input('Kādā veikalā jūs iepērkaties?(rimi/maxima/elvi/lats/vesko):')
saraksts = int(input('Cik preces ir jūsu sarakstā?'))
beigu_cena =0
saraksts = 'n'
while saraksts == "n":
    prece = input('Kā sauc preci?: ')
    precu_vieniba = int(input('Cik vienības jūs pirksiet?: '))
    if precu_vieniba == 0:
        exit
    cena = int(input('Cik prece maksā?:'))
    kopcena = precu_vieniba * cena
    saraksts = input('Vai ir nopirkst viss kas ir sarakstā?(j/n): ')
    if  saraksts == 'j':
        beigu_cena += kopcena
        print(beigu_cena)

if veikals == 'lats':
    atlaide = 0.30
if veikals == 'rimi':
    karte = input('Vai jums ir rimi karte?(j/n):')
    if karte == "j":
        atlaide = 0.40
    else:
        atlaide = 0
if veikals == 'maxima':
    karte = input('Vai jums ir maximas karte?(j/n):')
    if karte == "j":
        atlaide = 0.50
    else:
        atlaide = 0.20
if veikals == 'elvi':
    if saraksts >= 3:
        atlaide = 0.30
    else:
        atlaide = 0
if veikals == 'vesko':
    atlaide = 2

summa = beigu_cena * atlaide
print('summa:',summa)

 

        