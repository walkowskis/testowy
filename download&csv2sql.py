# import csv
# import sqlite3
# import urllib.request
#
# # url = "http://ec.europa.eu/growth/tools-databases/cosing/pdf/COSING_Ingredients-Fragrance%20Inventory_v2.csv"
# # urllib.request.urlretrieve(url, "cosing.csv")
#
# # Connect to the database
# connection = sqlite3.connect('cosing.db')
# cursor = connection.cursor()
#
# # Drop and create the table
# cursor.execute('DROP TABLE IF EXISTS cosing')
# cursor.execute('CREATE TABLE cosing (Ref_No, INCI_name, INN, PhEur, CAS_No, EC_No, Chem_Name, Restriction, Function, Update_Date)')
# connection.commit()
#
# # Load the CSV file into CSV reader
# with open('cosing.csv', encoding="utf8") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     all(next(csv_file) for i in range(9))
#     for t in csv_reader:
#         cursor.execute('INSERT INTO cosing VALUES (?,?,?,?,?,?,?,?,?,?)', t)
#
# # Close the csv file, commit changes, and close the connection
# csv_file.close()
# connection.commit()
# connection.close()
#
#
#

import csv
import sqlite3
import urllib.request

# Download CSV fle
url = "http://ec.europa.eu/growth/tools-databases/cosing/pdf/COSING_Ingredients-Fragrance%20Inventory_v2.csv"
urllib.request.urlretrieve(url, "testowa.csv")

# Connect to the database
connection = sqlite3.connect('cosing.db')
cursor = connection.cursor()

# Drop and create the table
cursor.execute('DROP TABLE IF EXISTS cosing')
cursor.execute('CREATE TABLE cosing (Ref_No, INCI_name, INN, PhEur, CAS_No, EC_No, Chem_Name, Restriction, Function, Update_Date)')
connection.commit()

# Load the CSV file into CSV reader
with open('testowa.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    all(next(csv_file) for i in range(9))
    for t in csv_reader:
        try:
            cursor.execute('INSERT INTO cosing VALUES (?,?,?,?,?,?,?,?,?,?)', t)
        except sqlite3.ProgrammingError as e:
            pass

# Close the csv file, commit changes, and close the connection
csv_file.close()
connection.commit()
connection.close()
