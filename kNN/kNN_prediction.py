from geopy.distance import geodesic
from kNN import train_main

def index_to_string(p):
    if p == 4:
        return "preko 199 999"
    else:
        return "opseg izmedju " + str(p * 50000) + " i " + str((p + 1) * 50000 - 1)

args = [None]*7
print("Dobro dosli!")
print("Unesite koordinate nekretnine (u formatu 40.12345, 20.12345): ")
coords = str(input()).split(', ')
try:
    x1 = float(coords[0])
    x2 = float(coords[1])
    args[0] = round(geodesic([x1, x2], (44.8125449, 20.4612299)).km, 5)
except ValueError:
    print("Koordinate pogresno unesene!")
    exit(-1)
print("Unesite broj kvadrata nekretnine: ")
try:
    args[1] = int(input())
except ValueError:
    print("Kvadratura pogresno unesena!")
    exit(-1)
print("Unesite sprat nekretnine: ")
try:
    args[2] = int(input())
except ValueError:
    print("Sprat pogresno unesen!")
    exit(-1)
print("Unesite broj soba nekretnine: ")
try:
    args[3] = int(input())
except ValueError:
    print("Broj soba pogresno unesen!")
    exit(-1)
print("Unesite da li postoji parking nekretnine: (1 da, 0 ne)")
try:
    args[4] = int(input())
except ValueError:
    print("Parking pogresno unesen!")
    exit(-1)
print("Unesite da li postoji lift u zgradi: (1 da, 0 ne)")
try:
    args[5] = int(input())
except ValueError:
    print("Lift pogresno unesen!")
    exit(-1)
print("Unesite da li postoji terasa u nekretnini: (1 da, 0 ne)")
try:
    args[6] = int(input())
except ValueError:
    print("Terasa pogresno unesen!")
    exit(-1)

k_auto = True
k = 0
print("Unesite da li zelite da se K odredjuje automatski: (1 da, 0 ne)")
try:
    k_auto = int(input())
    if not k_auto:
        print("Unesite vrednost K parametra: ")
        try:
            k = int(input())
        except ValueError:
            print("K pogresno unesen!")
            exit(-1)
except ValueError:
    print("K_auto pogresno unesen!")
    exit(-1)

price_euc, price_man = train_main(args, k_auto, k)

print("Vasa nekretnina je procenjena na " + index_to_string(price_euc) + " evra po Euklidovom rastojanju!")
print("Vasa nekretnina je procenjena na " + index_to_string(price_man) + " evra po Menhetnovom rastojanju!")
