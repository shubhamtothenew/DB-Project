# import external libraries
import argparse

# Import import and migrate modules
from migration import migrate
from Import import csv_read
# Main variable
if __name__ == '__main__':

    # Creation of parser
    parser = argparse.ArgumentParser(description='migration from one table to another')

    # Create optional command line arguments
    parser.add_argument('-option', help='import data from csv to table')
    parser.add_argument('-from', '--from_table', help='from table')
    parser.add_argument('-to', '--to_table', help='to table')

    args = parser.parse_args()

    # Calling functions based on conditions
    if args.option == 'migrate':
        # getting table names
        from_table = args.from_table
        to_table = args.to_table

        # calling migrate function
        migrate.migrate(from_table, to_table)
    elif args.option == 'import':
        import_table = args.to_table
        # Calling read_csv function
        csv_read.read_csv(import_table)
    else:
        print('please write the some valid inputs')
