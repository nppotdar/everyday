from __future__ import print_function
from review_class import ReviewSheet
import os
course_name = "cs260"
assignment_name = "hw3"
review_dir = "../reviews/"

attr_csv = "./attr.csv"

def start():
    if not os.path.exists(review_dir):
        os.makedirs(review_dir)
    skip_flag = False
    i = 0

    for root, sub_dir, files in os.walk('.'):
        for username in sub_dir:
            i = i+1
            print('%d)Begin grading for user  %s '%(i, username))
            if os.path.exists(review_dir+username+assignment_name):
                if skip_flag:
                    continue
                ch = raw_input("review exists, OVERWRITE?[y/(n)]")
                if ch !='y':
                    ch = raw_input("Skip till non-entry found?[(y)/n]")
                    if ch != 'n':
                        skip_flag = True
                    continue
            else:
                skip_flag = False
            for sub_root, sub_dir_2, sub_files in os.walk(username):
                if "%s.pdf"%assignment_name in sub_files:
                    os.system( "xdg-open " + username +"/"+ assignment_name + ".pdf" )
                else:
                    for leaf_file in sub_files:
                        ch = raw_input("open file %s [y/(n)]?"%leaf_file)
                        if ch == 'y':
                            os.system( "xdg-open " + username +"/"+ leaf_file )
            sol_sheet = ReviewSheet(attr_csv)
                
            for question in sol_sheet.get_question_list():
                question.set_points(int(raw_input("\tpoints for "+ question.get_name()+ "range(0-3): ")))
                if question.get_points() !=3:
                    ip = raw_input("Comments?[(n)]")
                    if len(ip)>3:
                        question.set_review(ip)
                print(question.get_net_points())
            selection = raw_input("Put up overall comments? [y/n]: ")
            if selection == 'y':
                sol_sheet.add_comments( raw_input("Paste additional comments:\n") )
            sol_sheet.to_file( review_dir+username+"."+assignment_name )

start()
