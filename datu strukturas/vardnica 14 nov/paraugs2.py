valstis = {
    'Somija':['Helsinki', 'Tamperi', 'Rovaniemi','Kemijarvi','Jyvsakyle'],
    'Norvēģija': ['Oslo', 'Bergena', 'Trumse','Molde','Arendāla'],
    'Dānija': ['Kopenhāgena', 'Ronne', 'Odense', 'Esbjerga','Aarhus']
}

#izdrukāt vārdnīcas elementus, piekļūstot vārdnīcā konkrētai atslēgai
for i in valstis['Dānija']:
    print(i)
for i in valstis['Somija']:
    print(i)
for i in valstis['Norvēģija']:
    print(i)

#izdrukāt pirmās 3 pilsētas Somijas
print(valstis['Somija'][:3])
#Iegūt pēdējās 2 pilsētas Norvēģijas
print(valstis['Norvēģija'][3:6]) #vai[-2:]
# visas somijas iznemot  3 pedejas
print(valstis['Somija'][:-3])
#iegūt no otrās līdz piektajai Dānijai
print(valstis['Dānija'][1:6])