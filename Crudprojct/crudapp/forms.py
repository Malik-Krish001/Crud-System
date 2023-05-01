from django import forms

from crudapp.models import StudentModel

class StudentInfoForm(forms.ModelForm):
    

    class Meta:
        model=StudentModel
        fields = "__all__"