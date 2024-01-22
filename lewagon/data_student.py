from lewagon.student import Student

class DataStudent(Student):
    course = 'datascience'
    
    def __init__(self, name, age, batch):
        super().__init__(name, age)
        self.batch = batch