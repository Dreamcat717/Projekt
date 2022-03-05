def zad2_2():
    wiek = int(input('Podaj wiek: '))
    pensja = float(input('Podaj pensję: '))
    if pensja < 0 and wiek < 18:
    		print('Nic nie zarabiasz złamasie i jesteś za mały!')
    elif pensja < 1800:
        return 0
    elif (pensja >=1800 and pensja < 2800) and wiek>=18:
        return 1
    elif (pensja >=2800 and pensja < 5000) and wiek>=18:
    		return 2
    elif (pensja >=5000 and pensja < 100000) and wiek>=18:
    		return 3

zad2_2()
