# import large_database_files
# python is an object oriented programming language. What does that mean?

class Student:
    def __init__(self, name, sex, grade):
        self.name = name
        self.sex = sex
        self.grade = grade
        
    def new_grade(self, new_grade):
        self.grade = (self.grade + new_grade) / 2
        
    def sex_change(self, new_sex):
        self.sex = new_sex
        
    def new_name(self, new_name):
        self.name = new_name
        

        
        
if __name__ == "__main__":
    student1 = Student("Jody", "M", 10)
    student2 = Student("Jane", "F", 11)
    
    print(f"Student 1: {student1.name}, Sex: {student1.sex}, Grade: {student1.grade}")
    print(f"Student 2: {student2.name}, Sex: {student2.sex}, Grade: {student2.grade}")
    
    student1.new_grade(12)
    print(f"Student 1: {student1.name}, Sex: {student1.sex}, Grade: {student1.grade}")
    
    