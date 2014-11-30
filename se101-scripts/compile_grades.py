import os
import re
import csv
class_list = "./class-list.csv"
grade_list = "./grade-list.csv"

def start():
    grade_dict = {}
    
    with open(class_list, 'rb') as f:
        for line in f:
            grade_dict[ line.strip()  ] = -1
    
    print len(grade_dict)
    for root, sub_dir, files in os.walk('./reviews/'):
        for leaf_file in files:
            f1 = open( "./reviews/" + leaf_file, 'r')
            username_rex = re.compile(r"([a-z0-9]*).*")
            rex1 = re.compile(r"(\d+)")
            marks = int( rex1.search( f1.readline() ).groups()[0] )
            username = username_rex.search( leaf_file ).groups()[0]
            grade_dict[username.strip()] = marks
    
    headers= ("name", "grade")
    with open(grade_list, 'wb') as f:  
        w = csv.DictWriter(f, fieldnames=headers)
        for k, v in grade_dict.items():
            w.writerow({"name": k, "grade":v})
    

start()
