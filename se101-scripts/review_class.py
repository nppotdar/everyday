from __future__ import print_function
from question import Question
import csv
import math

max_marks = 60.0
class ReviewSheet:
    def __init__(self, file_name):
        self.question_list = []
        self.comments = ""
        self.x = 0
        sum = 0
        with open(file_name, 'r') as handle:
            reader = csv.DictReader(handle, ['name', 'weight'])
            reader.next()
            for line in reader:
                self.question_list.append( Question(line['name'], int(line['weight'])) )
                sum += int(line['weight'])
        self.x = max_marks/float(sum*3)
        print("NOTE: Grade point value = "+ str(self.x))
        
    def get_total_points(self):
        sum = 0
        for question in self.question_list:
            sum += question.get_net_points()
        print(sum)
        return sum

    def get_max_points(self):
        return sum(question.get_weight()*3 for question in self.question_list)


    def get_question_list(self):
        return self.question_list
    
    def add_comments(self, comments):
        self.comments = comments

    def to_file(self, filename):
        file_obj = open(filename, 'w')
        sum = self.get_total_points()
        print("Marks Obtained: %d"%(math.ceil(sum*self.x)), file=file_obj)
        
        for question in self.question_list:
            if question.get_points() != 3:
                print("\n", file=file_obj)
                print(question.get_name(), file=file_obj)
                print( "Points Deducted = " , (3*question.get_weight() - question.get_net_points())*self.x, "/", (3*question.get_weight()*self.x), file=file_obj)
                print( "Review:\n" , question.get_review(), file=file_obj )
        print("\nADDITIONAL COMMENTS: \n", self.comments, file=file_obj)
    
