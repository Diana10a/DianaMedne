import math
garumi = {
    '1':172,
    '2':185,
    '3':164,
    '4':184,
    '5':162,
    '6':164,
    '7':165,
    '8':167,
    '9':177,
    '10':184,
    '11':165,
    '12':180
}


izvele = '' 

while izvele != '5': #Ja ievada 4 programma beidzās
    izvele = input('Ko jūs vēlaties darīt? 1- redzēt visus datus 2- Pievienot datus 3- izdzēst datus 4- aprēķināt vidējo 5- iziet: ')
    if izvele == '1':
        for k , v in garumi.items():  #printē viņus stabā uz leju
            print(k+".", v, 'cm')
        print('---------------------------')
    elif izvele == '2':
        jauns_kartas_num = input('Ievadiet kārtas nummuru: ')
        jauns_garums = int(input('Ievadiet garumu: '))
        garumi.update({jauns_kartas_num:jauns_garums}) # pievieno ievadīto vārdnīcai
        for k , v in garumi.items(): 
            print(k+".", v, 'cm')
        print("Jūs pievienojāt: ", jauns_kartas_num, "kārtas nummuru, ", jauns_garums, "cm")
        print('---------------------------')
    elif izvele == '3':
        dzest = input("Kārtas skaitlis, kas tiks izdzēsts: ")
        garumi.pop(dzest) #izdzēš ievadīto  key un vērtību 
        for k , v in garumi.items(): 
            print(k+".", v, 'cm')
        print("Šis kārtas skaitlis tika izdzēsts: ", dzest)
        print('---------------------------')
    elif izvele == '4':
        videjais = sum(garumi.values())/len(garumi) #aprēķina vidējo agrumu
        print('Vidējais garums ir: ',math.ceil(videjais) ,'cm') #noapaļo vidējo garumu
        print('---------------------------')
    elif izvele == '5':
        exit() #iziet no programmas
    else:
        print("Ieraksti pareizo ciparu! 🥱") #Gadijumā, ja cilvēks ievada nepareizo ciparu
        print('---------------------------')

