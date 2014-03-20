from django.shortcuts import render_to_response
from django.template import RequestContext
from student.models import Student, Module

def StudentsAll(request):
        students = Student.objects.all().order_by('name')
        context = {'students': students}
        return render_to_response('studentsall.html', context, context_instance=RequestContext(request))

def SpecificStudent(request, studentslug):
        student = Student.objects.get(slug=studentslug)
        context = {'student': student}
        return render_to_response('singlestudent.html', context, context_instance=RequestContext(request))

def SpecificModule(request, moduleslug):
        module = Module.objects.get(slug=moduleslug)
        students = Student.objects.filter(module=module)
        context = {'students': students}
        return render_to_response('singlemodule.html', context, context_instance=RequestContext(request))
