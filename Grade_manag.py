class Student:
    def __init__(self, student_id, name, english_score, c_score, python_score):
        self.student_id = student_id
        self.name = name
        self.english_score = english_score
        self.c_score = c_score
        self.python_score = python_score
        self.total_score = english_score + c_score + python_score
        self.average_score = self.total_score / 3
        self.grade = self.calculate_grade()
    
    def calculate_grade(self):
        if self.average_score >= 90:
            return 'A'
        elif 80 <= self.average_score < 90:
            return 'B'
        elif 70 <= self.average_score < 80:
            return 'C'
        elif 60 <= self.average_score < 70:
            return 'D'
        else:
            return 'F'

class ScoreManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Student with ID {student_id} removed successfully.")
                return
        print(f"Student with ID {student_id} not found.")

    def search_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_student_by_name(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def calculate_rank(self):
        self.students.sort(key=lambda x: x.total_score, reverse=True)
        for i, student in enumerate(self.students):
            student.rank = i + 1

    def count_students_above_80(self):
        count = 0
        for student in self.students:
            if student.total_score >= 240:  # Assuming total score out of 300
                count += 1
        return count

    def display_students(self):
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, Total Score: {student.total_score}, "
                  f"Average Score: {student.average_score}, Grade: {student.grade}, Rank: {student.rank}")

def main():
    score_manager = ScoreManager()

    for _ in range(5):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        english_score = int(input("Enter English score: "))
        c_score = int(input("Enter C score: "))
        python_score = int(input("Enter Python score: "))
        student = Student(student_id, name, english_score, c_score, python_score)
        score_manager.add_student(student)

    score_manager.calculate_rank()
    score_manager.display_students()

    count_above_80 = score_manager.count_students_above_80()
    print(f"Number of students with total score above 80: {count_above_80}")

if __name__ == "__main__":
    main()
