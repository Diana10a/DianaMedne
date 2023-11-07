'''izviedot 3 sarakstus:lietotājs pats norādīs, cik elementus
likt sarakstā.
>Pirmā un otrā sarakstā vērtības ievada lietotājs
>Trešā saraksta vērtības iegūst apvienojot pirmos 2
>Katra saraksta saturu glīti parādīt uz ekrāna '''

pirmais_saraksts = []
otrais_saraksts = []
tresais_saraksts = []

elementi_viens = int(input('Cik vērtības jūs gribēsiet pirmajā sarakstā?:'))
for i in range(0,elementi_viens):
    vertiba = input('Ievadiet vērtību:')
    pirmais_saraksts.append(vertiba)
print('Pirmais saraksts',pirmais_saraksts)

elementi_divi = int(input('Cik vērtības jūs gribēsiet pirmajā sarakstā?:'))
for i in range(0,elementi_divi):
    vertiba = input('Ievadiet vērtību:')
    otrais_saraksts.append(vertiba)
print('Otrais saraksts',otrais_saraksts)

tresais_saraksts = pirmais_saraksts + otrais_saraksts
print('Trešais saraksts',tresais_saraksts)
    