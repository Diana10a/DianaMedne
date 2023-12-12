import math
cena_linoleja = int(input('Cik maksā linolejs kvadrātmetrā?: '))
platums = int(input('Cik plats ir rullis?(m): '))
garums = int(input('Cik ir garums telpai?: '))
telpa = int(input('Cik plata ir telpa metros?: '))
turpinat = ''
cena = ''
t_platiba = telpa* garums
vajadzigais = (telpa/platums)*garums
while turpinat != '4':
    print("Telpas platums metros: ", telpa)
    print('Telpas garums metros: ', garums)
    print("Telpas kopējā platība: ", t_platiba, "metros")
    print("Būs nepieciešami: ", math.ceil(vajadzigais), " metri linoleja")
    izmaksas = math.ceil(math.sqrt(vajadzigais)) * cena_linoleja
    print("Tik izmaksās vajadzīgais linolejs:  ",izmaksas, 'euro')

    paliek_pari = math.ceil(math.sqrt(vajadzigais)) - math.sqrt(vajadzigais)
    print("Tik linoleja paliek pāri:", round(paliek_pari, 2))
    veikals = input("Kur iepirksieties?: ")


    print("-----------------")
    print("Veikals:",veikals,  "\nIzmaksas: ", izmaksas, "euro \nPlatums: ", telpa, '\nGarums: ', garums,"\nPlatība: ", t_platiba)
    print ("-----------------")
    apaksklajs = input("Vai vēlaties ieklāt apakšklāju? (1- Nē, 0 - Jā): ")
    if apaksklajs == '0':
        cena = int(input('Ievadat cenu: '))
        print("Tad kopā viss maksās: ", (math.ceil(math.sqrt(vajadzigais))*cena) + izmaksas)
    if apaksklajs == 1:
        print('ok')
    turpinat == input('Vai vēlaties turpināt? 3-jā 4-nē: ')
    if turpinat == '4':
        exit()