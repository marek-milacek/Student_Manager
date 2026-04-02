from student import Student

def add_student(students, name, score):
    student = Student(name, score)
    students.append(student)
    return student

def find_student(students, name):
    for student in students:
        if student.name == name:
            return student
    return None

def save_students(students, filename):
    with open(filename, 'w') as f:
        for s in students:
            f.write(f"{s.name},{s.score}\n")

def load_students(filename):
    students = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 2:
                continue
            name = parts[0].strip()
            try:
                score = float(parts[1].strip())
            except ValueError:
                continue
            students.append(Student(name, score))
    return students
