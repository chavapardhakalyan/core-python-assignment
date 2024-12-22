class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0


def find_top_performer(students):
    top_student = None
    highest_avg = 0
    for student in students:
        avg = student.calculate_average()
        if avg > highest_avg:
            highest_avg = avg
            top_student = student.name
    return top_student


students_data = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}
student_objects = [Student(name, marks) for name, marks in students_data.items()]
average_marks = {student.name: student.calculate_average() for student in student_objects}
top_performer = find_top_performer(student_objects)
print("Average Marks: " + str(average_marks))
print("Top Performer: " + str(top_performer))
