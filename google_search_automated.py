# Reads the first column of a csv file and searches the contents of each cell on google
# Released Under the MIT License 
# Created By Agneeth Mazumdar 

import webbrowser
import csv 

def read_csv():

    search_terms = []

    with open('list_of_stuff.csv', 'rb') as search_terms_data:
        csv_search_terms_data = csv.reader(search_terms_data)

        for row in csv_search_terms_data:
            search_terms.append(row[0])

    return search_terms 

def open_links(search_terms): 

    search_these = search_terms 
    start_of_url = "https://www.google.com/search?sclient=psy-ab&hl=en&site=webhp&btnG=Search&q="

    for index, value in enumerate(search_these):
        webbrowser.open(start_of_url + search_these[index])

    return None 

def main(): 

    search_terms = read_csv()
    open_links(search_terms)

if __name__ == "__main__":
    main()
