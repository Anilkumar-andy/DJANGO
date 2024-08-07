from faker import Faker
from django.db.models import Sum
fake = Faker()
import random
from . models import *

def seed_db(n=15):
    try:
        for i in range(0,n):
            student_id = f'STU-0{random.randint(100,9999)}'
            departments_objs=Department.objects.all()
            random_index = random.randint(0,len(departments_objs)-1)
            department = departments_objs[random_index]
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(19,35)
            student_address = fake.address()
        
            student_id_obj = StudentID.objects.create(student_id=student_id)
        
            student_obj = Student.objects.create(
                student_id = student_id_obj,
                department = department,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address,
            )
    except Exception as e:
        print(e)
        
def create_subject_marks(n):
    try:
        student_objs = Student.objects.all()
        for student in student_objs:
            subjects =Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    subject = subject,
                    student = student,
                    marks = random.randint(0,100),
                )
    except Exception as e:
        print(e)
        
def generate_report_card():
    current_rank =-1
    queryset_ranks = Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks') #bit  of complicated query
    
    i=1
    
    for rank in queryset_ranks:
        ReportCard.objects.create(
            student = rank,
            student_rank =i
        )
        i+=1