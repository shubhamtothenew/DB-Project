# Import External libraries
import sqlite3

import csv


def read_csv(import_table):
    ''' This function reads the csv file
    and create a table'''

    # Connect to database
    connection = sqlite3.connect('employees.db')

    # Create cursor
    cursor = connection.cursor()

    # Drop table if already exist
    cursor.execute('''DROP TABLE IF EXISTS {}'''.format(import_table))

    # Create table
    cursor.execute("""CREATE TABLE {}(
                  firstname text, lastname text,
                  age integer, location text,
                  email text, monthly_income integer
                  )""".format(import_table))

    # Open and read csv
    path = '/home/shubham/sampledata.csv'
    file = open(path, "r")
    file_reader = csv.DictReader(file)

    # Iterate csv
    imported_rows = 0
    for csv_line in file_reader:
        cursor.execute("INSERT INTO {} VALUES('{}','{}',{},'{}','{}',{})".format(import_table,csv_line['firstname'],
                                                                                 csv_line['lastname'],int(csv_line['age']),
                                                                                 csv_line['city'],csv_line['email'],
                                                                                 int(csv_line['salary'])))
        imported_rows += 1
    cursor.execute("select * from {}".format(import_table))

    # Fetch and print the record from database
    import_list = cursor.fetchall()
    for list in import_list:
        print('\033[92m{}'.format(list))
    print('\033[94mTotal no of rows which is imported is :', imported_rows)

    # Close and commit the connection
    connection.commit()
    connection.close()
    file.close()
