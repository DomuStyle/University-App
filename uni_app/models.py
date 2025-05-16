from django.db import models

# Create your models here.
class Classes():
    def __str__(self):
        return self.name

class Instructor():
    def __str__(self):
        return self.name

class Student():
    def __str__(self):
        return self.name

class Semester():
    def __str__(self):
        return self.name

class ClassDescription():
    def __str__(self):
        return self.name

