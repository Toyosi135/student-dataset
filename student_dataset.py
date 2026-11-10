import csv
students = [
    ["Student ID", "Department", "Level", "Attendance Percentage", "Average Examination Score"],

    ["ST001", "Cybersecurity", 200, 85, 78],
    ["ST002", "Computer Science", 300, 90, 82],
    ["ST003", "Software Engineering", 200, 75, 65],
    ["ST004", "Cybersecurity", 300, 95, 88],
    ["ST005", "Computer Science", 400, 80, 72],
    ["ST006", "Information Technology", 200, 70, 60],
    ["ST007", "Cybersecurity", 400, 92, 85],
    ["ST008", "Software Engineering", 300, 88, 80],
    ["ST009", "Computer Science", 200, 65, 55],
    ["ST010", "Information Technology", 400, 98, 91]
]

# Displaying the dataset

print("FICTIONAL STUDENT DATASET")
print("---------------------------------------------")

for student in students:
    print(student)

# Saving the dataset into a CSV file

with open("student_dataset.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(students)

print("---------------------------------------------")
print("Student dataset created successfully!")
print("File saved as student_dataset.csv")