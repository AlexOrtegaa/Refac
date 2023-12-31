from django.db import models
from django.urls import reverse
from users.models import Profile
import uuid
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class Project(models.Model):
    
    title = models.CharField(max_length=200, help_text='Ingresa el título del proyecto.')
    summary = models.TextField(default="",max_length=1000, help_text='Ingresa una descripción de la inversión.')
    mini_summary = models.TextField(default="",max_length=50, help_text='Ingresa una descripción breve de la inversión. No más de 50 carácteres.')
    company = models.CharField(max_length=200, help_text='Ingresa el nombre de la compañía que dirige el proyecto.')
    date_published = models.DateField(null=True, blank=True, help_text='Fecha de publicación.')
    interest_rate = models.DecimalField(default=0, max_digits=10, decimal_places=8)

    # add image 
    def __str__(self):
        return f'{self.title}, {self.company}'

    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])
    class Meta:
        permissions = (("can_add_project", "Puede añadir proyecto"),)
    
class ProjectInstance(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    date_acquired = models.DateField(null=True, blank=True, help_text='Fecha de unión al proyecto')
    date_of_end_contract = models.DateField(null=True, blank=True, help_text='Fecha de fin de unión al proyecto')
    investment = models.DecimalField(default=0, max_digits=19, decimal_places=10)
    investor =  models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    rate_time = models.IntegerField(default=0)
    
    
    @property
    def proyect_participation_ended(self):
        if self.date_of_end_contract and date.today() > self.date_of_end_contract:
            return True
        return False
    
    def get_absolute_url(self):
        return reverse('my-project', args=[str(self.id)])
    
    def __str__(self):
        return '%s (%s)' % (self.investor, self.project.title)
    class Meta:
        permissions = (("can_add_instance_project", "Puede añadir inversión"),)
    
    

