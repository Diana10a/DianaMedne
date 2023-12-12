#piemērs sarakstsm ar dažādiem datu  tipiem
mixed_list = ['suns', 7.25, 8, True]
print(mixed_list[2])

#apgrizt skaitļu sarakstu
skaitli = [1,2,3,4,5,6,7,8,9,4,5,2,6]
apgriests = list(reversed(skaitli))
print(apgriests)

#filtrēt tikai pāra skaitļus
para_skaitli = [num for num in skaitli if num %2 == 0]
print(para_skaitli)

#iegust saraksta garumu
#garums = len(skaitli)

videjais = sum(skaitli)/len(skaitli)
print(videjais)

#atrast lielako un mazako skaitli, paradit uz ekrana
mazakais = min(skaitli)
print('Mazakais skaitlis: ',mazakais)
lielakais = max(skaitli)
print("Lielakais skaitlis: ",lielakais)

augli = ['apelsins', 'abols', 'banans', 'citrons', 'mango']
#atrast vardus, kas sakas ar konkretu burtu
varda_sakums = [vards for vards in augli if vards.startswith('a')]
print("Vārdi, kas sākās ar a", varda_sakums)