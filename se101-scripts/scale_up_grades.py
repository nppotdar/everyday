import os
import re
class_list = "./class-list.csv"

def start():
    csv_grade_reader = csv.reader( open(class_list), 'rb' )
    grade_dict = dict(for name in csv_grade_reader)
    csv_grade_reader.close()

    for line in content:
        grade_dict[ line.strip() ] = 0

    for root, sub_dir, files in os.walk('./reviews/'):
        for leaf_file in files:
            f1 = open(leaf_file, 'r')
            username_rex = re.compile(r"([a-z0-9]).*")
            rex1 = re.compile(r"(\d+.\d+)")
            marks = int( rex1.search( f1.readline() ).groups()[0] )
            username = username_rex.search( leaf_file ).groups()[0]
            grade_dict[username] = marks
            f1.close()
    
    csv_grade_writer = csv.writer( open(class_list), 'wb' )
    with open(class_list, 'wb') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, grade_dict.keys())
        w.writeheader()
        w.writerow(grade_dict)

start()
