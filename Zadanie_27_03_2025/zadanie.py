def nwd(a,b):
    while a != b:
        if(a > b):
            a -= b
        else:
            b -= a
    return a

def zadanie1():
    print("\n\n\t ZADANIE I \n")
    with open("cyfry.txt", 'r') as file:
        ilosc = 0 
        with open('zadanie4.txt', 'w',encoding='utf-8') as wynik:
            for line in file:
                line = int(line.strip())  
                if line % 2 == 0:
                    ilosc += 1
            wynik.write(f"a) Liczb parzystych: {ilosc}\n")

            file.seek(0)  
            
            array = [[], []]
            for line in file:
                array[0].append(line.strip()) 
                suma = sum(int(i) for i in line.strip())  
                array[1].append(suma)
            
            wynik.write(f"b) Najmniejsza liczba: {array[0][array[1].index(min(array[1]))]} z wartością sumy {min(array[1])}\n")
            wynik.write(f"   Największa liczba: {array[0][array[1].index(max(array[1]))]} z wartością sumy {max(array[1])}\n")

            ciag = []
            for liczba in array[0]:
                if all(liczba[i] < liczba[i + 1] for i in range(len(liczba) - 1)):
                    ciag.append(liczba)
            wynik.write(f"c) Liczby tworzące ciąg rosnący: {ciag}\n")


def zadanie2():
    print("\n\n\t ZADANIE II \n")
    with open("napisy.txt", 'r') as file:
        parz_dlug = 0
        with open('zadanie4_1.txt', 'w',encoding='utf-8') as wynik:
            for line in file:
                line = line.strip()
                if(len(line) % 2 == 0):
                    parz_dlug += 1
            wynik.write(f"a) Napisów o parzystej długości: {parz_dlug}\n")

            file.seek(0)

            rowneZiJ = 0
            for line in file:
                line = line.strip()              
                if line.count("0") == line.count("1"):
                    rowneZiJ += 1
            wynik.write(f"b) Napisów które zawierają taką samą liczbę zer i jedynek: {rowneZiJ}\n")
            
            file.seek(0)

            sameZera = 0
            sameJedynki = 0
            for line in file:
                line = line.strip()              
                if(line.count("0") == 0):
                    sameJedynki += 1
                elif(line.count("1") == 0):
                    sameZera += 1
            wynik.write(f"c) Liczby składające się z samych zer: {sameZera}\n")
            wynik.write(f"   Liczby składające się z samych jedynek: {sameJedynki}\n")

            file.seek(0)

            wynik.write("d) Liczb: ")
            for k in range(2,17):
                licznik = 0
                file.seek(0)
                for line in file:
                    line = line.strip()              
                    if len(line) == k:
                        licznik += 1
                wynik.write(f"\t{k}-znakowych: {licznik}\n")

def zadanie3():
    print("\n\n\t ZADANIE III \n")
    with open("PARY_LICZB.txt", 'r') as file:
        licznik = 0
        with open('ZADANIE5.txt', 'w',encoding='utf-8') as wynik:
            for line in file:
                line = line.strip()
                if(int(line.split(" ")[0]) % int(line.split(" ")[1]) == 0):
                    licznik += 1
                elif(int(line.split(" ")[1]) % int(line.split(" ")[0]) == 0):
                    licznik += 1
            wynik.write(f"a) Wierszy w których jedna z liczb jest wielokrotnością drugiej: {licznik}\n")

            file.seek(0)

            licznik = 0
            for line in file:
                line = line.strip()
                if(nwd(int(line.split(" ")[0]), int(line.split(" ")[1])) == 1):
                    licznik += 1
            wynik.write(f"b) Liczb których NWD jest równe 1: {licznik}\n")

            file.seek(0)

            licznik = 0
            for line in file:
                line = line.strip()
                suma1 = sum(int(i) for i in (line.split(" ")[0]))  
                suma2 = sum(int(i) for i in (line.split(" ")[1])) 

                if(suma1 == suma2):
                    licznik += 1 
            wynik.write(f"c) Wierszy gdzie suma cyfr 1 liczby jest równa sumie cyfr 2 liczby: {licznik}\n")

zadanie1()
zadanie2()
zadanie3()