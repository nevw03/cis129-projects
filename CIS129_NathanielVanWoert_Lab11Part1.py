with open('grades.txt', mode='w') as grades:
    while True:
        grade = input("Enter a grade (or 'done' to finish): ")
        if grade.lower() == 'done':
            break
        grades.write(grade + '\n')