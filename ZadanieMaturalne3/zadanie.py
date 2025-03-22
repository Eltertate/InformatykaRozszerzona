import math


#-----------------------------------------------------------------
#FUNKCJE DODATKOWE
#-----------------------------------------------------------------


def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def nwd(a,b):
    while a != b:
        if(a > b):
            a -= b
        else:
            b -= a
    return a





#-----------------------------------------------------------------
#ZADANIE 5
#-----------------------------------------------------------------

def zadanie5_1():
    array = [[],[],[],[],[],[],[],[],[],[],[],[]]
    with open("slowa.txt", 'r') as file:
        for line in file:
            if 1 <= len(line.strip()) <= 12:
                array[len(line.strip()) - 1].append(line)
    with open('wynik_5.txt', 'w',encoding='utf-8') as wynik:
        wynik.write("\tZADANIE I\n\n")
        for i in range(0,12):
            #print("Słowa", i+1 ,"literowe:" , len(array[i]))
            wynik.write(f"Słowa {i+1} literowe: {len(array[i])}\n")


def zadanie5_2():
    array = [[],[]]
    nowe = open("nowe.txt", "r")
    slowa = open("slowa.txt", "r")

    for line in nowe: array[0].append(line.strip())
    for line in slowa: array[1].append(line.strip())
    with open('wynik_5.txt', 'a',encoding='utf-8') as wynik:
        wynik.write("\n\n\tZADANIE II\n\n")
        for line in array[0]:
            wynik.write(f"{line}  {array[1].count(line)} {array[1].count(line[::-1])}\n")





#-----------------------------------------------------------------
#ZADANIE 6
#-----------------------------------------------------------------

def zadanie6_1():
    with open("dane_6.txt", "r") as file:
        pierwsze = 0
        with open('wyniki_6.txt', 'w',encoding='utf-8') as wynik:
            wynik.write("\tZADANIE III\n\n")
            for line in file:
                x = line.strip()
                if(czy_pierwsza(int(x))):
                    pierwsze += 1
            wynik.write(f"Liczb pierwszych: {pierwsze}\n")


def zadanie6_2():
    array = []
    with open("dane_6.txt","r") as file:
        for line in file:
            array.append(int(line.strip()))
        with open('wyniki_6.txt', 'a',encoding='utf-8') as wynik:
            wynik.write("\n\n\tZADANIE IV\n\n")
            wynik.write("Min:",min(array),"\nMax:",max(array))

def zadanie6_3():
    array_pierwsze = []
    
    with open("dane_6.txt", "r") as file:
        for line in file:
            if czy_pierwsza(int(line.strip())):
                array_pierwsze.append(int(line.strip()))
    with open('wyniki_6.txt', 'a',encoding='utf-8') as wynik: 
        wynik.write("\n\n\tZADANIE V\n") 
        for i in range(len(array_pierwsze) - 1): 
            if abs(array_pierwsze[i] - array_pierwsze[i + 1]) == 2:
                wynik.write(f"{array_pierwsze[i]} {array_pierwsze[i + 1]}")






#-----------------------------------------------------------------
#ZADANIE 4
#-----------------------------------------------------------------

def zadanie4_1():
    liczby = []
    with open("liczby.txt", "r") as file:
        for line in file:
            liczby.append(line.strip())
    
    with open("wyniki4.txt", "w") as wynik:
        wynik.write("\tZADANIE VI\n")
        for liczba in liczby:
            sprawdzamy = (list(map(int, liczba.split())))
            if(sprawdzamy[0] < sprawdzamy[1] < sprawdzamy[2]):
                wynik.write(f"{sprawdzamy[0]}{sprawdzamy[1]}{sprawdzamy[2]}")

def zadanie4_2():
    liczby = []
    NWD = []
    with open("liczby.txt", "r") as file:
        for line in file:
            liczby.append(line.strip())

    with open("wyniki4.txt", "a") as wynik:
        wynik.write("\n\n\tZADANIE VII\n")
        for liczba in liczby:
            sprawdzamy = (list(map(int, liczba.split())))
            NWD.append(nwd(nwd(sprawdzamy[0],sprawdzamy[1]),sprawdzamy[2]))
        wynik.write(sum(NWD))


def zadanie4_3():
    sumy = []
    with open("liczby.txt", "r") as file:
        for line in file:
            line = line.strip()
            suma = 0
            for digit in line:
                if(digit.isdigit()):
                    suma += int(digit)
            sumy.append(suma)
    with open("wyniki4.txt", "a") as wynik:
        wynik.write("\tZADANIE VII\n")
        wynik.write(f"Ogólnie sum: {len(sumy)}\n")
        wynik.write(f"Liczba 35 występuje {sumy.count(35)} razy\n")
        wynik.write(f"Najwiękza liczba {max(sumy)} występuje {sumy.count(max(sumy))} razy\n")




#WYNIKI ZADAŃ

zadanie5_1()
zadanie5_2()
zadanie6_1()
zadanie6_2()
zadanie6_3()
zadanie4_1()
zadanie4_2()
zadanie4_3()


