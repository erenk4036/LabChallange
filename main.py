maxNumber = 250
aktuelleZahl = 2
primeNumberTrue = False
dateiname = "primeNumber.txt"

while aktuelleZahl <= maxNumber:
    primeNumberTrue = True
    testTeiler = 2

    while testTeiler < aktuelleZahl:
    
        if aktuelleZahl % testTeiler == 0:
            primeNumberTrue = False
        
        testTeiler += 1

    if primeNumberTrue == True:
        with open(dateiname, "a") as datei_object:
            print(aktuelleZahl, file=datei_object)
    
    aktuelleZahl += 1


        
