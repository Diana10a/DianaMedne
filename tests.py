def lietotaja_darzeni():
    print('* * * * * * * * * *')
    darzena_nosaukums = input('Ievadiet dārzeņa nosaukumu: ')
    try:
        darzena_attalums = int(input('Ievadiet dārzeņu attālumu: '))
    except ValueError:
        print("Ievadiet pareizus datus!")
        darzena_attalums = int(input('Ievadiet dārzeņu attālumu: '))
    
    darzeni[darzena_nosaukums] = darzena_attalums  #pievieno lietotāja ievadīto dārzeni un tā datus sarakstam 
    print('* * * * * * * * * *')
