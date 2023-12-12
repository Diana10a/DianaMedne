#izveido vārdnīcu ar datiem  par automašīnu
auto = {
    'Krāsa':'Zils',
    'Zīmols':"Audi",
    'Gads':2004,
    'Modelis':'xc90'
}
dati = input('Ievadiet zīmolu, lai pārbaudītu:')
if dati == auto['Zīmols']:
    print('Ir vārdnīcā😁')
elif dati == auto.values():#?
    print('Auto ir kā vērtība')
else:
    print("Auto nav😥")
