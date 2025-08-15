
student_grade = {}


def add_student(name, grade):
    student_grade[name] = grade
    print(f"Added {name} with grade {grade}")  

def update_student(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"{name}'s marks updated to {grade}")  
    else:
        print("Name not found!")

def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} was deleted successfully")  
    else:
        print("Name not found!")

def display_all_student():
    if student_grade:
        for name, grade in student_grade.items():  
            print(f"{name}: {grade}")
    else:
        print("No students found. Please add students first.")  

def main():
    while True: 
        print("\nStudent Grade System")
        print("1: Add a student")
        print("2: Update a student")
        print("3: Delete a student")
        print("4: View all students")
        print("5: Exit")  

        try:
            choice = int(input("Please enter your choice (1-5): "))
            
            if choice == 1:
                name = input("Enter student name: ")
                grade = int(input("Enter student grade: "))  
                add_student(name, grade)
                
            elif choice == 2:
                name = input("Enter student name to update: ")
                grade = int(input("Enter new grade: "))
                update_student(name, grade)
                
            elif choice == 3:
                name = input("Enter student name to delete: ")
                delete_student(name)
                
            elif choice == 4:
                display_all_student()
                
            elif choice == 5:  
                print("Program closing...")
                break
                
            else:
                print("Invalid choice. Please enter 1-5.")
                
        except ValueError:  
            print("Please enter a valid number (1-5)")

if __name__ == "__main__":
    main()