class Student :

    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
        self.mark=[]
        print(f'Your name is {self.name} Your age {self.age} Your city {self.city}')

    def add_mark(self,mark):
        self.mark.append(mark)

    def get_all_marks(self):
        return self.mark

    def calc_avg(self):
        return sum(self.mark)/len(self.mark)