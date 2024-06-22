from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator  #paginator 
from django.db.models import Q,Sum #this models helps to implement multiple queries in search condition using logical operators
from .models import *


# Create your views here.
def get_student(request):
    queryset=Student.objects.all()
    queryset_ranks = Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks') #bit  of complicated query
    for rank in queryset_ranks:
        print(rank.marks)
        search=request.GET.get('search')
    if request.GET.get('search'):
        queryset=queryset.filter(Q(student_name__icontains=search)|
                                 Q(student_age__icontains=search)|
                                 Q(student_id__student_id__icontains=search)|
                                 Q(department__department__icontains=search)|
                                 Q(student_address__icontains=search)|
                                 Q(student_email__icontains=search)
                                 )
        
    paginator = Paginator(queryset, 25)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # print(page_obj.object_list)
    return render(request,'students/student.html',{'queryset':page_obj,'ranks':queryset_ranks})
    
def see_marks(request,student_id):
    queryset=SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    queryset_name =get_object_or_404(Student,student_id__student_id=student_id)
    
    #current_rank= -1
    # queryset_ranks = Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks') #bit  of complicated query
    
    # i=-1
    
    # for rank in queryset_ranks:
    #     if student_id == rank.student_id.student_id:
    #         current_rank=i
    #         break
    #     i=i+1
    # #this is not an efficient way of generating rank for n no of ranks

    # print(queryset_name)
    queryset_rank=get_object_or_404(ReportCard,student__student_id__student_id=student_id)

    total_marks=queryset.aggregate(total_marks=Sum('marks'))
    context = {
        'queryset': queryset,
        'queryset_name': queryset_name,
        'total_marks':total_marks,
        'queryset_rank':queryset_rank
    }
    return render(request,'students/detail_marks.html',context)