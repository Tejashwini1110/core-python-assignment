class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def calculate_average(self):
        return sum(self.marks) / len(self.marks)
def track_performance(students):
    averages = {}
    top_performer = None
    highest_average = -1
    for name, marks in students.items():
        student = Student(name, marks)
        average = student.calculate_average()
        averages[name] = round(average, 2)
        if average > highest_average:
            highest_average = average
            top_performer = name
    return averages, top_performer
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
average_marks, top_performer = track_performance(students)
print("Average Marks:", average_marks)
print("Top Performer:", top_performer)
