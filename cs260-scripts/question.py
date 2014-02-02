class Question:
    
    def __init__(self, name, weight):
        self.name = name
        self.points = 0
        self.weight = weight
        self.review = ""

    def set_points(self, points):
        self.points = points
    
    def set_review(self, review):
        self.review = review

    def get_weight(self):
        return self.weight

    def get_points(self):
        return self.points

    def get_net_points(self):
        return self.points*self.weight

    def get_name(self):
        return self.name

    def get_review(self):
        return self.review

    
