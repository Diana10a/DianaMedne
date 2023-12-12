a = int(input("Ievadi 1. skaitli:"))
b = int(input("Ievadi 2. skaitli:"))   # lietotājs ievada 2 skaitļus
print('Pirmais skaitlis ir:', a)
print('Pirmais skaitlis ir:', b)


if a > b:     #ja 1. skaitlis ir lielāsks par 2. tad atņem 
    c = a - b
    print('Skaitļu starpība ir',c) 
elif a< b :    #ja 1. skaitlis ir mazāks par 2. tad saskaita
    c = a+b   
    print('Skaitļu summa ir',c)