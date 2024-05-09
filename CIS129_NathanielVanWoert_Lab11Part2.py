with open('grades.txt', 'r') as file:
    grades = [float(line.strip()) for line in file]

total = sum(grades)
count = len(grades)
average = total / count

print("Individual Grades:")
for grade in grades:
    print(grade)

print("\nTotal:", total)
print("Count:", count)
print("Average:", average)