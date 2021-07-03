import json
from geopy.distance import geodesic
#print(round(geodesic((44.77064370511346, 20.551312396301267), (44.8125449, 20.4612299)).km, 5))
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='ml_real_estate')
cursor = cnx.cursor()

with open('table_before_coding.json', 'r') as infile:
    table = json.load(infile)

with open('location2_coords.json', 'r') as infile:
    locations = json.load(infile)
for loc in locations:
    for row in table:
        if row['lokacija2'] is not None:
            row['lokacija2'] = round(geodesic(loc[row['lokacija2']], (44.8125449, 20.4612299)).km, 5)

        add_listing = ("INSERT INTO flats_for_sale (lokacija2, kvadratura, godina_izgradnje, povrsina_zemljista, sprat, ukupna_spratnost, uknjizenost, tip_grejanja, broj_soba, broj_kupatila, parking, lift, terasa, cena) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        listing = (row["lokacija2"], row["kvadratura"], row["godina_izgradnje"], row["povrsina_zemljista"], row["sprat"], row["ukupna_spratnost"], row["uknjizenost"], row["tip_grejanja"], row["broj_soba"], row["broj_kupatila"], row["parking"], row["lift"], row["terasa"], row["cena"])
        cursor.execute(add_listing, listing)
cnx.commit()
cnx.close()

with open('table_after_coding.json', 'w') as output_file:
    output_file.write(
        '[' +
        json.dumps(table, indent=4) +
        ']\n')
