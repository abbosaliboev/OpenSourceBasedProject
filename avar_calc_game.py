class Student:
    def __init__(self, student_id, name, english_score, c_score, python_score):
        self.student_id = student_id
        self.name = name
        self.english_score = english_score
        self.c_score = c_score
        self.python_score = python_score
        self.total_score = self.english_score + self.c_score + self.python_score
        self.average_score = self.total_score / 3
        self.grade = self.calculate_grade()
        self.rank = None

    def calculate_grade(self):
        average = self.average_score
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'


class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def calculate_rank(self):
        self.students.sort(key=lambda x: x.total_score, reverse=True)
        for i, student in enumerate(self.students):
            student.rank = i + 1

    def search_by_student_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_by_name(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def count_students_above_80(self):
        count = sum(1 for student in self.students if student.total_score >= 240)
        return count


def main():
    grade_manager = GradeManager()

    # 입력 함수
    for _ in range(5):
        student_id = input("학번을 입력하세요: ")
        name = input("이름을 입력하세요: ")
        english_score = int(input("영어 점수를 입력하세요: "))
        c_score = int(input("C언어 점수를 입력하세요: "))
        python_score = int(input("파이썬 점수를 입력하세요: "))

        student = Student(student_id, name, english_score, c_score, python_score)
        grade_manager.add_student(student)

    # 총점/평균 계산 함수
    grade_manager.calculate_rank()

    # 등수계산 함수
    for student in grade_manager.students:
        print(f"이름: {student.name}, 총점: {student.total_score}, 평균: {student.average_score}, 학점: {student.grade}, 등수: {student.rank}")

    # 탐색함수(학번)
    search_id = input("검색할 학번을 입력하세요: ")
    result_student_id = grade_manager.search_by_student_id(search_id)
    if result_student_id:
        print(f"학번 {search_id}에 해당하는 학생 정보: {result_student_id.name}")
    else:
        print("해당 학번을 가진 학생이 존재하지 않습니다.")

    # 탐색함수(이름)
    search_name = input("검색할 학생 이름을 입력하세요: ")
    result_name = grade_manager.search_by_name(search_name)
    if result_name:
        print(f"이름 {search_name}에 해당하는 학생 정보: {result_name.student_id}")
    else:
        print("해당 이름을 가진 학생이 존재하지 않습니다.")

    # 정렬(총점)함수
    grade_manager.students.sort(key=lambda x: x.total_score, reverse=True)
    print("총점순 정렬 결과:")
    for student in grade_manager.students:
        print(f"이름: {student.name}, 총점: {student.total_score}")

    # 80점 이상 학생 수 카운트 함수
    count_above_80 = grade_manager.count_students_above_80()
    print(f"80점 이상인 학생 수: {count_above_80}")


if __name__ == "__main__":
    main()
