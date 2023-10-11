from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project, ProjectInstance


# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required(login_url="login")
def index(request):
    return render (request, 'index.html' )


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    template_name ='project/project_list.html'
    queryset = Project.objects.all()
    paginate_by = 10


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    template_name ='project/project_detail.html'


class OwnedProjectsByUserListView(LoginRequiredMixin, generic.ListView):
    model = ProjectInstance
    template_name ='project/project_i_list.html'
    paginate_by = 10

    def get_queryset(self):
        return ProjectInstance.objects.filter(investor=self.request.user).order_by('date_acquired')
    
class OwnedProjectsByUserDetailView(LoginRequiredMixin, generic.DetailView):
    model = ProjectInstance
    template_name ='project/project_i_detail.html'
    paginate_by = 10
    context_object_name = 'pi'


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ProyectCreate(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title','summary','mini_summary','company', 'date_published', 'interest_rate']
    initial={'date_published':'01/01/2024'}
    

class ProyectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['title','summary','mini_summary','company', 'date_published', 'interest_rate']
    

class ProyectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('projects')
    

class ProyectInstanceCreate(LoginRequiredMixin, CreateView):
    model = ProjectInstance
    fields = ['id','project','date_acquired','date_of_end_contract', 'investment', 'investor', 'rate_time']
    initial={'date_acquired':'01/01/2024', 'date_of_end_contract': '01/01/2024'}
    

class ProyectInstanceUpdate(LoginRequiredMixin, UpdateView):
    model = ProjectInstance
    fields = ['id','project','date_acquired','date_of_end_contract', 'investment', 'investor', 'rate_time']
    

class ProyectInstanceDelete(LoginRequiredMixin, DeleteView):
    model = ProjectInstance
    success_url = reverse_lazy('projects')
    

"""def bid(request):
    if request.method =='POST':
        name=request.POST['name']
        proyect=request.POST['proyect']
        email=request.POST['email']
        date_acq=request.POST['date_acq']
        end_cont=request.POST['end_cont']
        amount=request.POST['amount']
        message = name + " se interesa en " + proyect + ". Su email es: " + email + ". Inicio: " + date_acq + ". Fin: " + end_cont + ". Monto: " + amount
        email_from=settings.EMAIL_HOST_USER,
        send_mail(
            'Puja',
            message,
            email_from,
            [email],
            
        
        )
        return render(request, 'index.html')
    return render(request, 'bid.html')"""
   






    







