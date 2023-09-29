import math
import random 

rlr = float(input("Ievadiet riņķa līnijas rādiusu:"))#rlr = riņķa līnijas rādius
print(rlr)

rlg = (rlr*2*math.pi)#rlg = riņķa līnijas garums
print("riņķa līnijas garums:","%.2f" %rlg )

rll = (math.pi*math.pow(rlr,2))#rll = riņķa līnijas laukums
print("Riņķa līnijas laukums:","%.2f" %rll  )

kv = int(input("Ievadiet taisnleņķa trijstūra pirmās katetes garumu:"))#kv = katete viens
print(kv)

kd = int(input("Ievadiet taisnleņķa trijstūra otrās katetes garumu:"))#kd = katete divi
print(kd)

thg = (math.pow(kv,2)+math.pow(kd,2)) #thg = trijstūra hipotenūzas garums
thg= (math.sqrt(thg))
print("Taisnleņķa trijstūra hipotenūzas garums:","%.2f" %thg)

print("Gadījuma skaitlis no 0-1:", random.random())