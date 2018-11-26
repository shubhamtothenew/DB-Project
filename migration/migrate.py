# Import External libraries
import sqlite3

import re

import csv

# Import popup module
from .popup import popup


def migrate(source_table, destination_table):
    ''' This function migrate the data
        from one table to another '''

    # returns the rate
    rate = popup()

    # Connect to database
    connection = sqlite3.connect('employees.db')

    # Create cursor
    cursor = connection.cursor()

    # Drop and create table
    cursor.execute(""" DROP TABLE IF EXISTS {}""".format(destination_table))
    cursor.execute(""" CREATE TABLE {}(
                   name text, age integer,
                   location text, email text,
                   monthly_income integer)""".format(destination_table))



    row_inserted = 0
    row_not_inserted = 0
    unmigrated_list = []
    start = 0
    source_list =['initial']

    while len(source_list) != 0:
        cursor.execute("select * from {} limit {},100".format(source_table, start))
        source_list = cursor.fetchall()
        start += 100

        # Getting values from source_table and add it to the destination
        for list in source_list:
            if not re.findall("\w[a-zA-Z0-9_.]@[a-zA-Z]+\.[a-zA-Z]{2,}", str(list[4])):
                unmigrated_list.append(list)
                row_not_inserted += 1
            else:
                cursor.execute("INSERT INTO {} VALUES('{}',{},'{}','{}',{})".format(destination_table, list[0]
                                                                                    + ' '
                                                                                    + list[1],
                                                                                    list[2], list[3], list[4],
                                                                                    '{0:1.2f}'.format(list[5] * rate)))
                row_inserted += 1


    # Fetech all records
    cursor.execute("SELECT * FROM {}".format(destination_table))
    migrate_list = cursor.fetchall()

    for list in migrate_list:
        print('\033[92m{}'.format(list))

    print('\033[94mThe  total no of rows which is inserted :', row_inserted)
    print()
    print('The total no of rows which is not inserted :', row_not_inserted)

    with open('logger.csv', 'a') as csvFile:
         writer = csv.writer(csvFile)
         writer.writerows(unmigrated_list)

    for list in unmigrated_list:
         print('\033[31m{}'.format(list))

    # Close the and commit the connection
    connection.commit()
    connection.close()