# CS390Z - Introduction to Data Mining - Fall 2021
# Instructor: Thyago Mota
# Student: Nicole Weickert
# Description: Homework 01 - XLSX Data Load

'''
## Goal:  To illustrate how to perform a typical XLSX parse to JSON

In this assignment you are NOT allowed to use any external library to read the given XLSX file directly. 
Instead, unzip the XLSX file and extract the following XML files: sharedStrings.xml and sheet1.xml. 

Use the shared strings file to create a list of all strings referenced in the document. You should then read sheet1.xml 
and extract all of its rows. Note that the content of each cell maps to the index in the shared string list. 
Finally, your parser should then saved the extracted information in json, using the format below: 
    {"name": "AALERUD Katrine", "noc": "Norway", "discipline": "Cycling Road"}, 
    {"name": "ABAD Nestor", "noc": "Spain", "discipline": "Artistic Gymnastics"}, 
    {"name": "ABAGNALE Giovanni", "noc": "Italy", "discipline": "Rowing"},
'''

import os, shutil, json
from zipfile import ZipFile
from bs4 import BeautifulSoup

# definitions/parameters
DATA_FOLDER =       os.path.join("..", "resources", "data")
OUTPUT_FOLDER =     os.path.join('.', 'output')
XLSX_FILE =         os.path.join(DATA_FOLDER, "athletes.xlsx")
SHARED_STRINGS =    os.path.join("xl", "sharedStrings.xml")
SHEET1 =            os.path.join("xl", "worksheets", "sheet1.xml")
OUTPUT_FILE =       os.path.join(OUTPUT_FOLDER ,"xlsx_to_json.json")


def main():

    # returns the xml from the files
    strings_xml, rows_xml = extract_xml(SHARED_STRINGS, SHEET1)

    # extract strings from sharedStrings.xml and extract rows from sheet1.xml
    strings = list(strings_xml.stripped_strings)
    rows = rows_xml.find_all('row')

    # uses the numeric row values from sheet1 and returns the matching string from shared_strings
    row_values = lambda row : [strings[int(z.string)] for z in row.children]

    # use first row strings (column headers) as keys in the dictionary
    column_headings = row_values(rows[0])

    # create list of dictionaries from the remaining rows
    file_contents = []
    for row in rows[1:]:
        file_contents.append(dict(zip(column_headings, row_values(row))))

    # save to json
    if not os.path.exists(OUTPUT_FOLDER): os.mkdir(OUTPUT_FOLDER)
    with open(OUTPUT_FILE, "w") as outfile:
        json.dump(file_contents, outfile, indent=1)
        outfile.close()


def extract_xml(*files):                         # unzips  XLSX_FILE and returns the xml

    # # create a temporary folder if it doesn't already exist
    tmp = os.path.join("temp_folder")
    if not os.path.exists(tmp): os.mkdir(tmp)

    # unzip xlsx file if it exists (Silent overwrite if data already exists in temp folder)
    if file_exists(file := XLSX_FILE):
        with ZipFile(file, 'r') as zipObj:
            zipObj.extractall(tmp)

    # extract xml from files
    xml = []
    for file in files:
        if file_exists(filepath := os.path.join(tmp, file)):
            xml.append((BeautifulSoup(open(filepath), 'xml')))

    # delete temporary folder and return xml
    shutil.rmtree(tmp)
    return xml
        

def file_exists(filepath):                      # Return True if file exists; else quit with message
    if not os.path.exists(filepath):
        print(f"Error: '{filepath}' not found.")
        quit()
    else:
        return True


if __name__ == "__main__":
    main()
    print("processed finished")


# List comprehension gets weird fast, and I'll probably forget what this expression means, so... note to self:
'''     rows[0] in...                print...                                        result...

row         first line of xml           [row]                                           [<row r="1" spans="1:3" x14ac:dyDescent="0.25"><c r="A1" t="s"><v>11314</v></c><c r="B1" t="s"><v>11315</v></c><c r="C1" t="s"><v>11316</v></c></row>]

.children:  all child tags              [z for z in row.children]                       [<c r="A1" t="s"><v>11314</v></c>, <c r="B1" t="s"><v>11315</v></c>, <c r="C1" t="s"><v>11316</v></c>]

.string     the strings of child tags   [z.string for z in row.children]                ['11314', '11315', '11316']

cast to integer to use as index         [int(z.string) for z in row.children]           [11314, 11315, 11316]

use as index for strings list           [strings[int(z.string)] for z in row.children]  ['Name', 'NOC', 'Discipline']
                                           
                                        ↪ equivalent to  [strings[11314], strings[11315], strings[11316]]
'''