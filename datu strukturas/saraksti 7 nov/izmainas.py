saraksts = [2,5,9,4,6,3,2,8]
saraksts.append('Cepums')#pievieno beigās
print(saraksts)

#izmet no beigām
saraksts.pop()
print(saraksts)

saraksts.insert(3, 'Hello!') #ievieto 3. no kreisās
print(saraksts)

saraksts.remove(8) #izdēš norādīto vērtību
print (saraksts)

#funkcijas del pielietojums
tests = [1,2,3,4,5,6,7,8]
del tests[2] #izdēš vienu elementu
print(tests)

del tests[3:6]
print(tests) #izdzēš intervālu 

cipari = [1,2,3,4,5,6,7,8]
del cipari[2:7:2]
print(cipari)