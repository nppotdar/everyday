import csv
import sys

def parse_for_id(csv_name):
    reader =  csv.DictReader( open(csv_name), delimiter = ",")

    headers = []
    for row in reader:
        id_string = ""
        if len(headers) == 0:
            headers = row.keys()
        for header in headers:
            if header == "Username":
                id_string = id_string + "  -  " + row[header]
            elif header == "First Name":
                id_string = id_string + "  -  " + row[header]
            elif header == "Last Name":
                id_string = id_string + "  -  " + row[header]
            elif len(row[header]) > 0:
                print header+ " = "+row[header] + "\n"
        print id_string
        print "\n"
        print "\n---------------------------------------------------------------------------\n"


if __name__ == "__main__":
    parse_for_id(sys.argv[1])
