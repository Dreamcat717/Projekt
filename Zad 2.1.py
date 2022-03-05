def zad2_1():
    kwota = float(input('Podaj ile masz dziengów: '))
    if kwota <= 0:
        return ('Nie masz kasy!')
    else:
        kurs = 4.49
        return round(kwota/kurs, 2)