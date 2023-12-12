#izveidot tukšu vārdnīcu
vardnica = {
    "a":1,
    "b":2
}

ievade_atsl = input('Ievadiet atslēgu:')
ievade_vert = input('Ievadiet vērtību:')

#pārbauda lietotāja ievadi un rediģē vārdnīcu
if ievade_atsl in vardnica:
    vardnica[ievade_atsl] = ievade_vert
    print('Vārdnīca ir atjaunota!')
else:
    vardnica[ievade_atsl]=ievade_vert
    print('Jauns vārds tika pievienots vārdnīcai!')

print('Atjaunotā vārdnīca',vardnica)