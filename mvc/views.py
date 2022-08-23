from django.shortcuts import render

# Create your views here.

from mvc.models import Student

def welcome_page(request):
    return render(request,template_name='index.html')

def add(req):
    message = ''
    if req.method == 'POST':
        formdata = req.POST
        if formdata:
                stud = Student(name=formdata.get('fname'),)
                stud.save()
                message = 'Student Record Saved..'

    return render(req,template_name='add.html',context={"result":message})

def fetch_student_for_edit(request,sid):
    student = Student.objects.get(id=sid)
    return render(request, template_name='update.html', context={"student": student})

def update(req):
        message = ''
        formdata = req.POST
        sid=formdata.get('id')
        student = Student.objects.get(id=sid)
        student.id =formdata.get('id')
        student.name=formdata.get('fname')
        student.save()
        stud_list = Student.objects.all()

        message='Student Updated.....!!!'

        return render(req,template_name='list.html',context={"result":message,"student_list": stud_list})


def delete_student_record(req,sid):
    message=''
    stud = Student.objects.get(id=sid)
    stud.delete()

    message = 'Stud' \
              '' \
              'ent Record Removed..'

    stud_list = Student.objects.all()
    return render(req, template_name='list.html',context={"student_list": stud_list,"result":message})


def show_list_of_students(req):
    stud_list = Student.objects.all()
    return render(req, template_name='list.html',context={"student_list":stud_list})

name_flag = True

def sorting_logic(req,val):
    print(val)
    global name_flag
    if val=='name':
        if name_flag:
            name_flag = False
            stud_list = Student.objects.order_by(val)[::-1]
        else:
            name_flag = True
            stud_list = Student.objects.order_by(val)
        #stud_list = Student.objects.order_by(val)

        return render(req, template_name='list.html', context={"student_list": stud_list})
