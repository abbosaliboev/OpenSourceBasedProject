#5명의 학생의 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램



def sum_score(score):
    sum=0
    sum+=score
    return sum

def avarage_score(score):
    avarage=sum_score()/5
    return avarage

def grade_score(score):
    if score >= 95:
        grade = 'A+'
    elif score >= 90:
        grade = 'A'
    elif score >= 85:
        grade = 'B+'
    elif score >= 80:
        grade = 'B'
    elif score >= 75:
        grade = 'C+'
    elif score >= 70:
        grade = 'C'
    elif score >= 65:
        grade = 'D+'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
        return grade
    
    def level_score(score):
        if score>100:
            level+=score
        return 
    
    student_number=[]

    for i in range(0,5,1):
        student_number.append(input(f'Enter a student number -  {i+1}'))

    