from django.forms import ModelForm, Textarea, forms
from deflor.models import Women


class AddWomen(ModelForm):
    class Meta:
        model = Women
        fields = ['title', 'content', 'is_published', 'cat']
        widgets = {
            'title': forms.Textinput(attrs={'class': 'form-control'}),
            'content': Textarea(attrs={'class': 'form-control'}),
            'is_published': forms.ChoiceField(attrs={'class': 'form-control'}),
        }
