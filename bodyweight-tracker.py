# Released under MIT License 
# Created By Agneeth Mazumdar

# Allows you to keep track of your weight without opening a spreadsheet everyday 

import datetime
import csv

def calculate_date():

    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d")

    return current_date

def get_weight():

    weight = raw_input("Enter in today's weight \n")

    return weight

def append_to_csv(date, weight):

    date_and_weight = [date, weight]

    with open('weight_log.csv', 'a') as weight_data:
        csv_weight_data = csv.writer(weight_data)
        csv_weight_data.writerow(date_and_weight)
    
def main():

    present_date = calculate_date()
    present_weight = get_weight()    

    append_to_csv(present_date, present_weight)

if __name__ == "__main__":
    main()
