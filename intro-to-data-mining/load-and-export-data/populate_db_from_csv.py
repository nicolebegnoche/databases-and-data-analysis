# CS390Z - Introduction to Data Mining - Fall 2021
# Instructor: Thyago Mota
# Description: Activity 01 - CSV Data Load

import os
import mysql.connector 
import csv

# Set True to see status messages
verbose = True

# definitions/parameters
FOLDER = os.getcwd()
DATA_FOLDER = os.path.join(FOLDER, "..", "resources", "data")
CSV_FILE_NAME = 'employees.csv'

DB_NAME = 'hr'
DB_HOST = 'localhost'
DB_USER = os.getenv('db_user')
DB_PASS = os.getenv('db_pass')

def main():

    try:
        # TODO: connect to db
        db = mysql.connector.connect(
            host        = DB_HOST,
            database    = DB_NAME,
            user        = DB_USER,
            password    = DB_PASS,
            autocommit  = True
        )
        status('Database connection established.')

        # TODO: check if csv file exists
        filepath = os.path.join(DATA_FOLDER, CSV_FILE_NAME)

        if not os.path.exists(filepath):
            status(f"File not found: {filepath}")
            exit()
        else:
            status(f"Using data from {filepath}")

        # TODO: process csv file
        cursor = db.cursor()
        count = 0
        sql = "INSERT INTO Employees " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        with open(filepath, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                try:
                    cursor.execute(sql, row)
                    count += 1
                except Exception as e:
                    pass

        status(f"{count} rows inserted.")

    except Exception as error:
        print(error)


def status(msg):
    if verbose:
        print(msg)


if __name__ == "__main__":
    main()