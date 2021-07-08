from django import forms
from .models import Project_ing

class ProjectingForm(forms.ModelForm):
    class Meta:
        model = Project_ing
        fields=['title_ing', 'project_name_ing','body_ing']