from django import forms

class CategoryGroupForm(forms.Form):
    category_group_name = forms.CharField(max_length=100)