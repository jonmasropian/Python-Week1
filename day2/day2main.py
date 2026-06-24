print("Welcome to class!")
print("Today we will be doing some simple drills")
print('Using a \"student intake\" script') # only the truly dedicated will see the "problem" here.

def student_intake():
    student_name = input("What is your name? ")
    student_sex = input("What is your sex? (M/F) ")
    student_grade = input("What is your grade? (9/10/11/12) ")
    array_of_info = [student_name, student_sex, student_grade]
    
    return array_of_info

def simple_print(student_info):
    print(f"Hello, {student_info[0]}! Welcome to class!")
    print(f"You are {student_info[1]} and in grade {student_info[2]}.")
    
if __name__ == "__main__":
some_array = ["some stuff", "multiple times", 1, 7]
    
    
    student_info = student_intake()
    simple_print(student_info)