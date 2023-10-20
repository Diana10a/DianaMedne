pasazieru_sk = int(input('Cik ir pasažieri? : ')) 
if pasazieru_sk > 3: #cilvēki ir vairāk par 3
    print('Taksī nevar būt vairāk par 3 pasažieriem.')
elif pasazieru_sk < 3 or pasazieru_sk == 3 : #cilvēki ir 3 vai mazāk
     laiks = int(input('Cik ir laiks? : '))
     if laiks < 6 and laiks < 21 :
            cena_km = 0.77 #nakts cena
     elif laiks > 5 and laiks < 20 :
            cena_km = 0.37 #dienas cena
     else:
            exit("Ievadi pareizus datus.")

vieta = input('Vai taksis ir stāvietā?(j/n) : ')
if vieta == 'j':
     noligsanas_cena = 2 #ir stāvvietā
elif vieta == 'n':
     noligsanas_cena = 4.50  #nav stāvvietā
else: 
      exit("Ievadi pareizus datus.")

gaidisana = int(input('Cik būs gaidīšanas laiks? : '))
gaidisanas_cena = gaidisana * 0.15

cels = int(input('Cik km jābrauc? : '))
cela_cena = cels * cena_km 
beigu_cena = noligsanas_cena + gaidisanas_cena + cela_cena

print('____________________')
print('Laiks :', laiks)
print('Atrodas stavvieta :', vieta)
print('Gaidīšana :', gaidisana, 'min')
print('Nobrauktie km :', cels, 'km')
print('____________________')
print('')
print('Cena kilometrā :', cena_km)
print('Nobrauktie km :', cels)
print('cela_cena :', cela_cena)
print('Noligsanas cena/ Izsaukuma cena :', noligsanas_cena)
print('Gaidīšana :', laiks)
print('Gaidīšanas cena minūtē : 0,15')
print('Gaidīšanas kopsumma:', gaidisanas_cena)
print('_____________________')
print('')
print('Beigu summa:', beigu_cena)

