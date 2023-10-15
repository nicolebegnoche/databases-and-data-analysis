# CS390Z - Introduction to Data Mining - Fall 2021
# Instructor: Thyago Mota
# Description: Activity 03 - Quotes API

'''
Goal: To illustrate how to perform a typical web service consumption using a RESTful API
Retreive data from a web API and save in .json format
'''
from pprint import pprint
import os, json, requests

# definitions/parameters
QUOTES_API_URL =    'http://quotes.rest/qod.json?api_key=XXX'
DATA_FOLDER =       os.path.join('..', 'resources', 'data')
OUTPUT_FOLDER =     os.path.join('.', 'output')
QUOTES_API_KEY =    os.path.join(DATA_FOLDER, 'quotes_api_key.txt')
OUTPUT_FILE =       os.path.join(OUTPUT_FOLDER,'quoteXs.json')

# debug mode files
fail =     os.path.join(DATA_FOLDER, 'quotes_api_failure.json')
success =  os.path.join(DATA_FOLDER, 'quotes_api_success.json')
success2 = os.path.join(DATA_FOLDER, 'quotes_api_success2.json')
debug_mode = False

def main():

    # get data
    raw_json = call_api(fail)

    # return a quote if api call was successful, otherwise throw error
    # new_quote = parse(raw_json)

    # # load prior quotes
    # quotes = read_file(OUTPUT_FILE) or []

    # # combine old + new (but no duplicates)
    # quotes.insert(0, new_quote)

    # # write combo to file
    # write_file(OUTPUT_FILE)



def call_api(test_file=None):

    # by default, call the api with private API key
    if test_file is None:
        url = QUOTES_API_URL + read_file(QUOTES_API_KEY)
        request = requests.get(url)
        if request.status_code == 200:
            return request
        else:
            code = request.status_code
            reason = request.reason
        
    # use a local file instead
    else:
        request = read_file(test_file) 
        if "success" in request:
            return request
        else:
            code = request['error']
            reason = request['error']['message']

        
    error = f"\nError {code}: {reason}"
    quit()


def parse(raw_json):
    x = raw_json
    print(x)

    print("status code:  ", x.status_code)
    print("text:         ", x.text)
    print("reason:       ", x.reason)
    print("content:      ", x.content)



    quit()

    request_status = list(raw_json.keys())[0]   # returns either 'error' or 'success'
    print(request_status)


    return None


def read_file(file):
    filetype = file.split('.')[-1]
    with open(file) as f:
        if filetype == "json":
            return json.load(f)
        else:
            return f.read()

def write_file(file):
    pass


def file_exists(file):
    if not os.path.exists(file):
        print(f"Error: could not find {file}")
        quit()


if __name__ == "__main__":
    main()
    print("\nProcess finished")