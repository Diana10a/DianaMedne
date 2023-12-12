a = int(input("Ievadi 1. skaitli:"))
b = int(input("Ievadi 2. skaitli:"))  #lietotajs ieavad skaitļus

if a*b > 0:   #programma pārbauda vai skaitļu reizinājums ir pozitīvs
     c = a+b   
     print("Skaitļu summa :",c)
elif a*b <0:    #programma pārbauda vai skaitļu reizinājums ir negatīvs
     print('Skaitlis ir negatīvs, rakstiet vēlreiz')   
     a = int(input("Ievadi 1. skaitli:"))
     b = int(input("Ievadi 2. skaitli:"))

   
