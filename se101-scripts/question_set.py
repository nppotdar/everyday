from __future__ import print_function
class ReviewSheet:
    def __init__(self, file_name):
        self.question_list = []
        self.comments = ""
        with open(file_name, 'r') as handle:
            reader = csv.DictReader(handle, ['name', 'weight', 'review'])
            for line in reader:
                self.question_list.append( Question(line['name'], line['weight'],line['review']) )
        
    def get_total_points():
        sum = 0
        for question in question_list:
            sum += question.get_net_points()
        return sum

    def get_max_points():
        return 4*len(question_list)


    def get_list():
        return question_list

    def add_comments(comments):
        self.comments = comments

    def to_file(filename):
        sum = total_points()
        print("Marks Obtained: " + sum, file=filename)
        
        for question in question_list:
            print("\n", file=filename)
            if question.get_points() != 3:
                print(question.get_name(), file=filename)
                print( "Points Deducted = " , (4*question.get_weight() - question.get_points()), file=filename)
                print( "Solution Overview:\n" , question.get_review(), file=filename )
        print(self.comments, file=filename)
    
