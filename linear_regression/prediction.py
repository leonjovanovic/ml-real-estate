import json
from geopy.distance import geodesic

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

with open("model_parameters.json", 'r') as infile:
    json_data = json.load(infile)
    parameters = json_data['parameters']
    mean = json_data['mean']
    std = json_data['std']

price = 0
i = 0
for param in parameters[0]:
    if i == 0:
        price += 1 * param
    else:
        price += ((args[i-1] - mean[i-1]) / std[i-1]) * param
    i += 1

print("Vasa nekretnina je procenjena na " + str(round(float(price), 2)) + " evra!")
