from student import Student
import manager

def main():
    students = []
    
    while True:
        print("\n=== Student Manager ===")
        print("1. Add student")
        print("2. Show all students")
        print("3. Change student score")
        print("4. Save")
        print("5. Load from file")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Enter student name: ")
            score = float(input("Enter student score: "))
            manager.add_student(students, name, score)
        elif choice == "2":
            for student in students:
                print(student.introduce())
        elif choice == "3":
            name = input("Enter the name of the student whose score you want to change: ")
            student = manager.find_student(students, name)
            if student is None:
                print("Student not found.")
            else:
                new_score = float(input("Enter new score: "))
                try:
                    student.set_score(new_score)
                except ValueError as e:
                    print(e)
        elif choice == "4":
            manager.save_students(students, "students.txt")
        elif choice == "5":
            students = manager.load_students("students.txt")
        elif choice == "6":
            break

if __name__ == "__main__":
    main()