maxNumber = 250
aktuelleZahl = 2
primeNumberTrue = False

while aktuelleZahl <= maxNumber:
    primeNumberTrue = True
    testTeiler = 2

    while testTeiler < aktuelleZahl:
    
        if aktuelleZahl % testTeiler == 0:
            primeNumberTrue = False
        
        testTeiler += 1

    if primeNumberTrue == True:
        print(aktuelleZahl)
    
    aktuelleZahl += 1


        
