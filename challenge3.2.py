def sort_students(students):
  return sorted(students, key=lambda x: x.cgpa, reverse=True)
class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

students = [
  Student("Alice", "001", 9.5),
  Student("Bob", "002", 8.7),
  Student("Charlie", "003", 9.1),
  Student("David", "004", 8.2)
]

sorted_students = sort_students(students)

for student in sorted_students:
  print(student.name, student.roll_number, student.cgpa)
