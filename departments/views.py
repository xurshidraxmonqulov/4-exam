from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Department
from .forms import DepartmentForm
from teachers.models import Teacher
from students.models import Student
from subjects.models import Subject
from groups.models import Group


class HomePageView(ListView):
    model = Student
    template_name = 'dashboard.html'
    context_object_name = 'departments'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        subjects = Subject.objects.prefetch_related('teachers')
        ctx['teachers'] = Teacher.objects.all()
        ctx['groups'] = Group.objects.all()
        ctx['subjects'] = subjects
        ctx['groups_count'] = Group.objects.filter(status='ac').count()
        ctx['subject_names'] = [subject.subject_name for subject in Subject.objects.all()]
        ctx['subject_teachers_counts'] = [subject.teachers.count() for subject in Subject.objects.all()]
        return ctx


class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/list.html'
    context_object_name = 'departments'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'departments/detail.html'
    context_object_name = 'department'


class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/form.html'
    success_url = reverse_lazy('departments:list')


class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/form.html'
    success_url = reverse_lazy('departments:list')


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'departments/confirm_delete.html'
    success_url = reverse_lazy('departments:list')