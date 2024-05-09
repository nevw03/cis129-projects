import csv

# Prompt instructor to enter student records and store them in a CSV file
with open('grades.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])
    
    while True:
        first_name = input("Enter student's first name (or 'done' to finish): ")
        if first_name.lower() == 'done':
            break
        
        last_name = input("Enter student's last name: ")
        exam1 = float(input("Enter Exam 1 grade: "))
        exam2 = float(input("Enter Exam 2 grade: "))
        exam3 = float(input("Enter Exam 3 grade: "))
        
        writer.writerow([first_name, last_name, exam1, exam2, exam3])