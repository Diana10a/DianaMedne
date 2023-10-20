print('Aritmētiskās progresijas elementu aprēķins')
pirmais = int(input('Ievadiet pirmo locekli!'))
difrence = int(input('Ievadiet diferenci!'))
skaits = int(input('Ievadiet elemtu skaitu!'))

for i in range(skaits):
    sum=pirmais+i*difrence
    print(i+1,". lockelis:\t",sum)