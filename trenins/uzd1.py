#for cikls
for i in range(1,10):
    print(str(i) * i)
    
suns = int(input('Cik vecs ir suns?:'))
if suns <=2:
    suna_gadi = suns * 10.5
    print('Sunim ir ', suna_gadi,'cilvēka gadi')
if suns > 2:
    suna_gadi = suns * 4
    print('Sunim ir ', suna_gadi,'cilvēka gadi')
if suns <= 0:
    print('Sunim nevar būt 0 vai mazāk gadi')

for i in range(1,21):
    print(i,'.autobusa pietura')

for i in range(1,7):
    b = "*"
    print(b * i)
    for h in range(7,1,):
         print(b * h)

rinda = 7
for i in range(0,rinda):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")
for i in range(rinda, 0, -1):
    for j in range(0,i-1):
        print("*",end=" ")
    print("\r")
