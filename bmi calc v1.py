import math
# kalkulator bmi
# wersja 1.0 z 30 listopada 
# mozna dodac sprawdzenie czy aby liczba jest dodatnia

# pobor danych - wzrost + waga
wzrost = float(raw_input('Podaj wzrost w centymetrach'))
waga = float(raw_input('Podaj wage w kilogramach'))

# wyswietlenie danych
print "Twoja waga to", w , "kg, a wzrost", h,"wynosi centymetrow."

# wzor na bmi -> masa/(wzrost^2)
# wzrost musi byc w metrach 

h2 = float(wzrost/100.0)
bmi = (waga /(h2**2))

#dodatkowy odstep
print

# komenta %.2f " % bmi pozwala wydrukowac .xf cyfr
print "Twoje bmi wynosi %.2f " % bmi, 

# %.2f" % 1.2399 
# dodatkowe wyjasnienie
if bmi < 16.0:
    print "Taka wartosc bmi oznacza wyglodzenie."
elif bmi > 16.0 and bmi <17:
    print "Taka wartosc bmi oznacza wychudzenie."
elif bmi > 17.0 and bmi <18.49:
    print "Taka wartosc bmi oznacza  niedowage."
elif bmi > 18.5 and bmi <24.99:
    print "Taka wartosc bmi oznacza wage prawidlowa."
elif bmi > 25.0 and bmi <29.99:
    print "Taka wartosc bmi oznacza  nadwage."
elif bmi > 30.0 and bmi <34.99:
    print "Taka wartosc bmi oznacza I stopien otylosci."
elif bmi > 35 and bmi <39.99:
    print "Taka wartosc bmi oznacza II stopiem otylosci."
elif bmi > 40:
    print "Taka wartosc bmi oznacza III stopiem otylosci."
    