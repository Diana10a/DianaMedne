print("Vai tas ir pieprastits izdevums?")
izdevums = input("jā/nē:") #vai izdevums ir pieprasīts
print("Atbilde:",izdevums)

print("Vai tu esi students?")
students = input("jā/nē:") #vai cilveks ir students
print("Atbilde:",students)

print("vai tu esi personāls?")
personals = input("jā/nē:") #vai cilveks ir personals
("Atbilde:",personals)

print("Vai ir  visi izdevumi noditi?")
nodots = input("jā/nē:") #vai gramata ir nodota 
("Atbilde:",nodots)

if izdevums == "jā" and nodots =="jā": #izdevums ir pieprasīts
    print("grāmata izdota uz 2 dienām")
elif izdevums== "nē" and  students == "jā" and nodots == "jā": #izdevums nav pieprasīts un cilvēks ir students (izdevumi nodoti)
    print("grāmata izdota uz 14 dienām")
elif izdevums== "nē" and  personals == "jā" and nodots == "jā":#izdevums nav pieprasīts un cilvēks ir personāls (izdevumi nodoti)
    print("grāmata izdota uz 28 dienām")
elif nodots == "nē": # Izdevumis nav nodots
    print("grāmata netiek izdota")
elif students == "jā" and personals == "jā" or students == "nē" and personals == "nē": #Tika ievadīts ka nav students vai personāls, vai ka ir abi
    print("Kļūda, rakstiet vēlreiz!")
else: print("Kļūda, rakstiet vēlreiz!")#Netika ieraksīts jā vai nē