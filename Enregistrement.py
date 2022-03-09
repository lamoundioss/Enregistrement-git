

import random
import mysql.connector
from mysqlx import SqlStatement


mysbd = mysql.connector.connect(
    host = "localhost",
    user = "lamoundioss",
    password = "test_123",
    database = "Stock_Piece"
)

cursor = mysbd.cursor()

# res = "INSERT INTO Piece(categorie, date, id_key) VALUES( %s, %s, %s)"


# for i in range(1,21):
#     tab = [("renault", "2012-12-15", random.randint(1, 20))]
#     cursor.executemany(res, tab)
#     mysbd.commit()


# ress = "INSERT INTO Reference(id_reference, prix) VALUES(%s, %s)"
# for j in range(20):
#     tabb = [(j,random.randint(200, 500)) ]
#     cursor.executemany(ress, tabb)
#     mysbd.commit()


# tab1 = ["Auris", "Avensis", "Aygo", "Focus","Galaxy", "Bronco"]
# Tab = ["Citroen", "Cevrelet", "Mercedes", "BMW","Ford", "Toyota"]
# res = "INSERT INTO Vehicule(id_vehicule, modele, annee, marque) VALUES( %s, %s, %s, %s)"
# for i in range(5,21):
#     tab = [(i, random.choice(tab1), random.randint(2002, 2022), random.choice(Tab))]
#     cursor.executemany(res, tab)
#     mysbd.commit()
keita = []
Res = "SELECT id_vehicule FROM Vehicule"
cursor.execute(Res)
Result = cursor.fetchall()
for secke in Result:
    keita.append(secke[0])
print(keita)

Keita = []
res = "SELECT id_piece FROM Piece"
cursor.execute(Res)
Result = cursor.fetchall()
for secke in Result:
    Keita.append(secke[0])
print(Keita)

ress = "INSERT INTO Correspondance(id_piece, id_vehicule) VALUES( %s, %s)"
for i in range(1,21):
    tab = [(random.choice(Keita), random.choice(keita))]
    cursor.executemany(ress, tab)
    mysbd.commit()

cursor.close()