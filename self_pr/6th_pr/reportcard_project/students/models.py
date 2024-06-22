from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=75)
    
    def __str__(self):
        return self.department
    
    # this is done to order the records in ascending order based on the specified in this department, -department for descending
    class Meta:
        ordering = ['department']
    
class StudentID(models.Model):
    student_id = models.CharField(max_length=25,unique=True)

    def __str__(self):
        return self.student_id
    
class Subject(models.Model):
    subject_name = models.CharField(max_length=75)
    
    def __str__(self):
        return self.subject_name
    
    
class Student(models.Model):
    student_id = models.OneToOneField(StudentID,related_name='studentid',on_delete=models.CASCADE)
    # foreign key is same as one to many & many to one
    department = models.ForeignKey(Department, related_name="depart",on_delete=models.CASCADE) 
    student_name = models.CharField(max_length=75)
    student_email = models.CharField(max_length=50,unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self):
        return self.student_name
    
    class Meta:
        ordering = ["student_name"]
        verbose_name = "student"
        
class SubjectMarks(models.Model):
    student = models.ForeignKey(Student,related_name="studentmarks",on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks= models.IntegerField()
    def __str__(self):
        return f"{self.student.student_name}has got {self.marks}in{self.subject.subject_name}"
    class meta:
        unique_together = ['student','subject']
        
class ReportCard(models.Model):
        student = models.ForeignKey(Student,related_name="studentreportcard",on_delete=models.CASCADE)
        student_rank = models.IntegerField()
        date_of_report_card_generation =models.DateField(auto_now_add=True)
        
        class Meta:
            unique_together = ['student_rank','date_of_report_card_generation','student']
        
        