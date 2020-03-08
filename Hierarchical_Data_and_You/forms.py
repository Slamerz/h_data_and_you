from django import forms
from Hierarchical_Data_and_You.models import File


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = [
            'name',
            'parent',
            'user'
        ]

    def __str__(self):
        return self.name
