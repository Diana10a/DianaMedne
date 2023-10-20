'''atbilde = 'j'
while atbilde == 'j':
    print('Nekusties!')
    atbilde = input('Vai briesmonis ir draudzīgs?(j/n)')
print('Bēdz prom')'''

#pārbaudīt vai lietotājs prot reizināt līdz 7
#programma atkārto darbību līdz brīdim, kad uzdoti visi 12 jautājumi
reiz = 7
for i in range(1,13): #cikla mainīgais no 1 - 12
    print('Cik ir',i,'*',reiz,'?')
    minejums = input()
    if minejums == 'stop':
        break #pārtrauc programmu
    if minejums == 'izlaist':
        print('Tiek izlaists')
        continue #izlaiž 1 jautājumu un turpina tālāk
    atb = i * reiz
    if int(minejums)== atb:
        print('Pareizi!')
    else:
        print('Nē, tas ir',atb)
