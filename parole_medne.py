lietotajs = 'skolens'
parole = '2222'
summa = 0


ievaditais_lietotajs = input('Lūdzu, ievadiet savu lietotājvārdu:')
ievaditais_parole = input('Lūdzu, ievadiet savu paroli:')
if ievaditais_lietotajs == lietotajs and ievaditais_parole == parole:
    print("Pieslēgšanās veiksmīga")
for i in range(5,0):
    while   i!=5:
        ievaditais_lietotajs = input('Lūdzu, ievadiet savu lietotājvārdu:')
        ievaditais_parole = input('Lūdzu, ievadiet savu paroli:')
        if ievaditais_lietotajs == lietotajs and ievaditais_parole == parole:#parliecinās vai ievadīti pareizi dati
            print('Pieslēgšanās veiksmīga!')
        else :
            print('Ir atlikuši vel',i, 'mēģinājumi')


pirmais_sk = int(input('Ievadiet 1. veselo skaitli:'))
otrais_sk = int(input('Ievadiet 2. veselo skaitli:'))

while pirmais_sk!= 'stop':
    sum = sum(i for i in range(pirmais_sk, otrais_sk + 1))#izreiķina summu
    print('Veselu secīgi pieaugušo skaitļu no 2 līdz 4 summa ir',sum)
print('Programmas beigas!')
