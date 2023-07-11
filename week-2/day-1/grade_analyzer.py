student_grades = [('Sam', 96.7),('Dan', 89.0), ('Anne', 87.3), ('James', 70.7), ('Eric', 78.9), ('David', 85.7), ('Darmien', 69.0)]

def grade_analyzer(student_grades, operation):
    if operation == 'average':
        total = 0
        for student in student_grades:
            total += student[1]
        return total / len(student_grades)
    
    elif operation == 'highest':
        highest = student_grades[0][1]
        for student in student_grades:
            if student[1] > highest:
                highest = student[1]
        return highest
    
    elif operation == 'lowest':
        lowest = student_grades[0][1]
        for student in student_grades:
            if student[1] < lowest:
                lowest = student[1]
        return lowest
            
    else:
        raise ValueError('Invalid Operation')
    
average = grade_analyzer(student_grades, 'average')
highest = grade_analyzer(student_grades, 'highest')
lowest = grade_analyzer(student_grades, 'lowest')
print(f'Average: {average}')
print(f'Highest: {highest}')
print(f'Lowest: {lowest}')
