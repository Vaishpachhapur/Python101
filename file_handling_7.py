'''
7.File handiling:
1. student_marks.csv contains the marks and other details for some students.
Write a python program to:
1. Open the file in read mode
2. Create a dictionary from the given data
3. Add a new field to the dictionary total\_marks and store the total marks of
the students.
4. Add a new field to the dictionary Average and store the average marks of the
students.
5. Create a new file and write this information to the new file
(https://www.kaggle.com/arunkumar413/studentmarks)
2. Create a new CSV file with the newly created total marks and average marks.

'''
#1
import csv
input_file = 'student_marks.csv'
output_file = 'updated_student_marks.csv'
students = []

with open(input_file, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        
        subjects = [int(row[key]) for key in row if key.startswith('subject')]
        total_marks = sum(subjects)
        average_marks = total_marks / len(subjects) if subjects else 0
        
        row['total_marks'] = total_marks
        row['average_marks'] = average_marks
        
        students.append(row)

with open(output_file, mode='w', newline='') as file:
    fieldnames = csv_reader.fieldnames + ['total_marks', 'average_marks']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    csv_writer.writeheader()
    csv_writer.writerows(students)

#2
total_average_file = 'total_average_marks.csv'
with open(total_average_file, mode='w', newline='') as file:
    fieldnames = ['Student_ID', 'total_marks', 'average_marks'] 
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    csv_writer.writeheader()
    for student in students:
        csv_writer.writerow({
            'Student_ID': student.get('Student_ID'),
            'total_marks': student['total_marks'],
            'average_marks': student['average_marks']
        })

