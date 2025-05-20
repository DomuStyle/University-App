from django.db import models

# Create your models here.

class Professor(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Semester(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Courses(models.Model):
    name = models.CharField(max_length=25)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL) # one instructor can have multiple classes
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE) # one Semester can have multiple classes
    
    def __str__(self):
        return f"Class: {self.name} Semester: {self.semester}" # returns class and semester as formatted string.
    
class CourseDescription(models.Model):
    description = models.CharField(max_length=255)
    courses = models.OneToOneField(Courses, on_delete=models.CASCADE) # one class can have one description
    
    def __str__(self):
        return f"Class description: {self.description}" # returns class description as formatted string.
    
class Student(models.Model):
    name = models.CharField(max_length=15)
    courses = models.ManyToManyField(Courses) # one student can have multiple classes
   
    def __str__(self):
        return f"{self.name}, {self.course}" # returns student's name and course as formatted string.
    
class StudentsId(models.Model):
    card_id = models.IntegerField(max_length=32, unique=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE) # one student can have one student id

    def __str__(self):
        return f"Student ID: {self.card_id} belongs to:{self.student.name}" # returns student_id number and student name as formatted string.





