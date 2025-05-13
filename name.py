class Student:
    def __init__(self,name,age,subject):
        self.name = name
        self.age = age
        self.subject = subject
    def student_details(self):
        print(f"Student Name:{self.name},Student Age:{self.age},Student Subject{self.subject}")

student1 = Student("Miminchandran",22,"Artificial intelligence and machine learning")
student1.student_details()
