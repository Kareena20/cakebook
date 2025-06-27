from django import forms
from .models import CakeRecipe

class CakeRecipeForm(forms.ModelForm):
    class Meta:
        model = CakeRecipe
        fields = ['title', 'ingredients', 'instructions', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'ingredients': forms.Textarea(attrs={'rows': 5, 'class': 'form-textarea'}),
            'instructions': forms.Textarea(attrs={'rows': 6, 'class': 'form-textarea'}),
        }
