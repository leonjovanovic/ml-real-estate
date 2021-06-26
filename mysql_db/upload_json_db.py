import json

import mysql.connector

def transfer_to_db(file):
    cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='ml_real_estate')
    cursor = cnx.cursor()

    with open(file, 'r') as infile:
        result = json.load(infile)
        i = 0
        for r in result:
            add_listing = ("INSERT INTO real_estates (tip_nekretnine, tip_ponude, lokacija1, lokacija2, kvadratura, godina_izgradnje, povrsina_zemljista, sprat, ukupna_spratnost, uknjizenost, tip_grejanja, broj_soba, broj_kupatila, parking, lift, terasa, cena) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

            listing = (r["Tip nekretnine"], r["Tip ponude"], r["Lokacija1"], r["Lokacija2"], r["Kvadratura"], r["Godina izgradnje"], r["Povrsina zemljista"], r["Sprat"], r["Ukupna spratnost"], r["Uknjizenost"], r["Tip grejanja"], r["Broj soba"], r["Broj kupatila"], r["Parking"], r["Lift"], r["Terasa"], r["Cena"])

            cursor.execute(add_listing, listing)
            print(i)
            i += 1
    cnx.commit()
    cnx.close()

transfer_to_db("cleaned.json")