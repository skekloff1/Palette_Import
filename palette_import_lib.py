"""
functions to read the a CSV file
and put it into a dictionary
"""

import csv

def read_palette_from_file(palette_filename):
    """
    read the palette from the csv file.
    Each row is a key and an RGB triple.  Make that RGB triple
    into a TUPLE and then put into a dictionary with the key.
    """
    pass


    my_dict = dict()


    with open (palette_filename, 'r') as f:


        csv_reader = csv.reader(f)

#TODO csv read_palette_from_file
        for row in csv_reader:


            key = int (row[0])
            value = (int (row[1]), int (row[2]), int (row[3]))

            my_dict[key] = value
    return my_dict
