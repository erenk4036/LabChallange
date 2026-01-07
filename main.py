def finde_primzahlen(limit, dateiname):
    aktuelleZahl = 2

    while aktuelleZahl <= limit:
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



finde_primzahlen(250, "primeNumber.txt")


        
