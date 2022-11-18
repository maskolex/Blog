from django.forms import *
from deflor.models import Women


class AddWomen(ModelForm):
    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'is_published', 'photo', 'cat']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'slug': TextInput(attrs={'class': 'form-control'}),
            'content': Textarea(attrs={'class': 'form-control'}),
            'is_published': CheckboxInput(attrs={'class': 'form-check-input'}),
            'photo': FileInput(attrs={'class': 'form-control'}),
            'cat': Select(attrs={'class': 'form-select form-select-sm', 'aria-label': '.form-select-sm example'}),
        }
