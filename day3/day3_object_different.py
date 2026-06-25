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
        
    def __str__(self):
        return f"Student: {self.name}, Sex: {self.sex}, Grade: {self.grade}"
    
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students
        
    def __str__(self):
        group_of_students = ""
        for student_id in self.students:
            this_student = self.students[student_id]
            group_of_students += this_student.__str__()
        return f"School: {self.name}, Students: {group_of_students}"
    
if __name__ == "__main__":
    local_copy_of_database_file = { 1: Student("Jody", "M", 10), 2: Student("Jane", "F", 11) }
    
    print(f"Student 1: {local_copy_of_database_file[1].name}, Sex: {local_copy_of_database_file[1].sex}, Grade: {local_copy_of_database_file[1].grade}")
    
    local_copy_of_database_file[1].sex_change("F")
    print(f"Student 1: {local_copy_of_database_file[1].name}, Sex: {local_copy_of_database_file[1].sex}, Grade: {local_copy_of_database_file[1].grade}")
    
    my_school = School("My School", local_copy_of_database_file)
    print(my_school)
    
    student_name = input("Enter student name: ")
    student_sex = input("Enter student sex: ")
    student_grade = int(input("Enter student grade: "))
    
    student1 = Student(student_name, student_sex, student_grade)
    
    student2 = Student(input("Enter student name: "), input("Enter student sex: "), int(input("Enter student grade: ")))
    
    print(f"Student 1: {student1.name}, Sex: {student1.sex}, Grade: {student1.grade}")
    print(f"Student 2: {student2.name}, Sex: {student2.sex}, Grade: {student2.grade}")
    student1.new_grade(int(input("Enter new grade for student 1: ")))
    
    #try:
    #   something
    #catch (some error):
    #    do this when error occurs