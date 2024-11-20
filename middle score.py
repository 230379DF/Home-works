grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
middle_grade1 = sum(grades[0])/len(grades[0])
middle_grade2 = sum(grades[1])/len(grades[1])
middle_grade3 = sum(grades[2])/len(grades[2])
middle_grade4 = sum(grades[3])/len(grades[3])
middle_grade5 = sum(grades[4])/len(grades[4])
grades[0] = middle_grade1
grades[1] = middle_grade2
grades[2] = middle_grade3
grades[3] = middle_grade4
grades[4] = middle_grade5
students = sorted(students)
students = list(students)
middle_score = dict(zip(students, grades))
print(middle_score)