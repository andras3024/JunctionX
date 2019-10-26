from django import forms
from .models import Child


class AddChild(forms.ModelForm):

    class Meta:
        model = Child
        fields = ('name', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
            'image': forms.ImageField(),
        }
        labels = {
                'name': "Name of Card:",
        }

    def clean(self):
        all_clean_data = super().clean()
