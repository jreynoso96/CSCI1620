def init():
    students = int(input('Enter number of students: '))
    grades_in(students)

def grades_in(students):
    while True:
        grades = input('Enter grades: ')
        gList = grades.split()
        gList = [int(i) for i in gList]
        if len(gList) >= students:
            break
    grades_sort(students, gList)

def grades_sort(students, gList):
    sorted_grades = []
    temp_list = gList[:students]
    best = max(temp_list)
    for i in range(len(temp_list)):
        if best - temp_list[i] <= 10:
            sorted_grades.append('A')
        elif best - temp_list[i] <= 20:
            sorted_grades.append('B')
        elif best - temp_list[i] <= 30:
            sorted_grades.append('C')
        elif best - temp_list[i] <= 40:
            sorted_grades.append('D')
        else:
            sorted_grades.append('F')
    display(sorted_grades, temp_list)


def display(gLetter, gNumber):
    for i in range(len(gLetter)):
        print ('Student ' + str(i+1) + ' score is ' + str(gNumber[(i)]) + ' and grade is ' + gLetter[i])

if __name__ == '__main__':
    init()